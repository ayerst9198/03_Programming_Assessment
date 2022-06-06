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
alphabet = convert("abcdefghijklmnopqrstuvwxyz")
print(alphabet)
key = num_check("What is your key? ", int, "Please enter a whole number")

to_encrypt_list = convert(input("What would you like to encrypt?: "))

print()
print("your key:", key)
print("To encrypt", to_encrypt_list)


