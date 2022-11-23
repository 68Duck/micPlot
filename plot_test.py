import csv 

def writer(fileToWrite,fileName):
    with open(fileName, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        for row in fileToWrite:
            writer.writerow(row)



def main():
    mics = 14
    speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["A","B","C","D"],["C","H","I"]]
    speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["B","C","D"],["A","D","C","H","I"]]
    speakingInScenesList = [["B","C","D","E"],["A","C","F","G"],["C","F"],["B","C","D"],["A","D","C","H","I"]]  #Could this be a problem to the algorithmn? 
    speakingInScenesList = [["B","C","D","E"],["A","C","F","G"],["C","F","D"],["B","C"],["A","D","C","H","I"]]  #Could this be a problem to the algorithmn? 
    # speakingInScenesList = [["test", "A", "B"], ["B", "test", "Char"], ["To", "idk"]]
    speakingInScenesList = [['Heath', 'Dewey', 'Theo', 'Ashwin', 'Harry'], ['Ned', 'Patty', 'Dewey'], ['Dewey', 'Ned'], ['Dewey', 'Heath', 'Theo', 'Louis'], ['Sophie', 'Shonelle', 'Dewey'], ['Dewey', 'Felix'], ['Dewey'], ['Dewey', 'Rosalie'], ['Rosalie', 'Heath', 'Zack', 'Summer', 'Hannah', 'Will Tackley', 'Noah', 'Louis', 'Amelia'], ['Rosalie'], ['Dewey', 'Rosalie', 'Ms Sheinkopf'], ['Dewey', 'Rosalie', 'Lucy', 'Louis'], ['Dewey', 'Rosalie', 'Ms Sheinkopf', 'Summer', 'Lawrence', 'Freddy', 'Zack'], ['Dewey', 'Ned', 'Patty'], ['Dewey', 'Gabe'], ['Rosalie'], ['Rosalie', 'Summer'], ['Dewey', 'Summer', 'Lawrence', 'Marcy', 'Zack', 'Katie', 'Freddy', 'James', 'Shonelle', 'Billy', 'Madison', 'Mason', 'Sophie', 'Tomika'], ['Felix', 'Freddy', 'Rajun', 'Billy', 'Tomika', 'Will Tackley', 'Noah', 'Heath', 'Zack'], ['Zack', 'Billy', 'Freddy', 'Lawrence', 'Madison', 'Shonelle', 'Mason'], ['Dewey', 'Marcy', 'Mason', 'Billy', 'Summer', 'Lawrence', 'Shonelle', 'Freddy', 'Zack'], ['Gabe', 'Hannah', 'Lucy', 'Ms Sheinkopf', 'Will Tackley', 'Leah', 'Noah', 'Rosie', 'Felix', 'Dewey', 'Rosalie', 'Louis'], ['Dewey', 'Rosalie', 'Gabe', 'Ms Sheinkopf'], ['Dewey', 'Shonelle', 'Marcy', 'Freddy', 'Zack', 'Mason', 'Summer', 'Billy', 'Lawrence', 'Katie', 'James', 'Rosalie', 'Sophie', 'Madison'], ['Dewey', 'Zack'], ['Mason', 'Dewey', 'Summer', 'Zack', 'Marcy', 'Lawrence', 'Rajun', 'Shonelle', 'Tomika']]
    #Need to change priorities, otherwise can have mics never used at the bottom

    # mics = max([len(x) for x in speakingInScenesList])
    mics = 5
    arr = []
    for i in range(len(speakingInScenesList)-1):
        arr.append(getMoves(speakingInScenesList[i], speakingInScenesList[i+1]))
    # print(arr)
    # print(parseArr(arr,mics))
    # prettyPrint(parseArr(arr, mics), mics)
    print(arr)
    parsedArr = parseArr(arr, mics)
    writer(reverseScenes(parsedArr,mics), "test.csv")
    prettyPrint(parsedArr, mics)
    print(calcChanges(parsedArr, mics))

