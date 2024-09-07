#Encryption code

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isaplha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                 shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted +=26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

key = ????????????????
encrypted_code = encrypt(original_code, key)
print(encrypted_code)

#Decryption key

total = 0
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

print(total)
