#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

grid = lines.split('\n')

numOfVisibleTrees = 0



for rowNum in range(len(grid)):
    row = grid[rowNum].strip()

    if rowNum == 0 or rowNum == len(grid)-1:
        numOfVisibleTrees += len(row)
        continue
    
    aboveRow = rowNum
    belowRow = rowNum+1

    for colNum in range(len(row)):
        
        if colNum == 0 or colNum == len(row)-1:
            numOfVisibleTrees += 1
        else:
            rowsAbove2Analyze = grid[:aboveRow]
            rowsBelow2Analyze = grid[belowRow:]
            top = [trees[colNum] for trees in rowsAbove2Analyze]
            bottom = [trees[colNum] for trees in rowsBelow2Analyze ]
            left=row[:colNum]
            right=row[colNum+1:]

            topMax = max(top)
            botMax = max(bottom)
            leftMax = max(left)
            rightMax = max(right)

            maxHeight =(topMax,botMax,leftMax,rightMax)

            columnHeight = row[colNum]

            for Height in maxHeight:
                if columnHeight > Height:
                    numOfVisibleTrees  += 1
                    break

print(numOfVisibleTrees)


            
            













# for indx in range(len(rows)):
#     rows[indx] = rows[indx].strip()


# VisibleTreesOnPerimeter = 2*len(rows[0])+ 2*len(rows)

# top = rows[0]
# bottom = rows[-1]

# left = ''
# right = ''

# for row in rows:
#     left += row[0]
#     right += row[-1]


# print(top)
# print(bottom)
# print(left)
# print(right)




