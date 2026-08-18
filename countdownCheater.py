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


print("CARDS: " + str(card_deck))