import math

#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

grid = lines.split('\n')

numOfVisibleTrees = 0

scenicScores = []

for rowNum in range(len(grid)):
    row = grid[rowNum].strip()

    if rowNum == 0 or rowNum == len(grid)-1:
        continue

    aboveRow = rowNum
    belowRow = rowNum+1    

    for colNum in range(len(row)):
        
        if colNum == 0 or colNum == len(row)-1:
            continue
        else:
            rowsAbove2Analyze = grid[:aboveRow]
            rowsAbove2Analyze.reverse()

            rowsBelow2Analyze = grid[belowRow:]
        

            top = [trees[colNum] for trees in rowsAbove2Analyze]
            bottom = [trees[colNum] for trees in rowsBelow2Analyze]
            left=list(row[:colNum])
            left.reverse()
            right=list(row[colNum+1:])

            treeHeight = int(row[colNum])

            Scores = [0,0,0,0]

            Indx = -1

            for section in (top,bottom,left,right):
                Indx += 1
                for tree in section:
                    
                    if treeHeight <= int(tree):
                        Scores[Indx] += 1
                        break

                    Scores[Indx] += 1
        
        TotalScore = math.prod(Scores)
        scenicScores.append(TotalScore)


print(max(scenicScores))