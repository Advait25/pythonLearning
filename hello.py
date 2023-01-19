print('hello world')

#exponential operations
exp = 2 ** 3
print(exp)

#exercise1 - get ans =100 in various ways
print(50+50,20*5,2 ** 2 * 25, 125 - 5 ** 2, 11*9+7%2)

#type()
print(type(exp))

#dynamic typing
exp = "dynamic typing"
print(exp)
print(type(exp))

#using escape sequence \n - new line, \t tab
print("dynamic \n \t string")

#string length
print(len(exp))

string = "python file"
#indexing
print(string[0])
#reverse indexing
print(string[-2])

#slicing
print(string[2:])
print(string[:4])
print(string[2:5])
print(string[::])
print(string[::2])
print(string[6:7:1])
#can be use to reverse string
print(string[::-1])

#string concatination
print(string[7:]+' '+'pointer')
print('z'*20)
print('3'+'2')

#imp string method
print(string.upper())
#to exectue upper function = string = string.upper() 

#print formatiing
#1).format
print('hello world {}'.format('inserted'))
print('using indexes - hello world {2} {3} {0} {1}'.format('beautiful','day','what','a'))
print('using same indexes - hello world {0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}'.format('a'))
print('using keys - hello world {w} {a} {b} {d}'.format(b='beautiful',d='day',w='what',a='a'))
##float formatting (value:width.precision f)
result = 20/98
print(result)
print('result is {0:10.4f}'.format(result))

#f-string method
name = 'Advait'
print(f'result is {result:10.4f}')
print(f'result is {result:10.4f} for {name}')


#Lists
print('\n\n\nLISTS')
my_list = [1,2,3,4]
my_list3 = ['Advait',25,99.99]
print(len(my_list))   #list length
print(my_list[2])     #indexing
print(my_list[-1])     #indexing
print(my_list[1:])    #slicing
my_list[2] = 'three'    #mutable string
my_list2 = ['a','b','c','zzz']
new_list =  my_list + my_list2 #concatination
print(new_list)
my_list.append(98.3)    #add new item to end of list
print('post append {}'.format(my_list))
print(new_list.pop())         #remove item at the end of the list by default i.e. index -1
print('post pop {}'.format(my_list))
print('pop 0 index {} refreshed list {}'.format(my_list.pop(0),my_list))  #pop item at specific index

a = ['a','x','g','k','c']
a.sort()
print('post sort a = {}'.format(a))
a.reverse()
print('post reverse a = {}'.format(a))
