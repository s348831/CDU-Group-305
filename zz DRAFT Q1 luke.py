#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 1")
print() #Print space
import csv
import os

def csvs_to_text(csv_file_paths, text_file_path):
    try:
        with open(text_file_path, mode='w', encoding='utf-8') as text_file: #open text file combined.txt
            for csv_file_path in csv_file_paths:
                if not os.path.exists(csv_file_path):
                    continue
                
                with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file: #open CSV file 
                    csv_reader = csv.reader(csv_file)
                    
                    for row in csv_reader: #write contents of CSV to text file
                        line = ','.join(row)
                        text_file.write(line + '\n')

                print(f"Content from '{csv_file_path}' has been written to '{text_file_path}'")
        
        print(f"Content from CSV files has been written to '{text_file_path}'")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Run function with CSV files and output path
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']  # CSV files to be converted
output_file = 'combined.txt' #text file to be written to
csvs_to_text(csv_files, output_file)
