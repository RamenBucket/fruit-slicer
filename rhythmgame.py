### Thing
print("Daniel Was here")
print("Andrew changed this")
print('Ricky was here')

beatmap = open("beatmap.txt", "r")

beatmapList = beatmap.readlines()

beatmap.close()

print(beatmapList)