# O(nlogn) time | O(1) space
def paint(painters, timeTaken, paintingBoards):
    paintingBoards = [i*timeTaken for i in paintingBoards]

    if painters > len(paintingBoards):
        return max(paintingBoards)
    left = max(paintingBoards)
    right = sum(paintingBoards)
    finalAns = max(paintingBoards)
    while left <= right:
        mid = (left + right)//2
        if isValid(painters,paintingBoards,mid):
            finalAns = mid
            right = mid - 1
        else:
            left = mid + 1

    return finalAns%(10000003)

def isValid(painters,paintingBoards,mid):
        numOfPainter = 1
        unitsPainted = 0
        for i in paintingBoards:
            if unitsPainted + i > mid:
                numOfPainter += 1
                unitsPainted = i
                if numOfPainter > painters:
                    return False
            else:
                unitsPainted += i
        return True



print(paint(2,1,[10, 20, 30, 40]))


