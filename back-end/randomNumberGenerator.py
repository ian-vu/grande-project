#make a script that loads random in future and other python libraries
import random
import sys

def randomNumberGenerator(min_number,max_number):
#min_number = int(input('Min: '))
#max_number = int(input('Max: '))

    min_number = int(float(min_number))
    max_number = int(float(max_number))

    if min_number > max_number:
        min_number,max_number = max_number,min_number
    
    rand_number = random.randint(min_number,max_number)
    
    return print(rand_number)

randomNumberGenerator(sys.argv[1], sys.argv[2])
