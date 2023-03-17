import random as r

def generate(width: int, height: int, numBomb: int) -> list[list[bool]]:
    arr = [[False for row in range(width)] for column in range(height)]
    placedBomb: int = 0
    
    position: int = 0

    while (placedBomb < numBomb) :
        position += r.randint(0, 7)
        if (arr[position % width][position % height]):
            continue
        arr[position % width][position % height] = True
        placedBomb += 1




    print(arr)

generate(5,5,3)