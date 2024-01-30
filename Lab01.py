
runnerSpeed = int(input("How fast are you? (MPH)"))
mile5 = 5
mile10 = 10
mileHalfMarathon = 13.1
mileFullMarathon = 26.2


def mins(miles):
    hours = 0
    minutes = (miles / runnerSpeed) * 60
    while minutes >= 60:
        if minutes >= 60:
            hours += 1
            minutes -= 60

    print("To run " + str(miles) + " miles it would take you Hours: " + str(hours) + " Mins: " + str(minutes))


mins(mile5)
mins(mile10)
mins(mileHalfMarathon)
mins(mileFullMarathon)


