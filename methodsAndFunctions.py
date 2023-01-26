print('METHODS AND FUNCTIONS')
print('\nMETHODS')
#example
print('pop out item from list using pop method.')
list1 = [1,2,3,4]
print(list1.pop())
#get to know methods using help
print(f'help() functions get to know pop() method\n')
help(list1.pop)

print('\n\nFUNCTIONS:')  
#basic function example
print('Writing function definition...')
def print_hello():
    print('hello')
print('calling the function...')
print_hello()

print('#example 2...function with parameter')
def say_name(name = 'default'):
    print(f'hello {name}')
say_name('Advait')

print('example 3..using return statement..\nfucntion for sum of 2 numbers 30 and -65.876')
def add_num(num1,num2):
    return num1+num2
print(add_num(30, -65.876))

print('\nsFunctions With Logic:')
print('Example1.. check if the number is odd')
def check_odd(num1):
    return num1%2 != 0
print(f'20- {check_odd(20)},\t23- {check_odd(23)},\t-34- {check_odd(-34)}')

print('example 1.1...check if the any one number is odd in a given list')
def check_odd_list(num_list):
    #return list of odd numbers
    list_odd = []  
    for num in num_list:
        if num%2 != 0:
            list_odd.append(num)
        else:
            pass
    return list_odd
    return 'no odd number in the list'

print(f'[1,2,3,4,5]-\t{check_odd_list([1,2,3,4,5])}')
print(f'[2,4,6]-\t{check_odd_list([2,4,6])}')


print('example 1.2...return all odd in a given list')
def get_odd_list(num_list):
    #return list of odd numbers
    list_odd = []  
    for num in num_list:
        if num%2 != 0:
            list_odd.append(num)
        else:
            pass
    return list_odd 

print(f'[1,2,3,4,5]-\t{get_odd_list([1,2,3,4,5])}')
print(f'[2,4,6]-\t{get_odd_list([2,4,6])}')

print('\nTuple unpacking using functions:')
employee_hours = [('a',100),('b',300),('c',200.5),('d',300.1)] 
print('example 1... return employee of the month')
print(employee_hours)
def employee_of_the_month(work_hours_list):
    currentMaxHours = 0
    employeeOfTheMonth = ''

    for emp,hours in work_hours_list:
        if(hours > currentMaxHours):
            currentMaxHours = hours
            employeeOfTheMonth = emp
    
    return (currentMaxHours,employeeOfTheMonth)

hoursWorked,employeeName = employee_of_the_month(employee_hours)       #tuple unpacking
print(f'{employeeName} is the Employee of the Month with {hoursWorked} hrs')

print('\nInteractions between functions:')
print('exmplae 1 ...Three cup Monte(gess where is the ball out of three cups)')
#shuffle list
from random import shuffle

def shuffle_list(list):
    shuffle(list)
    return list

#get user guess as input
def user_guess():
    guess = ''

    while(True):
        guess = input("guess the ball position!!! ->> 0,1 or 2 ")
        if(guess in ['0','1','2']):
            break
        else:
            print("oops!!wrong input,select between 0,1 or 2")
    return int(guess)

#check if the guess is correct or not
def check__guess(cups,guess):
    if cups[guess] == 'O':
        print('Correct guess, you won !!')
    else:
        print(f'Wrong guess, you Lost!  \nthe ball was here : {cups}')

#final function to play the game
def three_cup_montee():
    
    #set ball position
    cup_list = ['O',' ',' ']
    
    print('Welcome!!\nThe game starts now')

    while(True):
        #shuffle it
        shuffled_cups = shuffle_list(cup_list)
        #user guess
        index = user_guess()
        #validate
        check__guess(cup_list, index)
        #check if users wants to continue
        inp = input("do you wish to play again ? y or n ")
        if(inp == 'y'):
            continue
        else:
            print('Bye!!')
            break

#game start
three_cup_montee()


