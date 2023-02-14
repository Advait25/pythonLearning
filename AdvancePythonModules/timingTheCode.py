print('TIMING THE CODE')

#create two functions doing similar thing but using different approach
#create a function which returns the list of strings for the given range of number

#1 using list comprehension
def func1(n):
    return [str(num) for num in range(n)]

#2 using map fuction
def func2(n):
    return list(map(str,range(n)))

print(func1(10))
print(func2(10))

#to see which solution is efficient, lets time the code

import time

for f in [func1,func2]:
    #step1 get time before running the function
    start = time.time()
    #step2 run the function
    f(1000)
    #step3 get the time after function is completed
    end = time.time()
    #elapsed time 
    print(f'elapsed time for {f} is = {end-start}')


#for smaller parameters the elapsed time is so small that it is almost equal to zero, so its hard to compare
#so we can use the timeit modules for such comparison
#timeit module run the code multiple time to understand its efficiency

import timeit 

statement1 = '''
func1(100)
'''

setup1 = '''
def func1(n):
    return [str(num) for num in range(n)]
'''

statement2 = '''
func2(100)
'''

setup2 = '''
def func2(n):
    return list(map(str,range(n)))
'''

print('func1 : ')
print(timeit.timeit(statement1,setup1,number = 100000))
print('func2 : ')
print(timeit.timeit(statement2,setup2,number = 100000))

