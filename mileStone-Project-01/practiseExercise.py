print('Display Information')
r1 = [' ','|',' ','|',' ']
r2 = ['- - - - -']
r3 = [' ','|',' ','|',' ']
r4 = ['- - - - -']
r5 = [' ','|',' ','|',' ']

def display_info(*args):
    for i in args:
        #print(list(map(lambda x:print(x),i)))
        print(*i)

#display_info(r1,r2,r3,r4,r5)


print('\nUser Input')
#index_position =  int(input("enter an index position : "))
#print(index_position)


print('\nValidate user input')

def use_input():

    input_choice = False
    acceptable_input_range = range(0,10)
    inrange = False

    while input_choice == False or inrange == False:
        input_choice = input("Enter choice between (0-10): ")

        if input_choice.replace('-','').isdigit() == False:
            print("The input is not a digit")
        
        if input_choice.replace('-','').isdigit() == True:
            if int(input_choice) in acceptable_input_range :
                inrange = True
            elif int(input_choice) < 0:
                print("input cannot be negative")
                inrange = False
            else:
                print("The input is out of range (0-10)")
                inrange = False

    return input_choice

#index_position = use_input()
#print(index_position)





def win_check():
    #check for all combination to have same marker value
    combination_list = [[7,8,9],[4,5,6],[1,2,3],[7,4,1],[8,5,2],[9,6,3],[7,5,3],[9,5,1]]
    print(len(combination_list))
    
win_check()