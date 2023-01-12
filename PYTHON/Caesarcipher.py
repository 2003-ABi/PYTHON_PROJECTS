import string
import sys
try:
    file_name =  sys.argv[1]
    
except IndexError:
    print("file name not given")
    quit()
try:
    with open(file_name,"r") as fp:
        encrypted =  fp.read()
except FileNotFoundError:
    print(f'''Cannot open "{sys.argv[1]}". Sorry about that.''')

def fre(text):
    frequency = {}

    for alphb in text:   #alphabet counter 
        if alphb.isalpha():
            if alphb in frequency:
                frequency[alphb] = frequency[alphb] + 1 #alphbect repetation by adding to same alphabet
            else:
                frequency[alphb] = 1     #alphabet repetation of alphabet in dictionary
    return frequency
    


lower_case = string.ascii_lowercase  #string value store in always stored in  ascii
upper_case = string.ascii_uppercase
alphabet = lower_case + upper_case #addding ascii of both upper and lower in alphabet



enc_fre = fre(encrypted) #no of repetation in alphabet is stored in value i.e [j:129]


max_enc_free_value = max(value  for key,value in enc_fre.items()) #return maximum value stored in enc_free

max_enc_free_key = [i for i in enc_fre if enc_fre[i]==max_enc_free_value]  #reyturn key with maximum value

shifteds = ord(max_enc_free_key[0]) - ord('e') #alphabet difference by substraction high key value with e

decrypt_shifted = lower_case[-shifteds:]+lower_case[:-shifteds]+upper_case[-shifteds:]+upper_case[:-shifteds] #decrypt shifted values 

table = str.maketrans(alphabet,decrypt_shifted) #makes dictionary with encrypted and decrpyted letter

decrypted = encrypted.translate(table) #change decrypted letter to encrypted
if "the" in decrypted:  #to check it is decrypted by caesarcypher algorithm or not" most common word"
    print(decrypted)
    
else:
    print('Cannot decrypt. Most likely not a Caesar Cypher at work here.')
