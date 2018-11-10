import math 
import random

stake = 100
win = 200
numCards= 53
maxIters = 10

# black is 0
# red is 1 
# joker is -1

def game():
    cards = list()
    numBlacks = 0
    numReds= 0
    isJoker = 0 
    moneyLoss = 0
    moneyWin = 0
    score = 0

    index = 0
    while(index < numCards):
        if(index < 26):
            cards.append(0)
        elif((index >= 26) and (index < 52)):
            cards.append(1)
        elif(index == 52):
            cards.append(-1)
        index = index +1 
    random.shuffle(cards)

    for index in range(len(cards)):
    # probability of red being is atleast 70%
        if ( numBlacks < numReds+ 20):
            if(cards[index]== 1):
                numReds = numReds + 1
            elif(cards[index]== 0):
                numBlacks = numBlacks +1
            elif(cards[index]== -1):
                isJoker = 1
        elif (numBlacks >= numReds +20 ):
            guessRed  = 1
            if (cards[index] == guessRed):
                moneyWin = moneyWin + win
            else:
                moneyLoss = moneyLoss + stake
    score = moneyWin - moneyLoss
    return score
    
def run():
    iter = 1
    numGains = 0
    while (iter <= maxIters):
        score = game()
        if (score >= 0):
            numGains = numGains +1
        print("Iteration " + str(iter) +": The total gain of the game is " + str(score))
        iter = iter +1
    print()
    print("According to this simulation, the number of games that resulted in a gain is " + str(numGains) + " games out of " + str(maxIters) + " games." )
run()