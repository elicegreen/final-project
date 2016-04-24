import war_game

print('Hi! Welcome to the card game war!')
enter = input('Press any key to begin')
print(' ')
deck = war_game.deckGenerator() 
playerCards, computerCards = war_game.cardDealer(deck)
print(' ')
winner = war_game.mainGame(playerCards, computerCards)
if winner == True:
    print('You won the game! Congradulations!!!')
else: print('I won! Better luck next time!')
