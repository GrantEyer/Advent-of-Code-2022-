import textwrap



#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()


instructions = lines.split('\n')


cycleNum = 0

CRTMonitor = '.'*240

spriteBoundaries = [0,1,2]

CRTMonitorUpdated = ''

pos = 0
    
for instruction in instructions:
     
    instruction = instruction.strip()

    if instruction.startswith('addx'):
            
         

        for num in range(2):
            cycleNum += 1

            if pos in spriteBoundaries:
                CRTMonitorUpdated += '#'
            else:
                CRTMonitorUpdated += '.'

         #   print(f'Cycle:{cycleNum}')
         #   print(f'CRT Pos: {pos}')
            # print(spriteBoundaries)
            

            if num == 1:
                number = int(instruction.split(' ')[-1])
                for indx in range(len(spriteBoundaries)):
                    spriteBoundaries[indx] += number
                # print(spriteBoundaries)
            

            
         #   print(CRTMonitorUpdated)

            pos += 1

            if pos > 39:
                pos = 0
            

                

    else:
        cycleNum += 1
        
        # print(f'Cycle:{cycleNum}')
        # print(f'CRT Pos: {pos}')
        # print(spriteBoundaries)
        # print(CRTMonitorUpdated)
            
        if pos in spriteBoundaries:
            CRTMonitorUpdated += '#'
        else:
            CRTMonitorUpdated += '.'

        pos += 1

        if pos > 39:
            pos = 0

    






print(f'final pos: {pos}')

partsOfCRTScreen = textwrap.wrap(CRTMonitorUpdated,40)

screenDisplay = ''

for parts in partsOfCRTScreen:
    screenDisplay = screenDisplay + parts + '\n'

print(screenDisplay)