import numberSolver, letterSolver, sys

card_deck = []

# Handle the scenario in which no args are provided
if len(sys.argv) == 1:
    print("""
    No arguments provided.
    Please provide them in one of the following formats:

    NUMBER ROUND
    1 2 33 44 ...

    LETTER ROUND / CONUNDRUM
    A B C D E ...
    ABCDE ...
    """)
    raw_input = input(">>> ")
    card_deck = raw_input.split(" ")

    if len(card_deck) == 0:
        quit()

# Else puts the arguments into the array
else:
    card_deck = sys.argv[1:]

# Splits up the input if only one string provided
if len(card_deck) == 1:
    card_deck = list(card_deck[0])

# Number round
if card_deck[0].isdigit():
    print("    NUMBER ROUND")

    # Checks that all cards are numbers
    for card in card_deck:
        if not card.isdigit():
            print("\n   CARD SET CONTAINS NON-NUMBER CARDS")
            quit()
    
    # Solves the number round
    numberSolver.solve(card_deck)

# Letter round
else:
    print("    LETTER ROUND")

    # Checks that all cards are letters
    for card in card_deck:
        if card.isdigit():
            print("\n   CARD SET CONTAINS NUMBER CARDS")
            quit()
    
    # Solves the number round
    numberSolver.solve(card_deck)