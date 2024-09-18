#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 1 Task 3.1")
print() #Print space

from collections import Counter
import csv
import re

#opens the file. the with statement here will automatically close it afterwards.
with open("text.txt") as file:
    text=file.read()
words= re.findall(r'\b[a-zA-Z]+\b', text) #extracts all the words in the text (no numbers, punctuation or symbols)
#build a counter from each word in the file
count = Counter(words)

List = dict(count.most_common(30))
print(List)
#print(type(List)) #Used to workout if class dict was sucessfull

#Create csv file from dictionary.
with open('Listwords.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in List.items():
       writer.writerow([key, value])

input("Press enter to close the program") #so user can see the output
