import random as r

def generateBool(width: int, height: int, numBomb: int) -> list[list[bool]]:
    arr = [[False for row in range(height)] for column in range(width)]
    placedBomb: int = 0
    
    position: int = 0

    while (placedBomb < numBomb) :
        position += r.randint(0, 7)
        if (arr[position // height][position % width]):
            continue
        arr[position // height][position % width] = True
        placedBomb += 1
    return arr


def generateBoard(boolMap: list[list[bool]]) -> list[list[int]]:
    arr = [[0 for row in range(len(boolMap[0]))] for column in range(len(boolMap))]

    for y in range(len(arr[0])):
        for x in range(len(arr[0])):
            if boolMap[x][y]:
                incrementNeighbors(x, y, arr)

    for y in range(len(arr[0])):
        for x in range(len(arr)):
            if boolMap[x][y]:
                print(f" {x}, {y}")
                arr[x][y] = -1
    
    return arr

def incrementNeighbors(x: int, y: int, array: list[list[int]]):
    #Only enter here if position has a min
    height: int = len(array)
    width: int = len(array[0])

    if (x == 0):
        #Top
        if (y == 0):
            #Top left
            array[x + 1][y] += 1
            array[x + 1][y - 1] += 1
            array[x][y-1] += 1
        elif (y == width - 1):
            #Top right
            array[x + 1][y] += 1
            array[x + 1][y - 1] += 1
            array[x][y - 1] += 1
        else:
            #Top side
            array[x + 1][y] += 1
            array[x + 1][y + 1] += 1
            array[x][y + 1] += 1
            array[x + 1][y - 1] += 1
            array[x][y-1] += 1
    elif (x == height - 1):
        if (y == 0):
            #Bottom left
            array[x - 1][y] += 1
            array[x - 1][y - 1] += 1
            array[x][y-1] += 1
        elif (y == width - 1):
            #Bottom right
            array[x - 1][y] += 1
            array[x - 1][y - 1] += 1
            array[x][y - 1] += 1
        else:
            #Bottom side
            array[x - 1][y] += 1
            array[x - 1][y + 1] += 1
            array[x][y + 1] += 1
            array[x - 1][y - 1] += 1
            array[x][y-1] += 1
    elif y == 0:
        #Left side
        array[x + 1][y] += 1
        array[x + 1][y + 1] += 1
        array[x][y + 1] += 1
        array[x - 1][y] += 1
        array[x - 1][y + 1] += 1
    elif y == width - 1:
        #Right Side
        array[x + 1][y] += 1
        array[x + 1][y - 1] += 1
        array[x][y - 1] += 1
        array[x - 1][y] += 1
        array[x - 1][y - 1] += 1
    else:
        array[x - 1][y] += 1
        array[x - 1][y + 1] += 1
        array[x][y + 1] += 1
        array[x - 1][y - 1] += 1
        array[x][y-1] += 1
        array[x + 1][y] += 1
        array[x + 1][y + 1] += 1
        array[x + 1][y - 1] += 1
            


boolMap = generateBool(5, 5, 3)

for row in boolMap:
    print(row)

for row in generateBoard(boolMap):
    print(row)
