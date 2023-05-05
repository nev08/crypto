import numpy as np


key = np.array([[9, 4], [5, 7]])
alphabet = "abcdefghijklmnopqrstuvwxyz"
def char_to_num(c):
    return alphabet.index(c.lower())
def num_to_char(n):
    return alphabet[n % 26]
def encrypt(message, key):
  
    message = np.array([char_to_num(c) for c in message])
    message = np.reshape(message, (-1, 2)).T
    
   
    if message.shape[1] % 2 == 1:
        message = np.concatenate((message, np.zeros((2, 1))), axis=1)
    
    
    ciphertext = np.matmul(key, message) % 26
    
    
    ciphertext = "".join([num_to_char(n) for n in ciphertext.T.flatten()])
    
    return ciphertext

def decrypt(ciphertext, key):
    
    det = key[0][0] * key[1][1] - key[0][1] * key[1][0]
    inv_key = np.array([[key[1][1], -key[0][1]], [-key[1][0], key[0][0]]]) * det
    inv_key = inv_key % 26
    
    
    ciphertext = np.array([char_to_num(c) for c in ciphertext])
    ciphertext = np.reshape(ciphertext, (-1, 2)).T
    
    
    plaintext = np.matmul(inv_key, ciphertext) % 26
    
    
    plaintext = "".join([num_to_char(n) for n in plaintext.T.flatten()])
    
    return plaintext


message = "meet me at the usual place at ten rather than eight oclock"
ciphertext = encrypt(message, key)
print("Ciphertext:", ciphertext)


plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)
