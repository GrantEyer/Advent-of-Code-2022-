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
    calorieArr.append(sum(result))


#Sort the calorieArr list and find the greatest three total calories. Sum these values.
calorieArr.sort()
print(sum(calorieArr[-3:]))
