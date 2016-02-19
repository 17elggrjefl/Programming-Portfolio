from random import randint

def roll_again():
    yn = raw_input("Do you want to roll? y/n ")
    while yn.lower() != "y" and yn.lower() != "n":
        yn = raw_input("Please just use y or n, nothing else. y/n ")
    else:
        if yn.lower() == "y":
            return True
        elif yn.lower() == "n":
            return False
        else:
            raise IOError("Misunderstood statement")
    

player = [["Player One", 0], ["Player Two", 0]]

while player[0][1] < 100 and player[1][1] < 100:
    for play in player:
        turnScore = 0
        die = randint(1, 6)
        print play[0] + ":"
        rollAgain = roll_again()
        while die != 1 and rollAgain:
            print die
            turnScore += die
            die = randint(1, 6)
            print play[0]
            rollAgain = roll_again()
        else:
            if die == 1 and rollAgain:
                print "You rolled a 1."
                print "Your Score: " + str(play[1])
            else:
                play[1] += turnScore
                print "Your Score: " + str(play[1])