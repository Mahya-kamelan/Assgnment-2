number = old_number= int(input('Enter your number: '))
while True:
    if number < 0:
        print('Please give me a positive number.')
        number = old_number= int(input('Enter your number: '))
    else:
        break

rev = 0
while number != 0:
    if number >= 0:
        x = number % 10
        rev  = (rev*10) + x
        number = int(number / 10)
print(rev)
if (rev == old_number):
    print('The number is equal.')
elif (rev != old_number):
    print('The number is not equal.')
