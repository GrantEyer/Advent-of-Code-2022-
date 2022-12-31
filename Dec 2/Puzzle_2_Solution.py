#opens file that contains elf calorie data
file = open('Puzzle 1 Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')
pointsArr = []
OpponentPossible = ["A","B","C"]
MyPossible = ["X","Y","Z"]

addPoints = ['Y','Z']

for i in range(len(lines)):

    round = lines[i].strip()
 
    OpponentMove = round[0]
    
    MyMove = round[-1]
    
   
    OpponentMade = OpponentPossible.index(OpponentMove)
    #opens file that contains elf calorie data
file = open('Puzzle 1 Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')
pointsArr = []
OpponentPossible = ["A","B","C"]
MyPossible = ["X","Y","Z"]

addPoints = ["Y","Z"]
winningPairs = ['A B','B C','C A']
losingPairs = ['A C','B A','C B']

for i in range(len(lines)):

    round = lines[i].strip()
 
    OpponentMove = round[0]
    
    MyMove = round[-1]
    
   
    OpponentMade = OpponentPossible.index(OpponentMove)
    MyMade = MyPossible.index(MyMove)

    if MyMove == 'Z':
        if OpponentMove in ["A","B"]:
            pointsArr.append(OpponentMade+2) 
        else:
            pointsArr.append(1)
    elif MyMove == 'X':
        if OpponentMove in ["B","C"]:
            pointsArr.append(OpponentMade) 
        else:
            pointsArr.append(3)
        
    else: pointsArr.append(OpponentMade+1)


    if MyMove in addPoints:
        pointsArr.append(3*(MyMade))
    
    print(pointsArr)


print(sum(pointsArr))
