#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 3 Step 2")
print("Step 2 - input key from step 1 and encrypted text into encryption code to decipher text")
print() #Print space

def encrypt(text, key):                    #Encryption code
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - key
            if shifted < ord('a'):
                shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

key = 13                                         #Input key from encryption code

original_code="""                          
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        vs ybpny_inevnoyr % 2 == 0:
            ahzoref.erzbir(ybpny_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr (5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""
encrypted_code = encrypt(original_code, key)
print(encrypted_code)                            #Prints decrypted text

input("Press enter to close the program") #so user can see the output