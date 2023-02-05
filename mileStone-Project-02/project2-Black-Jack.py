import random

#suits
suits = ('Clubs', 'Hearts', 'Spades', 'Diamonds')

#rank
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#Integer value for each rank
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


playing = True


#CADRS
class Cards:

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit

#DECK
class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #create Deck
                self.all_cards.append(Cards(rank,suit))

    def __str__(self):
        for card in self.all_cards:
            print(card)
        return 'These are the cards!!!'

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one_card(self):
        return self.all_cards.pop()

#test
#Deck = Deck()
#Deck.shuffle_deck()
#print(Deck)

#HAND
class Hand:

    def __init__(self):
        self.cards = [] #to track all cards
        self.value = 0   #to track total card value
        self.aces = 0    #to track number of aces

    def add_card(self,new_card):
        self.cards.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):
        #if total value > 21 and still an Ace is found then decrease value of ace to 1 i.e. reduce total value by 10
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


#test
#testplayer = Hand() 
#testplayer.add_card(Deck.deal_one_card())
#testplayer.adjust_for_aces()
#print(f'{testplayer.value},{testplayer.aces},{testplayer.cards[0]}')
#testplayer.add_card(Deck.deal_one_card())
#testplayer.adjust_for_aces()
#print(f'{testplayer.value},{testplayer.aces},{testplayer.cards[1]}')
#testplayer.add_card(Deck.deal_one_card())
#testplayer.adjust_for_aces()
#print(f'{testplayer.value},{testplayer.aces},{testplayer.cards[2]}')

#CHIPS

class Chips:

    def __init__(self,total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



#take bet

def take_bet(Chips):

    while True:
        try:
            Chips.bet = int(input('how many chips would you like to bet?'))
        except:
            print('please enter valid amount of chips')
        else:
            if Chips.total < Chips.bet:
                print(f'not enough chips availanle, you only have {Chips.total} chips')
            else:
                break


#hit

def hit(Deck,Hand):
    single_card = Deck.deal_one_card()
    Hand.add_card(single_card)
    Hand.adjust_for_aces()


#hit_or_stand

def hit_or_stand(Deck,Hand):
    global playing

    while True:
        inp = input('Hit or Stand? enter h or s please: ').lower()
        if inp[0] == 'h':
            hit(Deck, Hand)
        elif inp[0] == 's':
            print('Player Stands!!')
            playing = False
        else:
            print("i don't understand that input, please try again with h or s")
            continue

        break


#show some
def show_some(player, dealer):

    #dealer's one ccard will be hidden and other will be shown
    print("\nDealer's Cards: ")
    print('<First card is hidden>')
    print(f'Second card is : {dealer.cards[1]}')

    #all of players cards (2) will be shown
    print("\nPlayer's Cards: ")
    print('',*player.cards,sep = '\n')

#show some
def show_all(player, dealer):

    #all of delaers cards (2) will be shown
    print("\nDealer's Cards: ")
    print('',*dealer.cards,sep = '\n')
    print(f"Dealer's Total - {dealer.value}")

    #all of players cards (2) will be shown
    print("\nPlayer's Cards: ")
    print('',*player.cards,sep = '\n')
    print(f"Player's Total - {player.value}")



#player busts
def player_busts(player,dealer,Chips):
    print('player busted!!!')
    Chips.lose_bet()

#player wins
def player_wins(player,dealer,Chips):
    print('player wins!!!')
    Chips.win_bet()

#dealer busts
def dealer_busts(player,dealer,Chips):
    print('dealer busted!!!')
    Chips.lose_bet()

#dealer wins
def dealer_wins(player,dealer,Chips):
    print('delaer wins!!!')
    Chips.win_bet()

#push
def push(player,dealer):
    print('Tie!!! PUSH')




#gameon
while True:

    #opening statement
    print('Welcome to Black-Jack')
    #creating plus shuffling the deck and dealing the cards
    deck = Deck()
    deck.shuffle_deck()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one_card())
    player_hand.add_card(deck.deal_one_card())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one_card())
    dealer_hand.add_card(deck.deal_one_card())

    #set player chips
    player_chips = Chips()

    #prompt the player's for their bet
    take_bet(player_chips)

    #show cards, at the start show some cards and not all
    show_some(player_hand, dealer_hand)

    while playing:               #global variable

        #prompt the player for hit or stand
        hit_or_stand(deck, player_hand)

        #show cards, but one dealer card is hidden
        show_some(player_hand, dealer_hand)

        #if player hand > 21, player bust and break
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    #if if player hasn't busted, play dealer hand until dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        #show all cards 
        show_all(player_hand, dealer_hand)

        #run different winning situation
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    #inform player of their chips total
    print(f'player chips total : {player_chips.total}')    

    #ask to play again
    new_game = input('wanna play again? , enter between Y,y,N,n : ').lower()
    if new_game[0] == 'y':
        playing = True
        continue
    else:
        print('bye!!!!')
        break



