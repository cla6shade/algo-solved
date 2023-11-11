# 코딩테스트 대비 메모

## 자주 쓰이는 구문들

### input 처리
```python
n = int(input()) # 하나의 수가 주어지는 경우
mlist = list(map(int, input().split())) # 1차원 숫자 배열 입력받기

# 숫자가 띄어쓰기 없이 여러 줄로 주어지고 2차원 배열로 변환하여야 하는 경우
lsquare = [list(map(int, input())) for _ in range(n)]

# 띄어쓰기가 있고 2차원 배열로 변환하여야 하는 경우
l2square = [list(map(int, input().split())) for _ in range(n)]
```
### string 처리
```python
b = ['a', 'b', 'a', 's', 'd']

# string array를 쉼표로 join
c = ','.join(b)
```

## 헷갈리는 것들
```python
# 딕셔너리 순회 시, k에는 키값이 들어간다.
for k in {'a': 1, 'b': 2, 'c': 3}:
    print(k)
# 리스트 순회 시 v에는 인덱스에 대응하는 value가 들어간다.
for v in ['a', 'b', 'c']:
    print(v)
```

## 정렬
sort()와 sorted()는 모두 기본 오름차순 정렬이지만, reverse=True로 내림차순 정렬을 할 수 있다.
```python
alist = [2, 3, 5, 1, 7, 6]
alist.sort() # alist를 오름차순 정렬.
blist = sorted(alist) # alist를 정렬한 새로운 리스트 반환
clist = sorted(alist, reverse=True) # 내림차순 정렬

# sorted는 튜플, 객체 등 다양한 iterable 객체를 정렬할 수 있음.
# 파라미터 `key`는 lambda식으로 어떤 것을 기준으로 정렬할 지 지정할 수 있음.
# 딕셔너리를 정렬할 경우 기본적으로 딕셔너리의 키를 기준으로 정렬함.

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
```

## 이진 탐색

이진 탐색 알고리즘은 `오름차순 정렬된 리스트`에서 특정한 원소를 찾기 위한 작업.
주어지는 데이터의 크기나 길이가 매우 큰 경우, 예상 연산 횟수가 10억회가 넘어가는 경우 이진 탐색을 고려해야 한다.

```python
def binary_search(array, target, start, end):
    # start > end인 경우 유효하지 않은 연산
    while start <= end:
        # 중간 인덱스 구하기
        mid = (start + end) // 2
        # 중간 인덱스의 값과 찾으려는 값이 일치하는 경우
        if array[mid] == target:
            return mid
        # 중간 인덱스의 값이 찾으려는 값보다 큰 경우, 왼쪽 탐색
        elif array[mid] > target:
            end = mid - 1
        # 반대의 경우 오른쪽 탐색
        else:
            start = mid + 1
    return None
```

## 그래프 탐색

아래의 그래프 탐색 알고리즘들은 graph라는 변수가 [노드 번호=>[연결된 노드]] 형태로 초기화되어 있음을 가정한다.

### BFS
너비 우선 탐색, queue 사용. 당연하겠지만 visited는 사용하기 전에 node 개수만큼 초기화해야함.
```python
from collections import deque
def dfs(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```

### DFS
깊이 우선 탐색, 재귀함수 사용

```python
def dfs(graph, node, visited):
    if not visited[node]:
        print(node, end=' ')
        visited[node] = True
        for v in graph[node]:
            dfs(graph, v, visited)
```
    