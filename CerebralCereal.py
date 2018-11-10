import math 
import random

numPhilosophers = 66
maxIters = 10

def philosophers():  
    philosophers = list()
    for index in range(numPhilosophers):
        philosophers.append(index)
    return philosophers

def johanMethod(philosophers):
    johanAverage = numPhilosophers * math.log(numPhilosophers)
    error = 0
    numBoxes = int (johanAverage)
    philosopherPic = list()
    philosophersFound = 0

    for index in range( numBoxes):
        toAppend = random.randint(0,65)
        philosopherPic.append(toAppend)
  
    for index in range(numBoxes):
        philosopher = philosopherPic[index]
        if ( philosophers[int(philosopher)] == philosopher ):
            philosophers[int(philosopher)] = 100

    for index in range(numPhilosophers):
        if (philosophers[index] == 100):
            philosophersFound = philosophersFound + 1
    
    return philosophersFound

def henrikMethod(philosophers):
    henrikAverage = numPhilosophers * math.e
    error = 0
    numBoxes = int (henrikAverage)
    philosopherPic = list()
    philosophersFound = 0

    for index in range( numBoxes):
        toAppend = random.randint(0,65)
        philosopherPic.append(toAppend)
    
    for index in range(numBoxes):
        philosopher = philosopherPic[index]
        if ( philosophers[int(philosopher)] == philosopher ):
            philosophers[int(philosopher)] = 100

    for index in range(numPhilosophers):
        if (philosophers[index] == 100):
            philosophersFound = philosophersFound + 1
    
    return philosophersFound

def run():
    iters = 1
    while ( iters <= maxIters):
        print("Iteration " + str(iters) + ": ")
        philosophersList = philosophers()
        johanAccuracy = johanMethod(philosophersList)
        henrikAccuracy = henrikMethod(philosophersList)
        print("Number of distinct philosphers using Johan average is: " + str(johanAccuracy))
        print("Number of distinct philosphers using Henrik average is: " + str(henrikAccuracy))
        print()
        iters = iters +1 
run()