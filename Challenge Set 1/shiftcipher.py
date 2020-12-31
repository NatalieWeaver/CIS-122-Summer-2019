'''
Author: Natalie Weaver
Date: July 3, 2019

CIS 122 Challenge Set 1 part 2: Shift cipher

Sources:
    This ASCII table: https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
    This post on Stack Overflow about converting letters to ASCII because I didn't know about the function ord() yet:
        https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character
'''

plaintext = input("Plaintext message: ")
ciphertext = ""

# Get the secret key and make sure it is an integer, then reduce mod 26.
k = float(input("Secret key: "))
while k % 1 != 0:
    print("Secret key must be an integer.")
    k = float(input("Secret key: "))
k = int(k) % 26

# Starting at the beginning, convert each character of the plaintext to the corresponding ciphertext character by shifting by k.
# We choose to preserve capitalization here.
i = 0
while i < len(plaintext):
    if plaintext[i].isupper():
        cipherletter = chr(((ord(plaintext[i]) - 65 + k) % 26) + 65 )
    elif plaintext[i].islower():
        cipherletter = chr(((ord(plaintext[i]) - 97 + k) % 26) + 97 )
    elif not plaintext[i].isalpha():
        cipherletter = plaintext[i]
        
    ciphertext = ciphertext + cipherletter
    i = i + 1
    
print("Ciphertext message:" , ciphertext)

