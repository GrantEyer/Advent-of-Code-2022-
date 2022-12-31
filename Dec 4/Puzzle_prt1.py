#opens file that contains elf calorie data
file = open('Puzzle Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')

numPairs = len(lines)

countContain = 0


for pair in lines:

    pairParts = pair.split(',')


    Part1 = pairParts[0].split('-')

    Part2 = pairParts[1].split('-')
 

    
    
    Part1Nums  = []
    
    Part2Nums = []

    startPrt1 = int(Part1[0])
    endPrt1 = int(Part1[1])

    startPrt2 = int(Part2[0])
    endPrt2 = int(Part2[1])

    set1 = set(range(startPrt1,endPrt1+1))
        
    
    set2 = set(range(startPrt2,endPrt2+1))
      


    if (set1.issubset(set2)) or (set2.issubset(set1)):
        
        countContain += 1

print(countContain)
            

        




    



