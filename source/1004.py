cases = int(input())


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)


counts = []


for i in range(cases):
    poses = list(map(int, input().split()))
    start, end = [poses[0], poses[1]], [poses[2], poses[3]]
    planetCount = int(input())
    counts.append(0)
    for p in range(planetCount):
        # 점과 직선사이의 거리가 반지름보다 작은 경우.
        poses = list(map(int, input().split()))
        center = [poses[0], poses[1]]
        radius = poses[2]
        startd = get_distance(start, center)
        endd = get_distance(end, center)
        if startd < radius and endd < radius:
            continue
        if startd < radius or endd < radius:
            counts[i] += 1
for c in counts:
    print(c)
