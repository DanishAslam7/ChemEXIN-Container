'''
This program file is part of "ChemEXIN: A Physicochemical Parameter-Based Exon-Intron Boundary Prediction Method" developed by the Computational Genomics group at Supercomputing Facility for Bioinformatics and Computational Biology (SCFBio), Kusuma School of Biological Sciences (KSBS), Indian Institute of Technology (IIT) Delhi, India.
Authors: Dinesh Sharma, Danish Aslam, Kopal Sharma, Aditya Mittal, B Jayaram.

Contact: run478@gmail.com, bjayaram@chemistry.iitd.ac.in 

Lab Webpage: www.scfbio-iitd.res.in
'''
import time
import sys
import pandas as pd
import simple_colors as SC
from src import input_seq_check, combine_tri, combine_tetra, run_model, prediction_df, norm_tri, norm_tetra, preprocess, final_processing_one, final_processing_two,results
import numpy as np

start=time.time()
print(SC.cyan("\n\t\t\tChemEXIN: A Physicochemical Parameter-Based Exon-Intron Boundary Prediction Method developed by SCFBio, IIT Delhi."))
print(SC.magenta(f"Input your file name present in the sequence directory and hit ENTER:"))
file_name = input(SC.green(f"Waiting for user input: "))
file_name = file_name.split(".")
org = input(SC.magenta("\nSelect the organism and hit ENTER:")+SC.red("\n> h or H for H. sapiens")+SC.red("\n> m or M for M. musculus")+SC.red("\n> c or C for C. elegans")+SC.green("\nWaiting for user input: "))
if org.upper() == "H" or org.upper() == "M" or org.upper() == "C":
	print(SC.green(f"\nCarrying forward the analysis with the selected Organism."))
else:
	print(SC.red(f"The entered option doesn't correspond to a valid organism.\nRerun the analysis with the correct options."))
	sys.exit()


processed_seq = preprocess.check_single(f"{('.').join(file_name)}")

output_input_check = input_seq_check.readsequencefile(processed_seq)

if output_input_check:
	normalised_map_tri = norm_tri.calculateParameters(output_input_check)
	combine_dict_tri = combine_tri.combine_params(normalised_map_tri)
	normalised_map_tetra = norm_tetra.calculateParameters(output_input_check)
	all_param_combined_final = combine_tetra.combine_params(normalised_map_tetra,combine_dict_tri)
	final_df = prediction_df.non_over_50(all_param_combined_final)
	pred_results,model = run_model.prediction(final_df,file_name[0],org.upper())
	print(SC.magenta(f"\nSelect the threshold value and hit ENTER else hit ENTER to proceed with default (0.75):"))
	prob = input(SC.red("> a or A for PROB: 0.70")+SC.red("\n> b or B for PROB: 0.80")+SC.red("\n> c or C for PROB: 0.85")+SC.green("\nWaiting for user input: "))
	if prob.upper() == "A":
		prob=0.70
		print(SC.green(f"Carrying forward the analysis with the selected threshold value: {prob}"))
	elif prob.upper() == "B":
                prob=0.80
                print(SC.green(f"Carrying forward the analysis with the selected threshold value: {prob}"))
	elif prob.upper() == "C":
                prob=0.85
                print(SC.green(f"Carrying forward the analysis with the selected threshold value: {prob}"))
	else:
		prob = 0.75
		print(SC.red(f"The entered option doesn't correspond to a valid threshold.\nCarrying the analysis with the default value (0.75)."))
	positions_one = final_processing_one.final_process(pred_results,float(prob))
	print(SC.green(f"	Check 1: PASSED ---> Positions captured successfully."))
	final_refined_pos = final_processing_two.process_pos(positions_one,pred_results)
	print(SC.green(f"	Check 2: PASSED ---> Positions refined successfully."))
	result=results.filter_dict(final_refined_pos,file_name[0],model,prob)
	result.index = result.index+1
	result.index.name="S.No."
	result.to_csv(f"results/{file_name[0]}_results.csv",mode = "a")
	print(SC.green(f"	Check 3: PASSED ---> Output saved successfully to results/{file_name[0]}_results.csv"))
	print(SC.blue("\nSTEP 8/8: SUCCESSFULLY COMPLETED :)"))
else:
	print("\nCANNOT PROCESS FURTHER !")
end=time.time()
print(SC.red(f"Total Execution time: {end-start} secs"))

