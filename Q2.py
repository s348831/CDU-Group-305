#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 2")
print() #Print space

print("Q2 Chapter 1")
#Import OS and Pillow Library
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

from PIL import Image
import os

# Provided algorithm
import time

current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print("Generated number: ", generated_number)

# Using OS to load image 
#ensure that image is in same directory as application

image = Image.open("chapter1.jpg")
pixels = image.load()  # Load pixel data

# Get image dimensions
width, height = image.size

# Process the pixels
for y in range(height):
    for x in range(width):
        R, G, B = pixels[x, y]
        # Change pixel values
        pixels[x, y] = (R+generated_number, G+generated_number, B+generated_number) #RGB values automatically capped at 255

# Save the new image
image.save("chapter1out.jpg")

# Sum of the red pixel values
total_red = 0

for y in range(height):
    for x in range(width):
        R, _, _ = pixels[x, y]
        total_red += R

print("Sum of all red pixel values: ", total_red)

print()
print("Q2 Chapter 2 - Part 1")

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

print()
print("Q2 Chapter 2 - Part 2")

def decrypt(text, key):                   
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.isupper():
                if shifted < ord('A'):
                    shifted +=26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

key = 13  #determined by trial and error                                       

cryptogram="""VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY
NAQ NG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF 
URYY QBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR
"""
encrypted_code = decrypt(cryptogram, key)
print(encrypted_code)

#Output = Deciphered quote
'''
IM SELFISH IMPATIENT AND A LITTLE INSECURE I MAKE MISTAKES I AM OUT OF CONTROL
AND AT TIMES HARD TO HANDLE BUT IF YOU CANT HANDLE ME AT MY WORST THEN YOU SURE AS
'''

input("Press enter to close the program")
