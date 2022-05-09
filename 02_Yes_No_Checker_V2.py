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
# looped for testing
while 1 == 1:
    
    # define variable
    ans = "invalid choice"
    while ans == "invalid choice":

        # ask user hte question
        ans = input("Did Toby legit beat Ryan in cr random deck 1v1? ")

        # checks if answer is valid
        ans = string_checker(ans, yes_no)

        # loops if invalid option
        if ans == "invalid choice":
            print("Please enter yes or no")

    # prints our responbse based on answer
    if ans == "Yes":
        print("correct")
        print()
    else:
        print("wrong")
        print()

