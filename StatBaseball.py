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
    if innings < 8:
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
        if first and second and third:
            aiRuns +=2
            second = False
        elif first and second:
            aiRuns +=1
            third = True
        elif first:
            third = True
        first = True
    if amount == 2:
        if first and second and third:
            aiRuns +=2
        elif first and second:
            aiRuns +=1
            third = True
        elif first:
            third = True
        first = False
        second = True
    if amount == 3:
        if first and second and third:
            aiRuns +=3
        elif first and second:
            aiRuns +=2
        elif first:            
            aiRuns +=1

        first = False
        second = False
        third = True
    if amount == 3:
        if first and second and third:
            aiRuns +=4
        elif first and second:
            aiRuns +=3
        elif first:            
            aiRuns +=2
        else:
            aiRuns +=1
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
    if result == "foulball":
        if strike < 2:
            strike += 1



printStats()
