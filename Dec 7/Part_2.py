#opens file that contains elf calorie data
file = open('Input.txt','r')

#reads the file and splits the elf calories by finding the blank lines
lines = file.read()

commands = lines.split('\n')

directoriesKey = {}

directoriesNotToConsider = set()

currentDirectory = ' '


for command in commands:

  #  print('stuck in loop 1')

  command = command.strip()


  if command.startswith('$ cd'):

    command = command[2:]

    directorySym = command.split(' ')
        

    if directorySym[-1] == '..':
      
      # list out keys and values separately
      key_list = list(directoriesKey.keys())
      val_list = list(directoriesKey.values())
            
 
      # print key with value of current directory
      for indx in range(len(val_list)):
               
        if currentDirectory in val_list[indx]:       
          break

      currentDirectory = key_list[indx]    

    elif directorySym[-1] != '/':
      
      directoryFull = currentDirectory + '-' + directorySym[-1]

      if directoryFull not in directoriesKey[currentDirectory]:
        directoriesKey[currentDirectory].append(directoryFull)
        
        
      if directoryFull not in directoriesKey.keys():
        directoriesKey[directoryFull] = []
      
      currentDirectory = directoryFull

    else:

      if directorySym[-1] not in directoriesKey.keys():
        directoriesKey[directorySym[-1]] = []

      currentDirectory = directorySym[-1]

  elif command.startswith('$ ls'):
    continue

  else:

      line = command.split('\n')

      for info in line:
        if info.startswith('dir'):
          dirName = info.split(' ')[-1]
          dirNameFull = currentDirectory + '-' + dirName
          if dirNameFull not in directoriesKey.keys():
            directoriesKey[dirNameFull] = []
            if dirNameFull not in directoriesKey[currentDirectory]:
              directoriesKey[currentDirectory].append(dirNameFull)
             #   print(f'directory {dirName}')
        else:
          fileSize = int(info.split(' ')[0])
           
          directoriesKey[currentDirectory].append(fileSize)


# list out keys and values separately
key_list = list(directoriesKey.keys())
val_list = list(directoriesKey.values())


for key in key_list:
  
  # print key with value of current directory
  for indx in range(len(val_list)):

    if key in val_list[indx]:
      key2changevalue = key_list[indx]
            
            
      # directoriesKey[key2changevalue] += directoriesKey[key]
      directoriesKey[key2changevalue].extend(directoriesKey[key])

 
DirectBytesInfo = {}

# list out keys and values separately
key_list = list(directoriesKey.keys())
val_list = list(directoriesKey.values())

for indx in range(len(val_list)):
  
  bytesInDirectory = 0
   
  for value in val_list[indx]:

    if isinstance(value,int):
      bytesInDirectory += value
    
    DirectBytesInfo[key_list[indx]] = bytesInDirectory


overallDirectory = DirectBytesInfo['/']

unusedSpaceOrig = 7e7-overallDirectory

del(DirectBytesInfo['/'])

for bytes in sorted(DirectBytesInfo.values()):
    
    unusedSpace = bytes + unusedSpaceOrig
    
    if unusedSpace >= 3e7:
        print(f'Size of smallest is {bytes}')
        break





