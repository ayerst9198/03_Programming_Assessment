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


def convert(lst):
    return list(lst)

#lists go here
alphabet = ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
print("ALPHABET", alphabet)

encrypted = ""
# loop for testing
while 1 == 1:
        
    #asks user for a key for encryption
    key = num_check("What is your key? ", int, "Please enter a whole number")

    #asks user for text to encrypt
    to_encrypt = input("What would you like to encrypt?: ")

    print()
    for i in to_encrypt:
        position = alphabet.find(i)
        new_pos = (position + key) % 26
        new_character = alphabet[new_pos]
        encrypted += new_character
    
    else:
        encrypted += i
    print("encrypted =", encrypted)
    print()
    

