from random import *

counter = 1
approved = 0

while counter <= 50:
    ETA = randint(5,50)
    if ETA <= 15:
        print(f'[o]'+str(ETA))
        approved += 1
    else:
        print(f'[]'+str(ETA))
    counter += 1

print(f'approved is',{approved})