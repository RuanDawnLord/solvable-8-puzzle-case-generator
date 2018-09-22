import random

caseCount = 100
def solveable(tiles):
    sumInversed = 0
    for i in range(0, len(tiles)):
        if tiles[i]==0:
            continue
        sumInversed = sumInversed + getInvertedSum(tiles, i)
    return (sumInversed,sumInversed%2==0)

def getInvertedSum(tiles, index):
    sumInversed = 0
    for i in range(index, len(tiles)):
        if tiles[i]==0:
            continue
        if tiles[index] > tiles[i]:
            sumInversed=sumInversed+1
    return sumInversed

goalState=[0,1,2,3,4,5,6,7,8]
newStates = goalState
for x in range(0, caseCount):
    random.shuffle(newStates)
    sumInversed, solvableTorF =solveable(newStates)
    while not solvableTorF:
        random.shuffle(newStates)
        sumInversed, solvableTorF =solveable(newStates)
    print(newStates)