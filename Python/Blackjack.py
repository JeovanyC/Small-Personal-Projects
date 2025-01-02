import random, sys


HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = 'backside'


def main():

    print('''
Hello, dear friend. Want to play a little game? It's called "BrackJack", and
to spice things up, we are going to play with a "small" bet.

This are the rules:

 1. Try to get as close to 21 without going over;
 2. Kings [K], Queens [Q], and Jacks [J] are worth 10 points;
 3. Aces [{}] are worth 1 or 11 points;
 4. Cards 2 through 10 are worth their face value;
 5. In case of a tie, the bet is returned to the player;
 6. The dealer stops hitting at 17.

These are the available moves to be taken:

    a. Hit (H) to take another card;
    b. Stand (S) to stop taking cards;
    c. Double Down (D) to increase the bet and take another card;(
    
Reminder!:

Double Down is only possible on the fist move!

Be cauful when tanking this risk!

'''.format(chr(9824)))

    money = 5000
    while True:
        if money <= 0:
            print('''
You lost all your money!

Is good thing you weren't playing with real money.

Thanks for playing!
''')
            sys.exit()


        print("Money: ", money)

        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Bet: ", bet)

        while True:
            displayHand(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break
            
            move = getMove(playerHand, money - bet)
            
            if move == "D":
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:", bet)
            if move in ("H", "D"):
                newCard =  deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}.".format(rank, suit))
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ("S", "D"):
                break
            

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) <= 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHand(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press Enter to continue...")
                print("\n\n'")


        displayHand(playerHand, dealerHand, True)

        playerValue = getHandValue (playerHand)
        dealerValue = getHandValue (dealerHand)


        if dealerValue >21:
            print("Dealer busts! You win ${}!".format(bet))
            money += bet
        elif (playerValue > 21 or playerValue < dealerValue):
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print("You won!")
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you.")
        
        input("Press Enter to continue...")
        print("\n\n")



def getBet(maxBet):
    while True:
        print("How much you want to bet? (1 - {}, or QUIT)".format(maxBet))
        bet = input('> ').upper().strip()
        if bet == "QUIT":
            print("Thanks for playing")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHand(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print("Dealer:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("Dealer Hand: ???")
        displayCards([BACKSIDE] + dealerHand[1:])
    print("Player:", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0
    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    
    return value


def displayCards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += ' ___ ' 
        if card == BACKSIDE:
    
            rows[1] += "|## |" 
            rows[2] += "|###|" 
            rows[3] += "|_##|" 
        else:

            rank, suit = card
            rows[1] += "|{} |".format(rank.ljust(2))
            rows[2] += "| {} |".format(suit)
            rows[3] += "|_{}|".format(rank.rjust(2, "_"))

    for row in rows:
        print(row)


def getMove(playerHand, money):
    while True:
        moves = ["(H)it", "(S)tand"]
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move
    


if __name__ == "__main__":
    main()