from random import *

user = list(range(1, 21))
shuffle(user)
winners = sample(user, 4)

print(f'chicken :',winners[0])
print(f'coffee :',winners[1:])
