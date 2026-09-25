import random
import time

def rollDice(endNum,simNum):
    allRollList = []
    allRollCount = []
    allElapsedTimes = []

    for j in range(simNum):
        startTime = time.time()

        rollList = []
        rollCount = 0
        i = 0

        while  len(rollList) < endNum:
            rollCount += 1
            roll = random.randint(1,endNum)
            print(roll)

            if len(rollList) == endNum:
                continue

            if roll == i+1:
                rollList.append(roll)
                i += 1
                print(rollList)

            else:
                i=0
                del rollList[:]

        elapsedTime = time.time() - startTime

        print(f'Completed roll is {rollList}, it took {rollCount} rolls.')
        print(f'Elapsed time: {elapsedTime} seconds.')

        allRollList.append(rollList)
        allRollCount.append(rollCount)
        allElapsedTimes.append(elapsedTime)

        time.sleep(1)

    return allRollList, allRollCount, allElapsedTimes

allRollList, allRollCount, allElapsedTimes = rollDice(int(input("Enter the number of sides on the dice: ")), int(input("Enter the number of simulations: ")))
meanRollCount = sum(allRollCount)//len(allRollCount)
meanElapsedTime = sum(allElapsedTimes)/len(allElapsedTimes)

print(f'All completed rolls: {allRollList}, All roll counts: {allRollCount}')
print(f'Mean roll count: {meanRollCount}, Median roll count: {sorted(allRollCount)[len(allRollCount)//2]}')
print(f'Mean elapsed time: {meanElapsedTime} seconds, Median elapsed time: {sorted(allElapsedTimes)[len(allElapsedTimes)//2]} seconds')
