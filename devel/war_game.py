import random

#creates and shuffles a full deck of cards; returns it as a list
def deckGenerator():
    print('Getting a full deck of cards for us.........')
    allCards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K', 'A']*4
    return allCards

#divides deck of cards evenly between the player and computer; returns them as two lists
def cardDealer(deck):
    print('Shuffling the deck.........')
    random.shuffle(deck)
    print('Dealing the cards..........')
    playerCards = deck[:26]
    computerCards = deck[26:]
    return(playerCards, computerCards)

    
def mainGame(playerCards, computerCards):

    #assigning values to card reference in a dictionary so to compare numaric values of careds
    dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    
    playerName = input('What is your name?  ')

    #loop runs so long as both player and computer have cards left
    while playerCards and computerCards:
        print(' ')
        print(playerName + ', ' + 'you have ', len(playerCards), ' cards')
        print(' ')
        print('I have ', len(computerCards), ' cards')
        print(' ')
        key = input('Press any key to flip your card')
        playerHand = playerCards[0]
        del playerCards[0] #removes the flipped card from the player's deck (deletes first value in the player list)
        computerHand = computerCards[0]
        del computerCards[0] #removes theflipped card from the computer's deck (deletes first value in the computer list) 
        print(' ')
        print(playerName + ', ' + 'your card is........')
        print(playerHand)
        print('My card is........')
        print(computerHand)

        #compares between flipped cards using the dictionary as ref and adds cards to the end of either the player
        #or the computer lists (according to compared value)
        if dict.get(playerHand)>dict.get(computerHand):
            print(' ')
            print('You get the cards!')
            playerCards.append(playerHand)
            playerCards.append(computerHand)
        elif dict.get(playerHand)<dict.get(computerHand):
            print(' ')
            print('I get the cards!')
            computerCards.append(playerHand)
            computerCards.append(computerHand)
        #enters this condition in case of 'war' (if both cards that were flipped are the same)
        else:
            tempPlayerPile = []
            tempComputerPile = []
            playerNewHand = 0
            computerNewHand = 0
            
            war = True #set to run automatically the first time; will only run again if double or triple war
            while war == True:
                print(' ')
                print('It is a tie! War time!!!')
                while playerNewHand == 0:
                    tempPlayerPile.append(playerHand) #adds the flipped card as the first card in the player war cared pile
                    tempComputerPile.append(computerHand) #adds the flipped card as the first card in the computer war cared pile         
                    playerNewHand = 1 #assures that this loop doesn't run again for war that is second or more times in a row

                print(' ')
                key = input('Press any key to place three cards on top of your flipped card')
                tempPlayerPile.extend(playerCards[0:3])#adds the three next cards from player cards to player war card pile
                print(' ')
                print('I am placing three cards on top of my flipped card...')
                tempComputerPile.extend(computerCards[0:3])#adds the three next cards from computer cards to computer war card pile

                del playerCards[0:3] #removes four first cards from player's deck (as they have been placed/stored in player war card pile)
                del computerCards[0:3] #removes four first cards from computer's deck (as they have been placed/stored in computer war card pile)

                print(' ')
                print(' ')
                key = input('Press any key to flip the top card in your war pile')
                playerNewHand = tempPlayerPile[-1] #stores last card in player war pile list for value comparison
                print(' ')
                print(' ')
                print(' ')
                print(playerName + ', ' + 'your card is........')
                print(playerNewHand)
                print(' ')
                print('I am flipping the top card in my war pile...')
                computerNewHand = tempComputerPile[-1] #stores last card in computer war pile list for value comparison
                print(' ')
                print('My card is........')
                print(computerNewHand)
                #compares between the player's and the computer's last cards placed in war piles ("flipped cards")
                #will add both war piles (all values in both lists) to either the player or computer cards according to value comparison and exit war [while] loop
                #if both cards flipped are the same again, will run loop again (but without appending currently flipped cards to war piles as they are already a part of the piles)
                if dict.get(playerNewHand)>dict.get(computerNewHand):
                    print(' ')
                    print('You get the cards!')
                    playerCards.extend(tempPlayerPile) 
                    playerCards.extend(tempComputerPile) #extend method adds all values of one list to another
                    war = False
                elif dict.get(playerNewHand)<dict.get(computerNewHand):
                    print(' ')
                    print('I get the cards!')
                    computerCards.extend(tempPlayerPile) #adds all four drawn cards to the coputer's deck
                    computerCards.extend(tempComputerPile) #adds all four drawn cards to the coputer's deck
                    war = False
                else:
                    war = True 

        print(' ')

    #returns true if player wins (computer is left with no cards) and false if computer wins (player left with no cards)
    if not computerCards:
        return True
    else:
        return False
