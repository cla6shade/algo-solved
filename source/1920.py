n = int(input())
alist = list(map(int, input().split()))
alist.sort()


def search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


m = int(input())
blist = list(map(int, input().split()))
for b in blist:
    if search(alist, b) == None:
        print(0)
    else:
        print(1)
