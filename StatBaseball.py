class main:
    balls = 0
    strikes = 0
    outs = 0
    innings = 0
    pitchResult = None

    def resetCount():
        balls = 0
        strikes = 0

    def inning():
        if innings < 8:
            innings += 1
            outs = 0

    def out():
        if outs > 1:
            outs = 0
            inning()
        else:
            outs+=1
        resetCount()

    def moveRunner():
        pass
    

    def changeCount(pitchResult):
        if pitchResult == "strike":
            strikes += 1
            if strikes >= 3:
                out()
        if pitchResult == "ball":
            balls += 1
            if balls >= 4:
                moveRunner()
        if pitchResult == "flyout":
            out()
        if pitchResult == "foulball":
            if strike < 2:
                strike += 1

    def printStats():
        print("\nCount " + str(balls) + "-" + str(strikes) + " Outs: " + str(outs) + " inning: " + str(innings) + "\n")