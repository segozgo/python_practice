from random import *

approved = 0

for ETA in range(1, 51):
    ETA = randint(5, 50)
    if ETA <= 15:
        print(f'[o]'+str(ETA))
        approved += 1
    else:
        print(f'[]'+str(ETA))

print(f'approved is',{approved})
