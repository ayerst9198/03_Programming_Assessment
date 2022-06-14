import time
import sys

def delay_print(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()
    print()   
delay_print("this is a test to see how the text delay works. The time used is 1 letter every 0.025 seconds.", 0.025)