import math 
import random

def simulation():
    numStudents = 222
    attendance = list()

    index = 0
    while(index <numStudents):
        if ( index < 99):
            attendance.append(1)
        elif(index >=99 and index < numStudents):
            attendance.append(2)
        index = index +1
    random.shuffle(attendance)
    
    firstHour = 99
    secondHour = 123
    Popularity = secondHour - firstHour
    SL1 = secondHour - (0.99 * firstHour)
    SL2 = secondHour - (0.95 * firstHour)
    err1 = SL1 - Popularity
    err2 = SL2 - Popularity

    print("Null hypothesis: Second hour si more popular than the first hour.")
    print("Popularity of second hour is: " + str(Popularity) + " students.")
    print(" With 99%: " + str(SL1))
    print(" With 95%: " + str(SL2))
    if ( err1 > err2):
        print("The difference is on 95% significance level.")
    else:
        print("The difference is on 99% significance level.")

simulation()