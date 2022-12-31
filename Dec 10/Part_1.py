#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

lines = lines.split('\n')

cycleNum = 0

X = 1

sumArr = []

for line in lines:
    line = line.strip()


    if line.startswith('addx'):
        
       
        for num in range(2):
            cycleNum += 1
            
            if (cycleNum-20)%40 == 0 and cycleNum <= 220:
                print(f'This is {cycleNum}')
                sumArr.append(cycleNum*X)
        
        num = int(line.split(' ')[-1])
        X += num
        

    else:
        cycleNum += 1
        if (cycleNum-20) % 40 == 0 and cycleNum <= 220:
            print(f'This is {cycleNum}')
            sumArr.append(cycleNum*X)



print(sum(sumArr))
print(sumArr)


