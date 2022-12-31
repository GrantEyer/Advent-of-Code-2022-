import math

#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

lines = lines.split('\n\n')

monkeyDictItems = {}


for line in lines:

    segment = line.split('\n')

    keyName = segment[0][:-1]

    startingItems = segment[1].strip()

    startingItems = startingItems.split(':')[-1]

    startingItems = startingItems.strip()

    startingItems = startingItems.split(',')

    Items = [int(num) for num in startingItems]


    operationSpec = segment[2].split('=')[-1]

    operationSpec = operationSpec.strip()


    divideSpec = segment[3].split('by')[-1]

    divideSpec = int(divideSpec.strip())

    
    trueSpec = segment[4].split('to')[-1]

    trueSpec = trueSpec.strip().title()

        
    falseSpec = segment[5].split('to')[-1]

    falseSpec = falseSpec.strip().title()

    logicSpec = [trueSpec,falseSpec]

    numberOfCounts = 0

    monkeyDictItems[keyName] = [Items,operationSpec,divideSpec,logicSpec,numberOfCounts]


itemsCountArr = []

for round in range(1,21):

    for key in monkeyDictItems.keys():

        itemsList = monkeyDictItems[key][0]

        while itemsList:
    
            item = itemsList.pop(0)

            monkeyDictItems[key][4] += 1

            operation = monkeyDictItems[key][1]
            operation = operation.replace('old',str(item))
            worryLevel = eval(operation)

            worryLevel = math.floor(worryLevel/3)

            testNum = monkeyDictItems[key][2]

            if worryLevel % testNum == 0:
                key2transfer2 = monkeyDictItems[key][3][0]
            else:
                key2transfer2 = monkeyDictItems[key][3][1]

            monkeyDictItems[key2transfer2][0].append(worryLevel)
            
        if round == 20:
            itemsCountArr.append(monkeyDictItems[key][4])


itemsCountArr = sorted(itemsCountArr,reverse=True)

monkeyBusiness = math.prod(itemsCountArr[:2])

print(monkeyBusiness)

print(monkeyDictItems)
