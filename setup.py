from setuptools import setup, find_packages

setup(
    name="ChemEXIN",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "simple_colors",
    ],
    author="Dinesh Sharma, Danish Aslam, Kopal Sharma, Aditya Mittal, and B. Jayaram",
    description="ChemEXIN: exon–intron boundary prediction using physicochemical DNA features and deep learning.",
    license="GPL-3.0",
    keywords=["genomics", "splice-site", "deep-learning"],
)

