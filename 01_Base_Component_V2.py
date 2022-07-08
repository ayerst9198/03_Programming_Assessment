import time
import sys
from string import ascii_lowercase
import random

# functions go here


def not_blank(question, error_msg):
    valid = False

    while not valid:
        response = input(question)

        if response == "":
            print(error_msg)
        
        # credit: Ryan Ogilvy; for the whitespace checker
        elif str.isspace(response):
            print(error_msg)
        else:
            return response
            

# number checker for key
def num_check(question, num_type, error, exit_code=None):

    valid = False
    while not valid:
        try:
            response = input(question).lower()


            if response == exit_code:
                return response

            else:
                response = num_type(response)
            
            return response

        except ValueError:
            print(error)
            print()


def delay_print(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()


def string_checker(choice, options):
    for var_list in options:

        # if snack is in list return full snack name
        if choice in var_list:

            # get full name of snack and put it 
            # in title case so it looks noice
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        # if choe option is not valid, set is_valid to no
        else:
            is_valid = "no"
    
    # if snack is not ok - ask again
    if is_valid == "yes":
        return chosen
    else: 
        return "invalid choice"


def instructions():

    print()
    print("***Caeser Cipher Instructions***")
    print()
    print()
    print("""This program is designed to easily allow you
to encrypt or decrypt text. When asked
whether you wantto encrypt or decrypt text,
you can input 'e', or 'encrypt' to encrypt
text, 'd' or 'decrypt', to decrypt text, or 
'xxx' to quit the program.

IF you choose to encrypt text, your will be asked to
input a key. This key is a number that decides how 
the text is encrypted. Once you input a key you will
then be asked to input the message you want to encrypt.
The program will then give you the encrypted
message, along with the key.

IF you choose to decrypt, you will first be asked to input
the message to be encrypted, followed by being asked
if you have a key to decrypt with. If you have a key, the
message will be decrypted according to they key, but if you
don't have a key, the program will trial and error through keys,
while asking if the decrypted message is correct. Once you arrive
at the correct message, confirm that the message is correct
and the program will give you the decrypted message
along with the key.

After the encryption or decryption is finished, The program will
loop back to asking if you want to encrypt or decrypt
where you can decide to encrypt or decrypt more messages,
or you could enter 'xxx' to quit.

Please keep in mind that this program is mainly for entertainment
purposes, and is not a secure form of encryption.""")
    return ""

def cipher():

    to_cipher = input("What is the message you would like to encrypt/decrypt?: ").lower()
    if to_cipher == "xxx":
        return "xxx"
    to_cipher = to_cipher.split()
    #ask user if they have a key.
    key_ans = "invalid choice"
    while key_ans == "invalid choice":
        #ask user if they have a key
        print()
        key_ans = input("Do you have a key?: ")
        #check that answer is valid
        key_ans = string_checker(key_ans, yes_no)

        if key_ans == "invalid choice":
            print("Please enter yes or no")
            print()
    if key_ans == "Xxx":
        return "xxx"
    #ask user if they want to encrypt or decrypt
    ask_encryption = "invalid choice"
    print()
    if key_ans == "Yes":
        key = num_check("What is your key? ", int, "Please enter a whole number")
        print()
    while ask_encryption == "invalid choice":

        ask_encryption = input("Do you want to encrypt or decrypt text? ")
        print()
        # check answer is valid
        ask_encryption = string_checker(ask_encryption, encrypt_decrypt)


        if ask_encryption == "invalid choice":
            print()
            print("Please enter decrypt (d), encrypt (e), or xxx to quit.")
            print()

    if ask_encryption == "Xxx":
        return "xxx"
    encrypted = ""
    # if the user has a key, ask if they want to decrypt or encrypt text
    if key_ans == "Yes":


        for item in to_cipher:
            for i in item:
                if i in alphabet:
                    # find letter from word in alphabet
                    position = alphabet.find(i)
                    # creates shuffles the letter to mach the key
                    if ask_encryption == "Encrypt":
                        new_pos = (position + key) % 26
                    # new decrypted letter is added to decrypted string
                    elif ask_encryption == "Decrypt":
                        new_pos = (position - key) % 26
                    new_character = alphabet[new_pos]
                    #new decrypted/decrypted letter is added to decrypted string
                    encrypted += new_character
                else:
                    encrypted += i
            encrypted += " "
        
        if ask_encryption == "Encrypt":
            print("Encrypted: ", encrypted)
        else:
            print("Decrypted: ", encrypted)
        print()
        print("Key: ", key)
        print()

    
    # if user does not have a key (no key)
    else:
        
        # keyless encryption


        correct_decrypt = False
        if ask_encryption == "Decrypt":
            key = 1
        else:
            key = random.randint(1, 25)
        
        while correct_decrypt is False:
            decrypted = ""
            for item in to_cipher:
                for i in item:
                    if i in alphabet:
                        #find letter from word in alphabet
                        position = alphabet.find(i)
                        #creates shuffles the letter to mach the key
                        new_pos = (position - key) % 26
                        new_character = alphabet[new_pos]
                        #new decrypted letter is added to decrypted string
                        decrypted += new_character
                    else:
                        decrypted += i
                decrypted += " "
            if ask_encryption == "Decrypt":
                print()            
                print("Attempted Decryption: '{}'".format(decrypted))

                correct_ans = "invalid choice"

                while correct_ans == "invalid choice":
                    print()
                    correct_ans = input("Is this decryption correct? ")

                    correct_ans = string_checker(correct_ans, yes_no)
                    
                    if correct_ans == "invalid_choice":
                        print("Please enter yes or no")
                        print()


                if correct_ans == "Yes":
                    print()
                    print("Decrypted: {}".format(decrypted))
                    print()
                    print("Key: {}".format(key))
                    correct_decrypt = True
                    return ""

                else:
                    key += 1
                    correct_decrypt = False
            else:
                print("Encryption: ", decrypted)
                print()
                print("Random Key: ", key)
                correct_decrypt = True
                return ""

# answer list
yes_no = [
    ["yes", "y"],
    ["no", "n"],
    ["xxx"]
]

#encrypt or decrypt ans list
encrypt_decrypt = [
    ["encrypt", "e"],
    ["decrypt", "d"],
    ["xxx"]
]

#lists go here
alphabet = ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
print()
print()

#asks user if they want instructions
instructions_valid = False

while not instructions_valid:
    ask_instructions = input("Do you want to see the instructions? ").lower()

    ask_instructions = string_checker(ask_instructions, yes_no)

    if ask_instructions == "invalid choice":
        print("Please enter yes or no (y or n)")
        print()
        instructions_valid = False
    # elif ask_instructions == "No" or "N":
    elif ask_instructions == "No":
        break
    # elif ask_instructions == "Yes" or "Y":
    elif ask_instructions == "Yes":
        instructions()
        break
    
print()

continue_game = True
while continue_game == True:
    ask_quit = cipher()
    if ask_quit == "xxx":
        break

print()
print("Thank you for using this program")
print()