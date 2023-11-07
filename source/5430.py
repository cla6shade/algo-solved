from collections import deque

caseCount = int(input())
reses = []
for c in range(caseCount):
    func = input()
    arrlen = int(input())
    arrstr = input().replace('[', '')
    arrstr = arrstr.replace(']', '')
    if arrlen == 0:
        arr = []
    else:
        arr = list(map(int, arrstr.split(',')))
    arr = deque(arr)
    pl = 1
    res = ''
    for s in list(func):
        if s == 'R':
            pl *= -1
            continue
        if s == 'D':
            if len(arr) == 0:
                res = 'error'
                break
            if pl == 1:
                arr.popleft()
            elif pl == -1:
                arr.pop()
    if res != 'error':
        if pl == -1:
            arr.reverse()
        res = '[' + ','.join(list(map(str, arr))) + ']'
    reses.append(res)
for r in reses:
    print(r)