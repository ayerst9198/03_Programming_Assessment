from secrets import choice
from string import ascii_lowercase

# functions go here

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

# string checker
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




# answer list
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

#lists go here
alphabet = ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
alphabet_frequency = "etaionshrdlucmfwygpbvkqjxz"
print("ALPHABET", alphabet)

# loop for testing
while 1 == 1:
    decrypted = ""

    #asks user for text to decrypt
    to_decrypt = input("What would you like to decrypt?: ").split()
    #asks user if they have a key
    key_ans = "invalid choice"
    while key_ans == "invalid choice":
        #ask user if they have a key
        key_ans = input("Do you have a key?: ")
        #check that answer is valid
        key_ans = string_checker(key_ans, yes_no)

        if key_ans == "invalid choice":
            print("Please enter yes or no")
            print()

    if key_ans == "Yes":
        #asks user for a key for decryption
        key = num_check("What is your key? ", int, "Please enter a whole number")
        # finds position of letters in the input string, replacing
        # with letters higher up in the alphabet based on the
        # key. 
        # increase letter by key and add new letter to the decrypted text

        for item in to_decrypt:
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
    else:
        correct_decrypt = False
        key = 1
        while correct_decrypt is False:
            decrypted = ""
            for item in to_decrypt:
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
            
            print("Attempted Decryption: '{}'".format(decrypted))

            correct_ans = "invalid choice"

            while correct_ans == "invalid choice":
                correct_ans = input("Is this decryption correct? ")

                correct_ans = string_checker(correct_ans, yes_no)
                
                if correct_ans == "invalid_choice":
                    print("Please enter yes or no")
                    print()


            if correct_ans == "Yes":
                print("Decrypted: {}".format(decrypted))
                print("Key: {}".format(key))
                correct_decrypt = True
                break

            else:
                key += 1
                correct_decrypt = False

