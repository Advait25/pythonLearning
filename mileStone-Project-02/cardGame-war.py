import random

#suits
suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')

#rank
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Integer value for each rank
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



#CARD CLASS, it will have
##SUIT -> hearts,diamonds,spade,clubs 
##RANK -> jack ,king, ace etc., 
##VALUE -> an understandable integer value to the card

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


#test
clubsTwo = Card('Clubs', 'Two')
#print(clubsTwo)


#Deck class to ->
#insantiate deck - 25 cards
#shuffle the deck
#deal cards from the deck

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create card objects
                created_Card = Card(suit, rank)
                self.all_cards.append(created_Card)


    def shuffle_cards(self):
        random.shuffle(self.all_cards)

    
    def deal_one_card(self):
        return self.all_cards.pop()


#test
#new_deck = Deck()
#print(new_deck.all_cards[-1])
#new_deck.shuffle_cards()
#print(new_deck.all_cards[-1])
#print(new_deck.deal_one_card())
#print(len(new_deck.all_cards))


#player class to
#hold players current list of cards

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one_card(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            #for multiple cards
            self.all_cards.extend(new_cards)
        else:
            #for single cards
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards'


#test
#new_player = Player('Advait')
#new_player.add_cards(clubsTwo)
#new_player.add_cards(clubsTwo)
#new_player.add_cards(clubsTwo)
#new_player.add_cards(clubsTwo)
#print(f'{new_player} {new_player.all_cards[0]}')
#new_player.remove_one_card()
#print(f'{new_player} {new_player.all_cards[0]}')

#game logic
def start_game():
    #set players
    player_one = Player((input('Enter Player 1 name: ')))
    player_two = Player((input('Enter Player 2 name: ')))

    #shuffle deck
    new_deck = Deck()
    new_deck.shuffle_cards()

    #distribute carpopds
    for card in range(26):
        player_one.add_cards(new_deck.deal_one_card())
        player_two.add_cards(new_deck.deal_one_card())

    game_on = True
    round = 0

    #game starts
    while game_on:
        round += 1
        print(f'\nROUND :: {round}')

        #check for out of cards
        if len(player_one.all_cards) == 0:
            print(f'player {player_one.name} is out of cards, player {player_two.name} win round {round} and Game!!!!!!!')
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print(f'player {player_two.name} is out of cards, player {player_one.name} win round {round} and Game!!!!!!!')
            game_on = False
            break
        
        #start new round
        player_one_cards = []       #cards played on the table
        player_one_cards.append(player_one.remove_one_card())

        player_two_cards = []       #cards played on the table
        player_two_cards.append(player_two.remove_one_card())

        at_war = True
        print(f'{player_one.name} deals {player_one_cards[-1]}\t{player_two.name} deals {player_two_cards[-1]}')
        #assume at war from beginning
        while at_war:

            #player 1 wins the round
            if player_one_cards[-1].value > player_two_cards[-1].value:
                print(f'{player_one.name} wins')
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            #player 2 wins the round
            elif player_two_cards[-1].value > player_one_cards[-1].value:
                print(f'{player_two.name} wins')
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            #at war situation
            else:
                print(f'WAR situation in this round')

                #if either player has not enough cards to resolve war situation, here it is defined as 10 cards, it can vary
                if len(player_one.all_cards) < 10:
                    print(f'{player_one.name} is unable to declare the war, \n{player_two.name} wins the war and Game!!!!')
                    game_on = False
                    break
                elif len(player_two.all_cards) < 10:
                    print(f'{player_two.name} is unable to declare the war, \n{player_one.name} wins the war and Game!!!!')
                    game_on = False
                    break
                else:
                    for cards in range(3):
                        player_one_cards.append(player_one.remove_one_card())
                        player_two_cards.append(player_two.remove_one_card())

            
#user input to continue or not

def game_on():

    another_game = True

    #ask if want to try another game
    while another_game:
        start_game()
        response = input('do you want to try another round?,  enter "Y,y,N,n: ').lower()
        if response == 'n':
            another_game = False
            print('Bye!! :)')
            break
        else:
            print('Sure, here you go')
            continue



#gameon
game_on()


