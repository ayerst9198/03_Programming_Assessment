# num checker
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

# loop for testing
while 1 == 1:
    key = num_check("Please enter a whole number key to encrypt with. ", int, "Please enter an integer", "xxx")
    if key == "xxx":
        print("exit code")
        print()
    else:
        print("Your key is ", key)
        print()