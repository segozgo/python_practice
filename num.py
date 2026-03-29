def determine(num, split):
    while int(num) - 1 > split:
        split += 1
        if int(num) % split == 0:
            return 'not prime number'
        elif int(num) - 1 == split:
            return 'prime number'
num = input('any_numb : ')

print(determine(num, 1))
