# toys
# small 10$ red 2005
# medium 15$ blue 2018
# large 32$ yellow 2017


class toy:
    def __init__(self, size, price, color, completionyear):
        self.size = size
        self.price = price
        self.color = color
        self.completionyear = completionyear
    
    def detail(self):
        print(self.size, self.price, self.color, self.completionyear)

toy_a = toy('small', '10$', 'red', '2005')
toy_b = toy('medium', '15$', 'blue', '2018')
toy_c = toy('large', '32$', 'yellow', '2017')

toys = []
toys.append(toy_a)
toys.append(toy_b)
toys.append(toy_c)

for i in toys:
    i.detail()
