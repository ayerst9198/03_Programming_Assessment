import time
import sys
import re


# a function that checks the most frequent letter in a string
def split(word):
    return [char for char in word]


def delay_print(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()   


def frequent_letter(text):
    delay_print(text, 0.15)

frequency_dict = {}

test_word = "This is a test to find that the most frequent letter is T in this sentence".lower().strip()

print(test_word)

test_word = test_word.replace(" ", "")
print(test_word)
test_word = re.sub(r"\s+", "", test_word, flags=re.UNICODE)




print(test_word)
test_list = split(test_word)
tested_list = sorted(test_list)
for item in tested_list:
    if item == " ":
        tested_list.remove(item)
frequent_letter(tested_list)

# for loop 

    # splits lists into each le