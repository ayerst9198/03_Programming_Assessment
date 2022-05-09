# functions go here

# yes no checker pulled from frc
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please input yes / no")
            print()

# main routin

#loop for testing
while 1 == 1:
    yesno = yes_no("Would you like to read the instructions? ")
    print()
    if yesno == "yes":
        print("instructions go here")
        print("program continues")
    else:
        print("program continues")
    print()