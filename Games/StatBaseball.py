balls = strikes = outs = innings = playerRuns = aiRuns = 0
first = second = third = False


def newGame():
    global balls, strikes, outs, innings, first, second, third, playerRuns, aiRuns, inning
    balls = strikes = outs = playerRuns = aiRuns = 0
    inning = 0


def printStats():
    global balls, strikes, outs, innings, first, second, third, playerRuns, aiRuns

    print("\nCount " + str(balls) + "-" + str(strikes) + " Outs: " + str(outs) + " inning: " + str(innings))
    print("Player Score: " + str(playerRuns) + " | Ai Score: " + str(aiRuns))
    print("First: " + str(first) + " | Second: " + str(second) + " | Third: " + str(third) + "\n")


def resetCount():
    global balls, strikes
    balls = 0
    strikes = 0


def inning():
    global innings, outs
    if innings >= 9 and aiRuns != playerRuns:
        newGame()
    else:
        innings += 1
        outs = 0


def out():
    global outs
    if outs > 1:
        outs = 0
        inning()
    else:
        outs += 1
    resetCount()


def moveRunner(amount):
    global first, second, third, playerRuns, aiRuns
    '''
    0 = walk
    1 = single
    2 = double 
    3 = triple
    4 = homerun
    '''
    if amount == 0:
        if first and second and third:
            aiRuns += 1
        elif first and second:
            third = True
        elif first:
            second = True
        first = True
    if amount == 1:
        if third:
            aiRuns += 1
            third = False
        if second:
            aiRuns += 1
            second = False
        if first:
            third = True

        first = True
    if amount == 2:
        if third:
            aiRuns += 1
            third = False
        if second:
            aiRuns += 1
            second = False
        if first:
            third = True
            first = False

        second = True
    if amount == 3:
        if third:
            aiRuns += 1
            third = False
        if second:
            aiRuns += 1
            second = False
        if first:
            aiRuns += 1
            first = False

        third = True
    if amount == 4:
        if first:
            aiRuns += 1
        if second:
            aiRuns += 1
        if third:
            aiRuns += 1
        aiRuns += 1

        first = False
        second = False
        third = False


def changeCount(result):
    global strikes, balls
    if result == "strike":
        strikes += 1
        if strikes >= 3:
            out()
    if result == "ball":
        balls += 1
        if balls >= 4:
            balls = 0
            moveRunner(0)
    if result == "flyout":
        out()
    if result == "groundout":
        out()
    if result == "foulball":
        if strikes < 2:
            strikes += 1


'''
game test loop is just to test mechanics of the game
q = quit
s = throw a strike
b = throw a ball
o = make an out
f = hitter hits a foul ball
0 = walk
1 = single
2 = double
3 = triple
4 = homerun
'''


def gameTestLoop():
    testInput = ''
    while testInput != 'q':
        testInput = input("What would you like to do ?")
        if testInput == 's':
            changeCount('strike')
        if testInput == 'b':
            changeCount('ball')
        if testInput == 'o':
            changeCount('flyout')
        if testInput == 'o':
            changeCount('groundout')
        if testInput == 'f':
            changeCount('foulball')
        moveRunner(int(testInput))
        printStats()


gameTestLoop()
