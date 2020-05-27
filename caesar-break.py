#!/usr/bin/python3

from secretpy import alphabets
from secretpy import Caesar
from ngramscore import NGramScore 


alphabet = alphabets.GERMAN

fitness = NGramScore('de.txt')
cipher = Caesar()

def crack(ctext):
    max_score = 0 
    key = 0 
    for i in range(0, len(alphabet)):
        dec = cipher.decrypt(ctext, i, alphabet)
        score = fitness.score(dec)
        print("key = " + str(i) + ", decrypted text: " + str(dec.upper()) + ", score: " + str(score))
        if score > max_score:
            max_score = score
            key = i
    return key 

# example ciphertext
enc = 'äbööemökglbgäßnm'
print("encrypted text: " + enc)
print()

key = crack(enc)

print()
print('best key = ' + str(key) + ':')
print(cipher.decrypt(enc, key, alphabet).upper())
