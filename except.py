from random import *

class soldout(Exception):
    def __init__(self):
        super().__init__()

chicken = 10
waiting = 1
try:
    while(True):
        print(f'remain chicken : {chicken}')
        order = randint(-3, 15)
        if order > chicken:
            print(f'not enough chicken({order})')
            waiting += 1
        elif order < 0 or order > 10:
            print(f'invalid number({order})')
            waiting += 1
        else:
            print(f'[waiting{waiting}, chickens{order}]')
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise soldout

except soldout:
    print('soldout')