def calcChanges(parsedArr, mics): #Not in reversed form
    reversed = reverseScenes(parsedArr, mics)
    total = 0 
    for row in reversed:
        r = [x for x in row if x is not None]
        for i in range(len(row)-2):
            if row[i] != row[i+1]:
                total += 1
    return total 

def reverseScenes(scenes, mics):
    reversed = [[None for i in range(len(scenes))] for i in range(mics)]
    for i in range(len(scenes)):
        for j in range(len(scenes[i])):
            reversed[j][i] = scenes[i][j]

    return reversed

def prettyPrint(scenes, mics):
    reversed = [[None for i in range(len(scenes))] for i in range(mics)]
    for i in range(len(scenes)):
        maxlen = max([len(x) if x is not None else 0 for x in scenes[i]]) - 1
        for j in range(len(scenes[i])):
            reversed[j][i] = addSpaces(scenes[i][j] if scenes[i][j] is not None else " ", maxlen) 
    
    for row in reversed:
        # maxlen = max([len(x) if x is not None else 0 for x in row])
        # print(" | ".join([addSpaces(x, maxlen) if x is not None else " " for x in row]))
        print(" | ".join([x if x is not None else " " for x in row]))

def addSpaces(word, desiredLength): #not working yet. (This function works but is not implemented properly into prettyPrint)
    return word + " ".join([" " for i in range(desiredLength - len(word))])


def parseArr(arr, mics):
    # first = []
    # for val in arr[0]:
    #     [a,b] = val
    #     if a is not "pool":
    #         first.append(a)

    # for i in range(mics - len(first)):
    #     first.append(None)

    # scenes = [first]

    # for sceneChange in arr:
    #     nextScene = [None] * mics
    #     for val in sceneChange:
    #         if val[0] == val[1] and val[0] in scenes[-1]:
    #             nextScene[scenes[-1].index(val[0])] = val[0]
    #     scenes.append(nextScene)
    
    scenes = [[None for i in range(mics)] for i in range(len(arr) + 1)]
    pools = []

    pool = 0
    for sceneChange in arr:
        for val in sceneChange:
            if val[1] == "pool":
                pool += 1
            elif val[0] == "pool":
                pool -= 1
        pools.append(pool)

    for i, sceneChange in enumerate(arr):  #iterate through the scene changes
        for j, val in enumerate(sceneChange):
            if val[1] == "pool" and val[0] != "pool":
                for k in range(i+1, len(arr), 1):
                    # print(k, pools[k-1])
                    if pools[k-2] > 0:
                        for v in arr[k]:
                            if v[0] == "pool" and v[1] == val[0]:
                                # prettyPrint(scenes, mics)
                                if val[0] not in scenes[i]: 
                                    scenes[i][scenes[i].index(None)] = val[0]
                                row = scenes[i].index(val[0])

                                for l in range(i+1, k+1, 1):
                                    scenes[l][row] = val[0]
                                    pools[l-1] -= 1 
                                    # print(pools, "pools")


        for n, val in enumerate(sceneChange):
            # print(scenes[i])
            if val[0] not in scenes[i] and val[0] != "pool":
                # print(val)
                # find the first avaliable slot
                # print(scenes[i])
                # print(scenes[i].index(None))
                # print(scenes[i][scenes[i].index(None)])
                # print(val[0])
                scenes[i][scenes[i].index(None)] = val[0]

        for j, val in enumerate(sceneChange):
            if val[0] == val[1]:
                # print(scenes[i])
                scenes[i+1][scenes[i].index(val[0])] = val[0]

    #add any extras that were not added to the last scene
    lastSceneChange = arr[-1]
    for i,val in enumerate(lastSceneChange):
        if val[0] == "pool" and val[1] not in scenes[-1]: #so has not already been added 
            #find the first avaliable slot
            scenes[-1][scenes[-1].index(None)] = val[1]


    return scenes

def getMoves(scene, next):
    arr = []
    for val in scene:
        if val in next:
            arr.append([val,val])
        else:
            arr.append([val,"pool"])

    for val in next:
        if val not in scene:
            arr.append(["pool",val])
    return arr            

main()