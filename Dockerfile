FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh

ENV PATH=$CONDA_DIR/bin:$PATH

ENV APP_ROOT=/app/ChemEXIN
ENV CONDA_ENV=ChemEXIN

WORKDIR /app

COPY ChemEXIN.yml /app/environment.yml

RUN conda config --system --remove-key channels || true && \
    conda config --system --add channels conda-forge && \
    conda config --system --set channel_priority strict && \
    conda init bash && \
    /bin/bash -c "source $CONDA_DIR/etc/profile.d/conda.sh && \
    conda env create -f /app/environment.yml && \
    conda clean -a -y"

COPY . ${APP_ROOT}

SHELL ["/bin/bash", "-c"]

RUN echo '#!/bin/bash' > /app/entrypoint.sh && \
    echo 'set -e' >> /app/entrypoint.sh && \
    echo "source $CONDA_DIR/etc/profile.d/conda.sh" >> /app/entrypoint.sh && \
    echo "conda activate ${CONDA_ENV}" >> /app/entrypoint.sh && \
    echo 'exec "$@"' >> /app/entrypoint.sh && \
    chmod +x /app/entrypoint.sh

WORKDIR /drive

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["python", "/app/ChemEXIN/main.py"]

