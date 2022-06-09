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
alphabet_frequency = ascii_lowercase # "etaionsrdlucmfwygpbvkqjxsz"
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
                    position = alphabet.find(i)
                    new_pos = (position - key) % 26
                    new_character = alphabet[new_pos]
                    decrypted += new_character
                else:
                    decrypted += i
            decrypted += " "
    else:
        # insert decryption without key
        for item in to_decrypt:
            for i in item:  
                if i in alphabet_frequency:
                    frequent_letter = max(to_decrypt)
                    position = alphabet_frequency.find(frequent_letter)
                    new_pos = (position + 1) % 26
                    new_character = alphabet_frequency[new_pos]
                    decrypted += new_character
                    position += 1
                else:
                    decrypted += frequent_letter
            decrypted += " "
    print("decrypted = ", decrypted)
    print()

    

