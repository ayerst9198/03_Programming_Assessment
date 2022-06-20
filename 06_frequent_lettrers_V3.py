import time
import sys

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

frequencies = {} 
  

test_word = input("Please enter text to be sorted: ").lower()

test_word = test_word.replace(" ", "")
print(test_word)


for char in test_word: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1

# Show Output
dict(sorted(frequencies.items(), key=lambda item: item[1]))
{0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
print ("Per char frequency in the test word is :\n {}".format(str(frequencies)))

