from random import *

comment = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

wn = sample(comment, 4)
chicken = wn.pop()
shuffle(wn)
wn.sort()

print('chicken_wn :', chicken)
print('coffee_wn :', wn)


users = range(1, 21)

print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)

print('chicken : {}'.format(winners[0]))
print('coffee : {}'.format(winners[1:]))