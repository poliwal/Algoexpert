# O(nlogn) time | O(1) space
def books(arr, students):
    if students > len(arr):
        return -1
    if len(arr) == students:
        return max(arr)
    minPages = max(arr)
    maxPages = sum(arr)
    ans = max(arr)
    while minPages <= maxPages:
        mid = (minPages + maxPages)//2
        if isValid(arr,students,mid):
            ans = mid
            maxPages = mid - 1
        else:
            minPages = mid + 1
    return ans

def isValid(arr,students,mid):
    stud = 1
    currPages = 0
    for i in arr:
        if currPages + i > mid:
            stud += 1
            currPages = i
            if stud > students:
                return False
        else:
            currPages += i
    return True


print(books([12, 34, 67, 90], 2))