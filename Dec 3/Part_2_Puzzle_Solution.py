#opens file that contains elf calorie data
file = open('Puzzle Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n')
groups = []
for i in range(0,len(lines),3):
    groups.extend([lines[i:i+3]])


lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = lowercase.upper()
total = 0
commonletter = ''


for group in groups:
  
    line = group[0]
 
 
    for letter in line:

        if (letter in group[1]) and (letter in group[2]):
         commonletter = letter
         break
    

    if commonletter in lowercase:
        total += lowercase.index(letter) + 1
    elif commonletter in uppercase:
        total += uppercase.index(letter)+27

print(total)