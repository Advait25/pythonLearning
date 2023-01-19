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
my_list[2] = 'three'    #mutable
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

nestedList = [0,4,3,5,[-1,-2,-3]] #nested list
print(f'nested list {nestedList}')
print(f'retrive element from nested list {nestedList[-1][1]}')  #grabbing element from last emelement which is another list)



#Dictionary
print('\n\n\n\nDICTIONARY')
my_dict = {'apple': 2.99,'orange':3,'banana': 5} #sample list1
print(my_dict)
print(f"orange price : {my_dict['orange']}")      #grabbing dict element
my_dict2 = {'a': 299,'c':my_dict,'b':[-1,4,9,0]}   #sample2
print(my_dict2)
print(f"b = {my_dict2['b']}")                       #list inside dictonary
print(f"blist element at 'b' = {my_dict2['b'][2]}")                    #list element inside dictonary
print(f"apples = {my_dict2['c']['apple']}")         #dictionary inside dictionary
my_dict['pineapple'] = 10               # add new element
print(my_dict)
my_dict['apple'] = 3.99                 # update an existing element
print(my_dict)
del my_dict['banana']                   #remove a particular pair
print(f'post deletion banana my dict -> {my_dict}')
print(f'all keys of my_dict2 -> {my_dict2.keys()}')                  #get all keys
print(f'all values of my_dict2 -> {my_dict2.values()}')                  #get all values
print(f'all key-value pairs of my_dict2 -> {my_dict2.items()}')                  #get all key-value pairs
my_dict.clear()                                #remove all pairs
print(f'post deletion of all pairs my dict -> {my_dict}')



print('\n\n\nTUPLES')
t1 = ('a','b',3)        #sample tuple
print(type(t1))       #check type of t1
print(t1)
print(f'tuple t1 length -> {len(t1)}')          #getting tuple length
print(f'get element at index 0 -> {t1[0]}')         #getting tuple elements
t2 = (1,2,3,4,4,5,1,1,1,7,8,3)
print(f'slicing t2 -> {t2} \tat 3rd index by step 2 -> {t2[3::2]}')                                     #slicing
print(f'get element at index 0 -> {t2.count(3)}')                 #to get count of a particular element in tuple
print(f'get index of element -> {t2.index(3)}')                 #to get index of an element, 1st index will be returned in case of multiple appearances





