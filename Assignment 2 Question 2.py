#Group name:[Cas group 305]

#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831

print("Cas Group 305 - Assignment 2")
print("Question 2")
print() #Print space

# Import OS and Pillow Library
from PIL import Image
import os

# Provided algorithm
import time

current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print("Generated number: ", generated_number)

# Using OS to load image and paths
input_image_path = os.path.join(os.path.dirname(__file__), 'chapter1.jpg')
output_image_path = os.path.join(os.path.dirname(__file__), 'chapter1out.jpg')

image = Image.open(input_image_path)
pixels = image.load()  # Load pixel data

# Get image dimensions
width, height = image.size

# Process the pixels
for y in range(height):
    for x in range(width):
        R, G, B = pixels[x, y]
        # Change pixel values
        new_R = min(R + generated_number, 255)  # Ensure values are within valid range
        new_G = min(G + generated_number, 255)
        new_B = min(B + generated_number, 255)
        pixels[x, y] = (new_R, new_G, new_B)

# Save the new image
image.save(output_image_path)

# Sum of the red pixel values
total_red = 0

for y in range(height):
    for x in range(width):
        R, _, _ = pixels[x, y]
        total_red += R

print("Sum of all red pixel values: ", total_red)