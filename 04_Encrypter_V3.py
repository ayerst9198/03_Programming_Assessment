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

#lists go here
alphabet = ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
print("ALPHABET", alphabet)

# loop for testing
while 1 == 1:
    encrypted = ""
    #asks user for a key for encryption
    key = num_check("What is your key? ", int, "Please enter a whole number")
    #asks user for text to encrypt
    output = " "
    to_encrypt = input("What would you like to encrypt?: ").split()
    print(to_encrypt)
    print(output.join(to_encrypt))

# finds position of letters in the input string, replacing
# with letters higher up in the alphabet based on the
# key. 
    print()
    # change any numbers in list from string to integers
    for i in range(0, len(to_encrypt)):
        try:
            to_encrypt[i] = int(to_encrypt[i])
        except ValueError:
            continue
    #print list for testing
    print(to_encrypt)
    # increase letter by key and add new letter to the encrypted text
    for item in to_encrypt:
        for i in item:
            position = alphabet.find(i)
            new_pos = (position + key) % 26
            new_character = alphabet[new_pos]
            encrypted += new_character
            print(encrypted)

    print("encrypted =", encrypted)
    print()

    

