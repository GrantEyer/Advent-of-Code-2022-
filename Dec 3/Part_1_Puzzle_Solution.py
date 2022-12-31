#opens file that contains elf calorie data
file = open('Puzzle Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')
lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
total = 0



for line in lines:
    
    rucksackLength = len(line)
    rucksackHalf = int(rucksackLength/2)
    firstHalf = line[:rucksackHalf]
   
    secondHalf = line[rucksackHalf:]
   

    for letter in firstHalf:
        if letter in secondHalf:
            print(letter)
            if letter in lowercase:
                total += lowercase.index(letter) + 1
            elif letter in uppercase:
                total += uppercase.index(letter)+27

            break
        
print(total)