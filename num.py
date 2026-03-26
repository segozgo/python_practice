def determine(num, split):
    while int(num) - 1 > split:
        split += 1
        if int(num) % split == 0:
            print('not prime number')
            break
        elif int(num) - 1 == split:
            print('prime number')
            break

num = input('any_numb : ')

print(determine(num, 1))