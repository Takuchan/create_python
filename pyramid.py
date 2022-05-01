import random

first_step = 0

print ("What number do you like?")
setNumber = int(input())
space = 0

for row in range(setNumber):
    
    randomInt = random.randint(0,9)
    for horizontaL in range(setNumber - row):
        print("もやし",end="")
        
    print("")
    
    
