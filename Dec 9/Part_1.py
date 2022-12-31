currentPosHead = [0,0]
positionsOfHeadList = []
currentPosTail = [0,0]
uniquePositionsVisited = [tuple(currentPosTail)]

#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

instructions = lines.split('\n')

for instruction in instructions:
    instruction = instruction.strip()



    instruction = instruction.split(' ')
    direction = instruction[0]
    steps = int(instruction[1])

    for num in range(1,steps+1):
        if direction == 'R':
            currentPosHead[0] += 1

        elif direction == 'L':

            currentPosHead[0] -= 1

        elif direction == 'U':

            currentPosHead[1] += 1

        else:

            currentPosHead[1] -= 1

        positionsOfHeadList.append(currentPosHead[:])



for indx in range(len(positionsOfHeadList)):

    coordinate = positionsOfHeadList[indx]

    minX = coordinate[0]-1
    minY = coordinate[1]-1
    maxX = coordinate[0]+1
    maxY = coordinate[1]+1

    possibleX = list(range(minX,maxX+1))
    possibleY = list(range(minY,maxY+1))

    currentPosTailX = currentPosTail[0]
    currentPosTailY = currentPosTail[1]

    if currentPosTailX in possibleX and currentPosTailY in possibleY:
        continue
    elif currentPosTailX == coordinate[0]:
        if currentPosTailY < coordinate[1]: 
            currentPosTail[1] += 1
        else:
            currentPosTail[1] -= 1
    elif currentPosTailY == coordinate[1]:
        if currentPosTailX < coordinate[0]: 
            currentPosTail[0] += 1
        else:
            currentPosTail[0] -= 1
    else:
        currentPosTail = positionsOfHeadList[indx-1]


    copyOfCoord = tuple(currentPosTail)

    uniquePositionsVisited.append(copyOfCoord)   


uniquePositionsVisited = set(uniquePositionsVisited) 

print(len(uniquePositionsVisited))









