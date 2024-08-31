






import time

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)

from PIL import Image
img = Image.open('Chapter1.png') # open image
img = img.convert("RGB") # convert to RGB