print('Exception Handling')
print('Example1 ->  adding int and str i.e. user input, + opening a file in read mode')

def addition(num1,num2):
    print(f'addition is > {num1+num2}')

try:

    num1 = 10
    #num2 = input('enter second number:')
    #addition(num1, num2)
    print('opening file..')
    f = open('sample.txt','r')
    f.write('some text')
except TypeError:
    print('looks like the 2nd number is not an integer')
except OSError:
    print('looks like the file is in read only mode, writing not allowed')
except :
    print('all other exceptions')
else :
    print('done!!')
finally :
    print('"finally" always runs')



print('\nExample 2..ask user for an integer')

def asking_for_integer():
    while True:
        try:
            num1 = int(input("please enter a number:"))
        except:
            print('not a number!!')
            continue
        else:
            print('Thank you!')
            break
        finally:
            print('I always run ')

asking_for_integer()