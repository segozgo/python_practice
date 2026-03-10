def sta_weight(gender, height):
    if gender == 'male':
        print(f'your gender : male your height : {height}')
        return round(((height/100)**2*22), 2)
    elif gender == 'female':
        print(f'your gender : female your height : {height}')
        return round(((height/100)**2*21), 2)

gender = input('enter your gender')
height= int(input('enter your height'))
weight = sta_weight(gender, height)
print(f'your standard weight : {weight}')
