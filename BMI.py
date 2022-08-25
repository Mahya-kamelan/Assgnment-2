weight = float(input('Enter your weight based on Kilograms: '))
height = float(input('Enter your height based on meters: '))

new_height = height * height
Bmi = weight / new_height
print(Bmi)
if (16 < Bmi < 18.5):
    print('Your body weight is deficit,.')
elif (18.5 <= Bmi < 24):
    print('You are ok')
elif (24 <= Bmi < 30):
    print('Your weight is over.')
elif (30 <= Bmi < 35):
    print('Youre obesity first degree.')
elif ( 35 <= Bmi < 40):
    print('Youre obesity second degree')
elif ( Bmi >= 40):
    print('Youre obesity third weight, Dude!')
