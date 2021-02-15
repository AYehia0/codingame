import sys
import math
import string

letters = string.ascii_uppercase

def update_message(msg, p_num):
    new_msg = ""
    for ind, i in enumerate(msg):
        ind = ind if p_num > 0 else -ind
        ind_letters = letters.index(i) + p_num + ind
        new_msg += letters[ind_letters % len(letters)]
        
    return new_msg


def encode(msg, rotors):
    
    for rotor in rotors:
        n_msg = ""
        for i in msg:
            n_msg += rotor[letters.index(i)]

        msg = n_msg

    return msg

def decode(msg, rotors):
    
    for rotor in reversed(rotors):
        n_msg = ""
        for i in msg:
            n_msg += letters[rotor.index(i)]
        msg = n_msg

    return msg


operation = input()
p_num = int(input())
rotors = list()
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()

if operation == 'ENCODE':
    n_message = update_message(message, p_num)
    n_message = encode(n_message, rotors)
else:
    n_message = decode(message, rotors)
    n_message = update_message(n_message, -1*p_num)
    

print(n_message)