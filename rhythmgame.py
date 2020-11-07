### Thing
print("Daniel Was here")
print("Andrew changed this")
print('Ricky was here')

#beatmap = open("beatmap.txt", "r")

from 

def readfile(path):
    with open(path,'rt') as f:
        return f.read()

def filetoList(file):
    path = file
    content = readfile(path)
    result = []
    for line in content.splitlines():
        result.append(line.split(','))
    return result

print(filetoList('beatmap.txt'))
beatmap = open("beatmap.txt", "r")

beatmapList = beatmap.readlines()

beatmap.close()

print(beatmapList)
