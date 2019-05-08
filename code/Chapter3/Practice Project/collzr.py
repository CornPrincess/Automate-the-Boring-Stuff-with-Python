# This is chapter3 project

def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    else:
        value = 3 * number + 1
        print(value)
        return value

print('Enter number:')
try :
    number = int(input())
except:
    print('Error: Please input the integer number.')
    
while True:
    if number != 1:
        number = collatz(number)
    else:
        break
