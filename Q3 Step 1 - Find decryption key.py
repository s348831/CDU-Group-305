#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 3 Step 1")
print("Step 1 - Run code to find encryption key")
print() #Print space

total = 0                  #Encryption key code
for i in range (5):
  for j in range (3):
    if i + j == 5:
      total += i + j
    else: total -+ i - j

counter = 0 
while counter < 5:
  if total < 13:
    total += 1
  elif total > 13:
    total -= 1
  else:
    counter += 2

print("Encryption key: ", total)              #Output = Key to decipher text = 13

input("Press enter to close the program") #so user can see the output
