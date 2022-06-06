import random
# functions go here

def word_check(question, error):
    valid = False
    while not valid:

        response = input(question)

        # checks word length
        if len(response) < 2:
            print(error)
            continue
        else:
            return response


key_word = word_check("What is the product? ", "Please enter a product name")
word_list = list(key_word)
comp_list = word_list
print(word_list)

while 1 == 1:
    token = random.choice(word_list)
    print(token)

    if token in comp_list:
        comp_list.remove(token)
    word_list = list(key_word)
    
    if comp_list == []:
        break
    
    play = input("")
print("congratulations")