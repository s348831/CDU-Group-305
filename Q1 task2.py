#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 1 Task 2")
print() #Print space

print('this may take a few minutes')
print()
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "spacy"])

subprocess.check_call([sys.executable, "-m", "pip", "install", "scispacy"])

subprocess.check_call([sys.executable, "-m", "pip", "install", "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_core_sci_sm-0.5.4.tar.gz"])

subprocess.check_call([sys.executable, "-m", "pip", "install", "https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz"])

subprocess.check_call([sys.executable, "-m", "pip", "install", "transformers"])
