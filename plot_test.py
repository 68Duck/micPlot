

def main():
    # mics = 5
    # speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["A","B","C","D"],["C","H","I"]]
    # # speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["B","C","D"],["C","H","I"]]
    # scenes = [[None] * mics]
    # pool = {}
    # for i in range(len(speakingInScenesList)):
    #     (scene, pool) = nextScene(speakingInScenesList[i], scenes[-1], pool, mics)
    #     scenes.append(scene)
    mics = 5
    speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["A","B","C","D"],["C","H","I"]]
    speakingInScenesList = [["A","B","C","D","E"],["C","F","G"],["C","F"],["B","C","D"],["A","D","C","H","I"]]
    arr = []
    for i in range(len(speakingInScenesList)-1):
        arr.append(getMoves(speakingInScenesList[i], speakingInScenesList[i+1]))
    print(arr)
    print(parseArr(arr,mics))
    prettyPrint(parseArr(arr, mics), mics)

def prettyPrint(scenes, mics):
    reversed = [[None for i in range(5)] for i in range(5)]
    for i in range(len(scenes)):
        for j in range(len(scenes[i])):
            reversed[i][j] = scenes[j][i]
    
    for row in reversed:
        print(" ".join([x if x is not None else " " for x in row]))
        # print(row)



#One change I think fixed the last row 
def parseArr(arr, mics):
    first = []
    for val in arr[0]:
        [a,b] = val
        if a is not "pool":
            first.append(a)

    for i in range(mics - len(first)):
        first.append(None)

    scenes = [first]

    for sceneChange in arr:
        nextScene = [None] * mics
        for val in sceneChange:
            if val[0] == val[1] and val[0] in scenes[-1]:
                nextScene[scenes[-1].index(val[0])] = val[0]
        scenes.append(nextScene)

    pools = []

    pool = 0
    for sceneChange in arr:
        for val in sceneChange:
            if val[1] == "pool":
                pool += 1
            elif val[0] == "pool":
                pool -= 1
        pools.append(pool)

    # for i,sceneChange in enumerate(arr):
    #     for r,val in enumerate(sceneChange):
    #         if (val[1] == "pool") and (val[0] != "pool"):
    #             for j in range(i+1,len(arr)-1,1):
    #                 if pools[j-1] > 0:
    #                     print(j-1, pools[j-1])
    #                     # print("test")
    #                     for v in arr[j]:
    #                         # print(v)
    #                         if v[0] == "pool" and v[1] == val[0]:
    #                             for k in range(i+1, j, 1):
    #                                 # print("test")
    #                                 scenes[k][r] = val[0]
    #                                 print(val[0])
    #                                 pools[k-1] -= 1
    #                                 print(pools,"pools")



    for i, sceneChange in enumerate(arr):  #iterate through the scene changes
        for j, val in enumerate(sceneChange):
            if val[1] == "pool" and val[0] != "pool":
                for k in range(i+1, len(arr), 1):
                    # print(k, pools[k-1])
                    if pools[k-2] > 0:
                        for v in arr[k]:
                            if v[0] == "pool" and v[1] == val[0]:
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

#Works up until the last column    
# def parseArr(arr, mics):
#     first = []
#     for val in arr[0]:
#         [a,b] = val
#         if a is not "pool":
#             first.append(a)

#     for i in range(mics - len(first)):
#         first.append(None)

#     scenes = [first]

#     for sceneChange in arr:
#         nextScene = [None] * mics
#         for val in sceneChange:
#             if val[0] == val[1] and val[0] in scenes[-1]:
#                 nextScene[scenes[-1].index(val[0])] = val[0]
#         scenes.append(nextScene)

#     pools = []

#     pool = 0
#     for sceneChange in arr:
#         for val in sceneChange:
#             if val[1] == "pool":
#                 pool += 1
#             elif val[0] == "pool":
#                 pool -= 1
#         pools.append(pool)

