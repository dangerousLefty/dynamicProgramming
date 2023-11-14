def knapSack(w: int, wtList: list[int], valList: list[int]): 
    table = [[0 for i in range(w + 1)] for i in range(len(wtList))]
    rows = len(table)
    columns = len(table[0])

    #populate the first weight (base case)
    for i in range(len(table[0])):
        if i < wtList[0]:
            continue
        
        else:
            table[0][i] = valList[0]

    for i in range(1,rows):
        for j in range(columns):
            if j < wtList[i]: 
                table[i][j] = table[i-1][j]
            
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-wtList[i]] + valList[i])

    itemsSelected = []
    currentItem = table[rows-1][columns-1]
    i = rows - 1
    j = columns - 1

    while i > 0 or j > 0:
        
            #if we choose the new item
            if currentItem != table[i-1][j]:
                itemsSelected.append(wtList[i])
                currentItem = table[i-1][j-wtList[i]]
                j -= itemWeights[i]
                i -= 1
                
            
            else:
                currentItem = table[i-1][j]
                i -= 1
    
    returnTuple = (table[rows-1][columns-1], itemsSelected)
    
    return returnTuple
    




itemWeights = [5, 3, 4, 2]
itemProfits = [60, 50, 70, 30]

a = knapSack(5,itemWeights, itemProfits)
print(f"the max profix we can amass is {a[0]} with items {a[1]}")
