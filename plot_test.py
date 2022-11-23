import csv 

def writer(fileToWrite,fileName):
    with open(fileName, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        for row in fileToWrite:
            writer.writerow(row)



def main():
    mics = 9
    # speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["A","B","C","D"],["C","H","I"]]
    # speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["B","C","D"],["A","D","C","H","I"]]  #5 with 5 mics 
    # speakingInScenesList = [["B","C","D","E"],["A","C","F","G"],["C","F"],["B","C","D"],["A","D","C","H","I"]]  #5 with 5 mics
    speakingInScenesList = [["B","C","D","E"],["A","C","F","G"],["C","F","D"],["B","C"],["A","H","C","D","I"]]   #5 with 5 mics
    # speakingInScenesList = [["test", "A", "B"], ["B", "test", "Char"], ["To", "idk"]]
    # speakingInScenesList = [['Heath', 'Dewey', 'Theo', 'Ashwin', 'Harry'], ['Ned', 'Patty', 'Dewey'], ['Dewey', 'Ned'], ['Dewey', 'Heath', 'Theo', 'Louis'], ['Sophie', 'Shonelle', 'Dewey'], ['Dewey', 'Felix'], ['Dewey'], ['Dewey', 'Rosalie'], ['Rosalie', 'Heath', 'Zack', 'Summer', 'Hannah', 'Will Tackley', 'Noah', 'Louis', 'Amelia'], ['Rosalie'], ['Dewey', 'Rosalie', 'Ms Sheinkopf'], ['Dewey', 'Rosalie', 'Lucy', 'Louis'], ['Dewey', 'Rosalie', 'Ms Sheinkopf', 'Summer', 'Lawrence', 'Freddy', 'Zack'], ['Dewey', 'Ned', 'Patty'], ['Dewey', 'Gabe'], ['Rosalie'], ['Rosalie', 'Summer'], ['Dewey', 'Summer', 'Lawrence', 'Marcy', 'Zack', 'Katie', 'Freddy', 'James', 'Shonelle', 'Billy', 'Madison', 'Mason', 'Sophie', 'Tomika'], ['Felix', 'Freddy', 'Rajun', 'Billy', 'Tomika', 'Will Tackley', 'Noah', 'Heath', 'Zack'], ['Zack', 'Billy', 'Freddy', 'Lawrence', 'Madison', 'Shonelle', 'Mason'], ['Dewey', 'Marcy', 'Mason', 'Billy', 'Summer', 'Lawrence', 'Shonelle', 'Freddy', 'Zack'], ['Gabe', 'Hannah', 'Lucy', 'Ms Sheinkopf', 'Will Tackley', 'Leah', 'Noah', 'Rosie', 'Felix', 'Dewey', 'Rosalie', 'Louis'], ['Dewey', 'Rosalie', 'Gabe', 'Ms Sheinkopf'], ['Dewey', 'Shonelle', 'Marcy', 'Freddy', 'Zack', 'Mason', 'Summer', 'Billy', 'Lawrence', 'Katie', 'James', 'Rosalie', 'Sophie', 'Madison'], ['Dewey', 'Zack'], ['Mason', 'Dewey', 'Summer', 'Zack', 'Marcy', 'Lawrence', 'Rajun', 'Shonelle', 'Tomika']]
    #Need to change priorities, otherwise can have mics never used at the bottom

    # mics = max([len(x) for x in speakingInScenesList])
    # mics = 5
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
        for i in range(len(r)-1):
            if r[i] != r[i+1]:
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
    scenes = [[None for i in range(mics)] for i in range(len(arr) + 1)]
    pools = []

    pool = mics - len([1 for [a,b] in arr[0] if a != "pool"])
    for sceneChange in arr:
        for val in sceneChange:
            if val[1] == "pool":
                pool += 1
            elif val[0] == "pool":
                pool -= 1
        pools.append(pool)

    pools[-1] = mics #since the order of the last one does not need to be checked (doesn't matter if there is space in the pool or not)
    print(pools)

    for i, sceneChange in enumerate(arr):
        # toPutIn = [[x,s] for [x,s] in sceneChange if x != "pool" and s == "pool" and x not in scenes[i+1]] #so only gets in the form ["char", "pool"] that is not in the scene already
        toPutIn = [[x,s] for [x,s] in sceneChange if x != "pool" and x not in scenes[i+1]] #so only gets in the form ["char", "pool"] that is not in the scene already
        print(toPutIn)
        toPutIn = sortByPriority(arr, i, toPutIn, pools, scenes)
        print(toPutIn)
        while len(toPutIn) > 0:
            val = toPutIn[0]
            distance = getDistanceOfNoSwaps(val, arr, i, pools, scenes)
            if val[0] not in scenes[i]: #checks if the char is already in the scene
                print(val[0], "test")
                scenes[i][scenes[i].index(None)] = val[0] #if not it adds it to the first empty slot
                #THIS IS NOT OPTIMISED 
            if distance is not None: #checks if we need to add any more chars to the scenes
                for j in range(distance):
                    if pools[i+j] > 0:
                        scenes[i+j+1][scenes[i].index(val[0])] = val[0] #it is i+j+1 since j is zero indexed 
                        pools[i+j] -= 1
            toPutIn.remove(val)
            print(val)
            print(pools)
            print(scenes)

        for val in toPutIn:
            if val not in scenes[i]:
                print(val)
                scenes[i][scenes[i].index(None)] = val

        coppies = [x for [x,s] in sceneChange if x == s]
        for coppy in coppies:
            scenes[i+1][scenes[i].index(coppy)] = coppy

        # for j, val in enumerate(sceneChange):


    # for i, sceneChange in enumerate(arr):  #iterate through the scene changes
    #     for j, val in enumerate(sceneChange):
    #         if val[1] == "pool" and val[0] != "pool":
    #             for k in range(i+1, len(arr), 1):
    #                 if pools[k-2] > 0:
    #                     for v in arr[k]:
    #                         if v[0] == "pool" and v[1] == val[0]:
    #                             if val[0] not in scenes[i]: 
    #                                 scenes[i][scenes[i].index(None)] = val[0]
    #                             row = scenes[i].index(val[0])

    #                             for l in range(i+1, k+1, 1):
    #                                 scenes[l][row] = val[0]
    #                                 pools[l-1] -= 1 


    #     for n, val in enumerate(sceneChange):
    #         if val[0] not in scenes[i] and val[0] != "pool":
    #             scenes[i][scenes[i].index(None)] = val[0]

    #     for j, val in enumerate(sceneChange):
    #         if val[0] == val[1]:
    #             scenes[i+1][scenes[i].index(val[0])] = val[0]

    #add any extras that were not added to the last scene
    lastSceneChange = arr[-1]  #NOT CORRECT SINCE ONLY CHECKS LAST ONE. FIX ME! (Has I think been fixed by setting the last element of pools to the max)
    for i,val in enumerate(lastSceneChange):
        if val[0] == "pool" and val[1] not in scenes[-1]: #so has not already been added 
            if len(scenes) > 1:
                if val[1] in scenes[-2]:
                    scenes[-1][scenes[-2].index(val[1])] = val[1]

    for i,val in enumerate(lastSceneChange):
        if val[0] == "pool" and val[1] not in scenes[-1]: #so has not already been added 
            #find the first avaliable slot 
            scenes[-1][scenes[-1].index(None)] = val[1]


    return scenes

def sortByPriority(arr, sceneChangeNumber, toPutIn, pools, scenes): #sceneChangeNumber is 0 indexed
    toBeSortedQueue = []
    for item in toPutIn:
        distance = getDistanceOfNoSwaps(item, arr, sceneChangeNumber, pools, scenes)
        if distance is not None:
            toBeSortedQueue.append([distance, item])
    print(toBeSortedQueue)
    sortedQueue = sortByFirst(toBeSortedQueue)
    print(sortedQueue)
    for item in toPutIn:
        if item not in sortedQueue: #so was a None in the distance formula, so it should be at the end
            sortedQueue.append(item)

    return sortedQueue

def sortByFirst(arr): #This should sort by the first index of the list and then return an ordered list of the second indexes
    result = sorted(arr, key = lambda x: x[0], reverse=True)
    return [x for [_, x] in result]

def getDistanceOfNoSwaps(item, arr, sceneChangeNumber, pools, scenes): #sceneChangeNumber is 0 indexed
    for i in range(sceneChangeNumber + 1, len(arr), 1):
        if pools[i] > 0:
            for v in arr[i]:
                if v[0] == "pool" and v[1] == item[0]:
                    if item[0] not in scenes[i]:
                        return i - sceneChangeNumber
    return None #because this should be at the end of the priority queue no matter how we sort it.


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