import string

#display my items
def display_items(*args):
    #to display key during user input
    if len(args) > 1:
        i=iter(string.ascii_lowercase)
        for key in args[0]:
            print(f'{next(i)}. {key}')
    #display all items and there values
    else:
        for key,value in args[0].items():
            print(f'{key} : {value}')


#get user's replaccement choice
def user_replacemen_choice(my_items):
    #default choice is wrong
    choice = False

    #acceptable choice
    acceptable_choice = ['a','b','c','d']

    while choice not in acceptable_choice:

        print('\nSelect the letter of choice infron of the item you want to replace')
        display_items(my_items,True)
        choice = input("Your choice : ")

        if choice not in acceptable_choice:
            print('\nSorry, invalid choice! please enter a valid choice') 
    

    #maping acceptable choice with items name
    keys = tuple(my_items.keys())
    my_keys = keys
    (a,b,c,d) = my_keys
    #get the key

    if(choice == 'a'):
        return a
    elif(choice == 'b'):
        return b
    elif(choice == 'c'):
        return c
    else:
        return d


#get the value that user wants to replacae with
def get_user_replacement_value(my_items,key):
    #get user input
    replacement =  input(f"\nplease enter the value that you want to replace it with: ")
    #replace the value
    my_items[key] = replacement

    return my_items

#def start game
def start_game():
    print('Welcome to replacement game!!!\n')
    #initiate the items
    my_items = {'food': 'apple','laptop':'asus','football team':'RealMadrid', 'F1 Driver':'Lewis_hamilton'}
    
    #to check if users wants to keep playing
    continue_playing = ''

    while continue_playing != 'n':
        #display
        display_items(my_items)

        #get item choice user wants to replace
        item = user_replacemen_choice(my_items)

        #get the user's replacement value
        my_items = get_user_replacement_value(my_items, item)

        #display updated list
        print('\nUpdated Successfully!')
        display_items(my_items)

        #set continue_playing = '' for next iteration to continue
        continue_playing = ''

        while continue_playing not in ['y','n']:
            
            continue_playing = input('\nWant to continue playing? enter Y,y,N,n: ').lower()
            
            if continue_playing not in ['y','n']:
                print('Invalid choice')



#start the game
start_game()



