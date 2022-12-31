#opens file that contains elf calorie data
file = open('input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

for marker in range(5,len(lines)):

    charList = set(lines[marker-5:marker-1])
    if len(charList) == 4:
        break

numOfChars = marker - 1
print(numOfChars)
