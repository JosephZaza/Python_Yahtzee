## This program simulates a simplified game of Yahtzee where a player
# plays against the computer.
# @author Joseph Kern

from random import randint

YAHTZEE_POINTS = 60
TWO_OF_KIND = 30
NUM_DIE_SIDES = 6
rollDice = "Y"
playerScore = 0
computerScore = 0

while (rollDice.upper() == "Y"):
    # Roll player dice
    die1 = randint(1, NUM_DIE_SIDES)
    die2 = randint(1, NUM_DIE_SIDES)
    die3 = randint(1, NUM_DIE_SIDES)
    
    # Display player's roll and results
    print(f"Player rolls: {die1}, {die2}, {die3}")
    if (die1 == die2 and die2 == die3):
        print(f"Yahtzee! (+{YAHTZEE_POINTS})")
        playerScore += YAHTZEE_POINTS
    elif (die1 == die2 or die2 == die3 or die1 == die3):
        print(f"Two of a Kind! (+{TWO_OF_KIND})")
        playerScore += TWO_OF_KIND
    else:
        chance = die1 + die2 + die3
        print(f"Chance! (+{chance})")
        playerScore += chance
    
    # Roll computer dice
    die1 = randint(1, NUM_DIE_SIDES)
    die2 = randint(1, NUM_DIE_SIDES)
    die3 = randint(1, NUM_DIE_SIDES)    
    
    # Display computer's roll and results
    print(f"Computer rolls: {die1}, {die2}, {die3}")
    if (die1 == die2 and die2 == die3):
        print(f"Yahtzee! (+{YAHTZEE_POINTS})")
        computerScore += YAHTZEE_POINTS
    elif (die1 == die2 or die2 == die3 or die1 == die3):
        print(f"Two of a Kind! (+{TWO_OF_KIND})")
        computerScore += TWO_OF_KIND
    else:
        chance = die1 + die2 + die3
        print(f"Chance! (+{chance})")
        computerScore += chance
    
    # Display current totals and ask for another roll    
    print("\n==============================")
    print(f"Player total points: {playerScore}")
    print(f"Computer total points: {computerScore}")
    print("==============================")
    rollDice = input("\nRoll again (Y or N)? ")
