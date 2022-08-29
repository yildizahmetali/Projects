#Guessing Game - by Ahmet Ali Yildiz

import random

prevcat = 0
prevdiff = 0


def main():
    print("Welcome to the guessing game!")

    gametype = getChoice()
    while gametype != 0:
        rnum = random.randint(1,100)
        print("I am thinking of a number between 1 and 100...")
        if gametype == 1:
            playHotCold(rnum)
        elif gametype == 2:
            playHighLow(rnum)
        else:
            print("I do not understand game type: " + str(gametype))

        gametype = getChoice()
        print()

    print("Thanks for playing!")

def playHotCold(rnum):
    gcount = 0
    playing = True
    while playing:
        guess = getGuess()
        gcount += 1
        if guess == 0:
            print("Sorry you did not guess my number " + str(rnum) + " in " + str(gcount-1) + " tries.")
            playing = False
        elif guess == rnum:
            print("You guessed my number in " + str(gcount) + " tries.")
            playing = False
        else:
            showHotCold(rnum,guess)
            playing = True


def playHighLow(rnum):
    gcount = 0
    playing = True
    while playing:
        guess = getGuess()
        gcount += 1
        if guess == 0:
            print("Sorry you did not guess my number " + str(rnum) + " in " + str(gcount-1) + " tries.")
            playing = False
        elif guess == rnum:
            print("You guessed my number in " + str(gcount) + " tries.")
            playing = False
        else:
            showHighLow(rnum,guess)
            playing = True

def showHotCold(rnum,guess):
    global prevcat, prevdiff
    category = 0
    diff = abs(rnum - guess)
    msg = ""
    if diff >= 60:
        category = 1
        msg = "cold"
    elif diff>= 30:
        category = 2
        msg = "warm"
    elif diff >= 16:
        category = 3
        msg = "very warm"
    else:
        category = 4
        msg = "HOT"
    #print("You are " + msg)
    if category == prevcat:
        if diff == prevdiff:
            msg += " (same degree)"
        elif diff > prevdiff:
            msg += " (getting colder)"
        else:
            msg += " (getting warmer)"

    print("Your guess is: " + msg)
    prevcat = category
    prevdiff = diff

def showHighLow(rnum,guess):
    category = 0
    diff = (rnum - guess)
    msg = ""
    if diff > 0:
        category = 1
        msg = "too low"
    elif diff < 0:
        category = 2
        msg = " too high"


def getChoice():
    goodVal = False
    while not goodVal:
        try:
            choice = int(input("Game Type: 1=Hot/Cold, 2=High/Low, 0=Quit: "))
            if choice < 0 or choice > 2:
                print("Unknown operation: 1-2 or 0 to quit only")
            else:
                goodVal = True
        except ValueError:
            print("Illegal input: integers between 0 and 2 only.")
    return choice

def getGuess():
    g = int(input("Your Guess? (1-100), 0=Quit: "))
    return g


if __name__ == "__main__":
    main()
