import sys
from collections import deque
n = int(input())
nums = list(map(int, input().split())) # queue, 선입선출
line1 = deque(nums)
line2 = []

next_receiver = 1
while line1:
    if line1[0] == next_receiver:
        last_received = line1.popleft()
        next_receiver += 1
    else:
        line2.append(line1.popleft())

    while line2:
        if line2[-1] == next_receiver:
            last_received = line2.pop()
            next_receiver += 1
        else:
            break

if len(line2) == 0:
    print('Nice')
else:
    print('Sad')
