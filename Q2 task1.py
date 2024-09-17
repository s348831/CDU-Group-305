#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 2")
print() #Print space

#Import OS and Pillow Library
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"]) #ensures that Pillow is installed

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

input("Press enter to close the program") #so user can see the output
