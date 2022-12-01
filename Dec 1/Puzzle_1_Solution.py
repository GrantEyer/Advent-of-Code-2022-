#opens file that contains elf calorie data
file = open('Puzzle_1_elf_calories_data.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()
lines = lines.split('\n\n')

#Creates an empty array to store data 
calorieArr = []

#Loop through each entry 
for line in lines:

    #Create a numerical list for each elf, then sum the 
    #values to find the total number of calories for
    #that elf.
    result = [int(i) for i in line.split('\n')]

    #Each entry is added to the calorieArr list
    calorieArr.append(sum(result))

#For Puzzle 1, simply find the maximum number of total calories oout of all the elves.
print(max(calorieArr))

