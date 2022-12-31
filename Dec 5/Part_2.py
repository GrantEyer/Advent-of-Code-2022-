#opens file that contains elf calorie data
file = open('Puzzle Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')

stopIndx = 0
crates = []
for line in lines:
    if '[' in line:
        stopIndx += 1
        crates.append(line)
    else:
        break

columnNums = lines[stopIndx]

columnNums = set(columnNums.split(' '))
columnNums.discard('')
columnNums = [int(i) for i in columnNums]

columnNums = max(columnNums)

instructions = lines[stopIndx+2:]

rows = len(crates)

location = [['0' for col in range(columnNums)] for row in range(rows)]


rowIndx = 0

for crate in crates:
    
    
    columnIndx= 0

    for indx in range(1,len(crate),4):
        if crate[indx].isalpha():
            location[rowIndx][columnIndx] = crate[indx]+str(rowIndx)+str(columnIndx)
        
        columnIndx += 1

    rowIndx += 1



columnArray = [[[] for row in range(rows)] for col in range(columnNums)]


for rowNum in range(len(location)):

    row = location[rowNum]

    row = set(row)
 
    row.discard('0')
    row = list(row)

    for element in row:
            num = int(element[-1])
            letter = element[0]
            columnArray[num][rowNum] = letter
            

for columnNum in range(len(columnArray)):
    
    column = columnArray[columnNum]

    print(column)
    
    indx2endremoval = column.count([])-1
    print(indx2endremoval)

    if indx2endremoval >= 0:
        column = column[indx2endremoval+1:]
    

    column.reverse()
    columnArray[columnNum]=column

for instruction in instructions:

    instructionParsed = instruction.split(' ')

    numOfBoxes = int(instructionParsed[1])

    fromColNum = int(instructionParsed[3]) - 1

    toColNum = int(instructionParsed[-1]) - 1

    boxlabels=columnArray[fromColNum][-numOfBoxes:]

    #boxlabels.reverse()

    columnArray[fromColNum][-numOfBoxes:] = []

    columnArray[toColNum].extend(boxlabels)


string = ''

for column in columnArray:
    string += column[-1]

print(string) 
