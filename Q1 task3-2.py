#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 1 - Task 3.2")
print() #Print space

# import relevant modules
from collections import Counter
from transformers import LongformerTokenizer

# define function for tokenizer

def token_file(file_path, number=30):
    tokenizer = LongformerTokenizer.from_pretrained("allenai/longformer-base-4096") # tokenizer used for long texts. bert based faults as file is too long >512
    
    with open(file_path, 'r') as file: # read file ***file_path
        content = file.read()
    tokens = tokenizer.tokenize(content) # tokenize text
    counter = Counter(tokens) # count tokens
    top_tokens = counter.most_common(number)
    
    print("Top", number, "Tokens:") # print tokens, number of tokens.
    for token, count in top_tokens:
        print(f"{token}: {count}")
    
    return top_tokens


file_path = "extractdiffcolumn.txt"  #file path of file to tokenize ***edit file name to read here
top_tokens = token_file(file_path, number=30)  # start function and process file

print() #Print space
x = input("Press Enter key to exit")
