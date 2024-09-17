#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 2 Task 2.1")
print() #Print space

s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

#seperate string into a string of numbers and letters

alpha = '' #string of letters
num = '' #string of numbers

for char in s: #check each character, if it is a letter, add it to alpha nad if it's a number add to num 
    if char.isalpha(): 
        alpha+=char
    elif char.isdecimal():
        num+=char

print("Letter string: ", alpha)
print("Number string: ", num)
print()

#Convert even numbers in numbers string to ASCII code decimal values

decnum = [] #create a 2 lists, one for the even numbers and one for their ASCII values
asciinum = []

for i in range(len(num)):
    if int(num[i])%2==0: #Check if the number is even
        decnum.append(int(num[i])) #add to list of even numbers
        asciinum.append(int(ord(num[i]))) #create list of ASCII code of the even numbers
        

print(*decnum, sep=", ", end=" (Even Numbers)\n")
print(*asciinum, sep=", ", end=" (ASCII Code)\n")
print()

#Convert upper-case letters in letters string to ASCII code decimal values

upper = []
asciiupper = []

for i in alpha:
    if i.isupper():
        upper.append(i)
        asciiupper.append(int(ord(i)))
        
print(*upper, sep=", ", end=" (Uppercase Letters)\n")

print(*asciiupper, sep=", ", end=" (ASCII Code)\n")

input("Press enter to close the program")#so user can see the output
