#opens file that contains elf calorie data
file = open('Puzzle 1 Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')
pointsArr = []
OpponentPossible = ["A","B","C"]
MyPossible = ["X","Y","Z"]

winningPairs = ['A Y','B Z','C X']

for i in range(len(lines)):

    round = lines[i].strip()
 
    OpponentMove = round[0]
    
    MyMove = round[-1]
    
   
    OpponentMade = OpponentPossible.index(OpponentMove)
    MyMade = MyPossible.index(MyMove)

    pointsArr.append(MyMade+1)

    if OpponentMade == MyMade:
        pointsArr.append(3)
    elif round in winningPairs:
        pointsArr.append(6)

print(sum(pointsArr))



    