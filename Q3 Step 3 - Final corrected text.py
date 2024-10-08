#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 3 Step 3 - Run decrypted text and fix all errors")
print() #Print space

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

#my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}         #Duplicate numbers in a set cancel out, this set should be {1, 2, 3, 4, 5} to provide the same result
my_set = {1, 2, 3, 4, 5}
#result = process_numbers(numbers=my_set)        #Remove numbers=my_set as process_numbers doesnt require a parameter
result = process_numbers()

#def modify_dict():                               #Added local_variable into modify_dict() to assign variable 10 to key4 and ensure line 51 coditions are met
def modify_dict(local_variable):
    local_variable = 10
    my_dict['key4'] = local_variable             

#modify_dict(5)                                   #5 is not used as its overwritten by the assignment of 10 above, change number to 10 inside the perenthises 
modify_dict(10)

def update_global():
    global global_variable
    global_variable += 10

update_global()                                 #Add update_global if the code intends to update the global variable
            
for i in range (5):
    print(i)
    #i += 1                                     #i += 1 is not required as the for call already takes care of incrementing i

if my_set is not None and my_dict['key4'] == 10:   
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")        

print(global_variable)
print(my_dict)
print(my_set)

input("Press enter to close the program") #so user can see the output
