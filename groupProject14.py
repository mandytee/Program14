def union(list1,list2):
    '''
    '''
    newList = []
    for el in list1:
        if el not in newList:
            newList.append(el)
    
    for el in list2:
        if el not in newList:
            newList.append(el)
    return newList 

def intersection(list1,list2):
    '''
    '''
    newList = []
    for el in list1:
        if el in list2:
            newList.append(el)
    return newList 

def membership(list1,el):
    '''
    '''
    if el in list1:
        return 'yes'
    else:
        return 'not there'

#main
print(union([1,2,2],[12,0]))
print(intersection([1,2,3,2],[10,1]))
print(membership([1,2],1))


    

