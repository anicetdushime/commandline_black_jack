import random
import math

CARDS = []
DEALER_HAND = []
PLAYER_HAND = []

#constants to make it easier to distinguish who wins
PLAYER_WINS = 1
DEALER_WINS = 2
DRAW = 0

DONE = False  # tells if the game is over





"""
starts the game by asking the user when they want to start
"""
def main():
    print("---------------")
    print("WELCOME TO THE BLACK JACK GAME ....")
    choice_to_start = input("To start playing, enter 1")
    set_up_cards()
    if choice_to_start == "1":
        play_game()
        print("THANKS FOR PLAYING !! WELCOME BACK SOON...")


"""
sets up all cards in a list
"""
def set_up_cards():
    characters = ["2", "3", "4", "5", "6", "7", "8", "9", "A", "J", "K", "Q" ]
    for character in characters:
        for i in range(4):
            CARDS.append(character)

"""
Starts the game
Chooses the starting cards
Lets user take their turn
Lets dealer take their turn
checks the winner
"""
def play_game():

    deal_initial_cards()
    if DONE:
        return
    player_turn()
    if DONE:
        return
    dealer_turn()
    if DONE:
        return
    check_final_winner()

"""
Deals the first two cards to each player
"""
def deal_initial_cards():
    # get dealer cards, one face up, and add them to hand
    dealer_card1 = get_card()
    dealer_card2 = get_card()
    DEALER_HAND.append(dealer_card1)
    DEALER_HAND.append(dealer_card2)

    print("Dealer card 2 is a", dealer_card2, "with card value", get_card_value(dealer_card2))

    # get player cards and show both
    player_card1 = get_card()
    player_card2 = get_card()
    print("Player card 1 is a", player_card1, "with card value", get_card_value(player_card1))
    print("Player card 2 is a", player_card2, "with card value", get_card_value(player_card2))
    PLAYER_HAND.append(player_card1)
    PLAYER_HAND.append(player_card2)
    check_early_winner()

"""
dealer plays while under 17 points
"""
def dealer_turn():
    while calculate_hand(DEALER_HAND) < 17:
        dealer_card = get_card()
        if dealer_card == -1:
            check_final_winner()  # if you run out of cards by any chance, just compare cards at that point
        DEALER_HAND.append(dealer_card)
        print("The dealer hand is", DEALER_HAND)
        print("The dealer score is", calculate_hand(DEALER_HAND))
        check_early_winner()
        if DONE:
            return

"""
player chooses to hit or stand
"""
def player_turn():
    choice = input("Press 1 to hit, and 0 to stand... ")
    while True:
        if choice == "0":
            break
        if choice == "1":
            user_card = get_card()
            if user_card == -1:
                check_final_winner()  # if you run out of cards by any chance, just compare cards at that point
                return
            PLAYER_HAND.append(user_card)
            print("You picked a ", user_card, "of value", get_card_value(user_card))
            check_early_winner()
            if DONE:
                return
        if choice not in "01":
            print("Enter a valid option")
        choice = input("Press 1 to hit, and 0 to stand... ")



"""
@:param card to get value (str)
:return the value of a card passed (int)
"""
def get_card_value(card):
    if card == "A":
        return 1, 11 # a tuple of the two possibilities
    elif card in "KJQ":
        return 10
    else:
        return int(card)



"""
@:return string indicating what card is chosen from the deque
"""
def get_card():
    indices_max = len(CARDS)-1
    if indices_max == -1:
        # ran out of cards
        return -1
    #random.seed()
    index = random.randint(0, indices_max)
    card = CARDS[index]
    return card


"""
checks if someone has won in the middle of the game from being lucky (21)
or the opponent being unlucky(>21)
"""
def check_early_winner():
    dealer_points = calculate_hand(DEALER_HAND)
    player_points = calculate_hand(PLAYER_HAND)
    if dealer_points == 21 or player_points > 21:
        terminate(DEALER_WINS)
    if player_points == 21 or dealer_points > 21:
        terminate(PLAYER_WINS)



"""
calculates the best value of a hand
If there are A's present, it tries all different counts of the As to get the one that makes most
benefit
"""
def calculate_hand(hand):
    total_value = 0
    num_of_As = 0
    value_of_As = get_card_value('A')
    for card in hand:
        if card == 'A':
            num_of_As += 1
        else:
            total_value += get_card_value(card)
    if num_of_As == 0:
        return total_value  # No complications

    # when there are As
    values = [total_value]
    for i in range(num_of_As):
        temp_list_values = []
        while values:
            current = values.pop()
            temp_list_values.append(current + value_of_As[0])
            temp_list_values.append(current + value_of_As[1])
        values = temp_list_values

    final = -math.inf
    for val in values:
        if val == 21:
            return 21
        if val > 21:
            continue
        final = max(val, final) # gets highest value between 0 and 20
    return final


"""
Checks who is the final winner of the game at the end
"""
def check_final_winner():
    player_points = calculate_hand(PLAYER_HAND)
    dealer_points = calculate_hand(DEALER_HAND)
    if player_points > dealer_points:
        terminate(PLAYER_WINS)
    elif dealer_points > player_points:
        terminate(DEALER_WINS)
    else:
        terminate(DRAW)

"""
Prints final message and updates DONE variables so other functions know it is done
"""
def terminate(value):
    global DONE
    DONE = True
    name = ""

    print("--------------")
    print("We have ourselves a winner!!!!")
    if value == DEALER_WINS:
        name = "dealer"
        print(DEALER_HAND)
        print("Damn! Better luck next time")
    elif value == PLAYER_WINS:
        print(PLAYER_HAND)
        name = "you"
        print("Hurray!", name, "have won!!!")
    elif value == DRAW:
        print("So close! It's a draw!")



if __name__ == "__main__":
    main()
