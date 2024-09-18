#Group name:[Cas group 305]
#Group Members:
#[Reece Colgan] - S377586
#[Hayden Powell] - S376682
#[Daniel Sales] - S322244
#[Luke Few] - S348831
print("Cas Group 305 - Assignment 2")
print("Question 2.2")
print() #Print space

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
HELL DONT DESERVE ME AT MY BEST MARILYN MONROE
'''

input("Press enter to close the program")#so user can see the output
