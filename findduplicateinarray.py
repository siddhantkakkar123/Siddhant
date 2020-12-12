def ans(arr1, arr2):
    counter = 0
    resultList = []

    global elemt
    dict = {}
    # finding smaller
    if len(arr1) > len(arr2):
        shortList = arr2
        longList = arr1
    else:
        shortList = arr1
        longList = arr2
    # dict[shortList] = 0


    # building dict
    for elemt in shortList:
        if elemt in dict:
            dict[elemt] += 1
        else:
            dict[elemt] = 1



    #searching in dict
    for i in range(0, len(longList)):#reading and searching in dict
        elem2 = longList[i]
        if elem2 in dict and dict[elem2] > 0:
            resultList.append(elemt)
            dict[elem2] -= 1


    return resultList


arr1 = [5, 5, 4]


arr2 = [3]


resultList = ans(arr1, arr2)
print('print the result list')
print(resultList)