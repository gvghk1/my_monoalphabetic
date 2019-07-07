# Name: Chi Ho Leung
# PID: 6106288
#
# This is a Monoalphabetic Cipher program encryting or decryting message 
# using keys provided by users, or keys gernerated by python library.
#
# Reference: https://gist.github.com/cowdinosaur/4504ab9705f0926c8cf8
# http://inventwithpython.com/hacking (BSD Licensed)

import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters for convertion

def main():
    q = 'y' # default promte value 'y' 
    
    while q == 'y': # if the prompt is not 'n', Cipher keeps running 
        q = input('Do you want to encrypr or decrypt?(y/n)')
        if q == 'y':
            myMessage = input("Enter plain Text\n") 
            myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM' # unique key used for substitution
            myMode = input('Enter mode\n') # promte or encryption or decryption

            checkValidKey(myKey)

            if myMode == 'encrypt': # if input is encrypt
                translated = encryptMessage(myKey, myMessage)
            elif myMode == 'decrypt': # if input is decrypt
                translated = decryptMessage(myKey, myMessage)
            print('Using key %s' % (myKey))
            print('The %sed message is:' % (myMode))
            print(translated)
        elif q == 'n':
            q = 'n'
            print("End") # end of program
        else:
            print("Invalid input") # input invalid
            q = 'y'


def checkValidKey(key): # check to see if letters and keys are 1 to 1
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message): # convert letters to key
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message): # convert key back to letters
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = '' # Empty default string
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA # swapping letters to keys and keys to letters

    # loop through each symbol(letter) in the message
    for symbol in message:
        if symbol.upper() in charsA: # if symbol is in capital and a letter
            # encrypt/decrypt the symbol
            # find index number of specific letter or key
            symIndex = charsA.find(symbol.upper())  
            if symbol.isupper():
                # Concatenating capital case symbols
                translated += charsB[symIndex].upper()
            else:
                # Concatenating lower case symbols
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def getRandomKey(): # generate ramdom key for encrption and decryption
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

main()
