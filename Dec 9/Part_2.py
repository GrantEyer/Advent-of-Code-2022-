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


#print(positionsOfHeadList)
#print('\n')



otherLists = [[]]*8
previousHeadLists = [positionsOfHeadList]

previousHeadLists.extend(otherLists)




for numListIndx in range(len(previousHeadLists)):

    previousHeadList = previousHeadLists[numListIndx][:]  

    currentPosTailNum = [0,0]

    
    if numListIndx != len(previousHeadLists)-1:
        previousHeadListCopy = []

    for indx in range(len(previousHeadList)):
        

        
        coordinate = previousHeadList[indx]
    

        minX = coordinate[0]-1
        minY = coordinate[1]-1
        maxX = coordinate[0]+1
        maxY = coordinate[1]+1

        possibleX = list(range(minX,maxX+1))
        possibleY = list(range(minY,maxY+1))

        currentPosTailX = currentPosTailNum[0]
        currentPosTailY = currentPosTailNum[1]
        

        if currentPosTailX in possibleX and currentPosTailY in possibleY:
            pass
        elif currentPosTailX == coordinate[0]:
            if currentPosTailY < coordinate[1]: 
                currentPosTailNum[1] += 1
            else:
                currentPosTailNum[1] -= 1
        elif currentPosTailY == coordinate[1]:
            if currentPosTailX < coordinate[0]: 
                currentPosTailNum[0] += 1
            else:
                currentPosTailNum[0] -= 1
        else:
            
            if currentPosTailY < coordinate[1] and currentPosTailX < coordinate[0]:
                currentPosTailNum[0] += 1
                currentPosTailNum[1] += 1
            elif currentPosTailY > coordinate[1] and currentPosTailX > coordinate[0]:
                currentPosTailNum[0] -= 1
                currentPosTailNum[1] -= 1
            elif currentPosTailY < coordinate[1] and currentPosTailX > coordinate[0]:
                currentPosTailNum[0] -= 1
                currentPosTailNum[1] += 1
            else:
                currentPosTailNum[0] += 1
                currentPosTailNum[1] -= 1

        if numListIndx == len(previousHeadLists)-1:
            
            copyOfCoord = tuple(currentPosTailNum)
            uniquePositionsVisited.append(copyOfCoord)   
        else:
            
            copyOfPrev = currentPosTailNum[:]

            previousHeadListCopy.append(copyOfPrev)
          #  print('\n')
          #  print(f'previousHeadListCopy revised: {previousHeadListCopy}')
            

    if numListIndx != len(previousHeadLists)-1:

        previousHeadLists[numListIndx+1] = previousHeadListCopy[:]

            

uniquePositionsVisited = set(uniquePositionsVisited) 


print(len(uniquePositionsVisited))