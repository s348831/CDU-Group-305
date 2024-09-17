#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 1")
print() #Print space
#import relevant modules
import csv 
import os

def csvs_to_text(csv_file_paths_with_columns, text_file_path):
        with open(text_file_path, mode='w', encoding='utf-8') as text_file: #open text file
            for csv_file_path, columns in csv_file_paths_with_columns.items(): # Check if the nominated csv files exist.
                if not os.path.exists(csv_file_path):
                    print(f"File not found: {csv_file_path}")
                    continue
                
                with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file: #open CSV file
                    csv_reader = csv.reader(csv_file)
                    
                    for row in csv_reader:
                        selected_columns = [row[i] for i in columns if i < len(row)] #selected columns
                        line = ','.join(selected_columns)
                        text_file.write(line + '. \n') #write data to .txt file

                print(f"Selected column from '{csv_file_path}' has been written to '{text_file_path}'")
        
        print(f"Extracted column from all CSV files has been saved to '{text_file_path}'")
    
# set column in CVS to be used in data transfer. these columns were selected based on which column appeard to have the most text
# set the ouptut file name.
csv_files_with_columns = {
    'CSV1.csv': [2],       # column 2 which is C. starts from 0
    'CSV2.csv': [2],       # column 2 which is C. starts from 0
    'CSV3.csv': [1],       # column 0 which is B. starts from 0
    'CSV4.csv': [1]        # column 1 which is B. starts from 0
}
output_file = 'text.txt'
# Run the csvs_to_text function
csvs_to_text(csv_files_with_columns, output_file)
