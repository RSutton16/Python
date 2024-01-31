balls = 0
strikes = 0
outs = 0
innings = 1
first = second = third = False
playerRuns = 0
aiRuns = 0

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
    if innings < 9:
        innings += 1
        outs = 0

def out():
    global outs
    if outs > 1:
        outs = 0
        inning()
    else:
        outs+=1
    resetCount()

def moveRunner(amount):
    global first, second, third, playerRuns, aiRuns
    if amount == 0:
        if first and second and third:
            aiRuns +=1
        elif first and second:
            third = True
        elif first:
            second = True
        first = True
    if amount == 1:
        if third:
            aiRuns +=1
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

input2 = ''
while input2 != 'q':
    input2 = input("What would you like to do ?")
    if input2 == 's':
        changeCount('strike')
    if input2 == 'b':
        changeCount('ball')
    if input2 == 'o':
        changeCount('flyout')
    if input2 == 'o':
        changeCount('groundout')
    if input2 == 'f':
        changeCount('foulball')

    if input2 == '0':
        moveRunner(0)
    if input2 == '1':
        moveRunner(1)
    if input2 == '2':
        moveRunner(2)
    if input2 == '3':
        moveRunner(3)
    if input2 == '4':
        moveRunner(4)



    printStats()


