# your code goes here!
import time

def countdown(count):
    while count > 0:
        print(f"{count} SECOND(S)!")
        count -= 1
        if count == 0:
            print("HAPPY NEW YEAR!")

countdown(10)

def countdown_with_sleep(count):
    while count > 0:
        print(f"{count} SECOND(S)!")
        count -= 1    
        time.sleep(1)
        
        if count == 0:
            print("HAPPY NEW YEAR!")
countdown_with_sleep(10)