#     # for i,sceneChange in enumerate(arr):
#     #     for r,val in enumerate(sceneChange):
#     #         if (val[1] == "pool") and (val[0] != "pool"):
#     #             for j in range(i+1,len(arr)-1,1):
#     #                 if pools[j-1] > 0:
#     #                     print(j-1, pools[j-1])
#     #                     # print("test")
#     #                     for v in arr[j]:
#     #                         # print(v)
#     #                         if v[0] == "pool" and v[1] == val[0]:
#     #                             for k in range(i+1, j, 1):
#     #                                 # print("test")
#     #                                 scenes[k][r] = val[0]
#     #                                 print(val[0])
#     #                                 pools[k-1] -= 1
#     #                                 print(pools,"pools")



#     for i, sceneChange in enumerate(arr):  #iterate through the scene changes
#         for j, val in enumerate(sceneChange):
#             if val[1] == "pool" and val[0] != "pool":
#                 for k in range(i+1, len(arr)-1, 1):
#                     # print(k, pools[k-1])
#                     if pools[k-2] > 0:
#                         for v in arr[k]:
#                             if v[0] == "pool" and v[1] == val[0]:
#                                 row = scenes[i].index(val[0])
#                                 for l in range(i+1, k+1, 1):
#                                     scenes[l][row] = val[0]
#                                     pools[l-1] -= 1 
#                                     # print(pools, "pools")


#         for n, val in enumerate(sceneChange):
#             # print(scenes[i])
#             if val[0] not in scenes[i] and val[0] != "pool":
#                 # print(val)
#                 # find the first avaliable slot
#                 scenes[i][scenes[i].index(None)] = val[0]

#         for j, val in enumerate(sceneChange):
#             if val[0] == val[1]:
#                 # print(scenes[i])
#                 scenes[i+1][scenes[i].index(val[0])] = val[0]

#     #add any extras that were not added to the last scene
#     lastSceneChange = arr[-1]
#     for i,val in enumerate(lastSceneChange):
#         if val[0] == "pool" and val[1] not in scenes[-1]: #so has not already been added 
#             #find the first avaliable slot
#             scenes[-1][scenes[-1].index(None)] = val[1]


#     return scenes


        

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
            


# def nextScene(toPutIn, previous, pool, mics):
#     print(pool,"pool")
#     print(toPutIn)
#     print(previous,"previous")
#     scene = [None] * mics

#     removingList = []
#     for (i,val) in enumerate(previous):
#         if val in toPutIn:
#             scene[i] = val
#             removingList.append(val)

#     for val in removingList:
#         toPutIn.remove(val)

#     removingList = []
#     for (i,val) in enumerate(toPutIn):
#         if val in pool:
#             scene[pool[val]] = val
#             removingList.append(val)

#     for val in removingList:
#         toPutIn.remove(val)

#     for val in toPutIn:
#         scene[scene.index(None)] = val

#     newPool = {}
#     for i,val in enumerate(previous):
#         if val not in scene:
#             newPool[val] = i 

#     for key in pool:
#         if key not in scene:
#             newPool[key] = pool[key]


#     return (scene, newPool)
    
# def nextScene(toPutIn, previous, pool, mics):
#     print(pool,"pool")
#     print(toPutIn)
#     print(previous,"previous")
#     scene = [None] * mics

#     removingList = []
#     for (i,val) in enumerate(previous):
#         if val in toPutIn:
#             scene[i] = val
#             removingList.append(val)

#     for val in removingList:
#         toPutIn.remove(val)

#     removingList = []
#     for (i,val) in enumerate(toPutIn):
#         if val in pool:
#             scene[pool[val]] = val
#             removingList.append(val)

#     for val in removingList:
#         toPutIn.remove(val)

#     for val in toPutIn:
#         scene[scene.index(None)] = val

#     newPool = {}
#     for i,val in enumerate(previous):
#         if val not in scene:
#             newPool[i] = val 

#     for key in pool:
#         val = pool[key]
#         if val not in scene:
#             newPool[key] = val


#     return (scene, newPool)
    




main()