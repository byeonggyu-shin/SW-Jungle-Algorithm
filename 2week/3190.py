# 큐 (중) - 뱀

# 1. 뱀의 위치와 방향을 관리하기 위해 deque 자료구조를 사용합니다. deque는 큐의 양쪽 끝에서 삽입과 삭제가 가능한 자료구조로, 뱀의 머리를 쉽게 추가하고 꼬리를 제거할 수 있습니다.

# 2. 사과를 먹었을 때 뱀의 길이를 늘리기 위해, 뱀의 꼬리를 제거하지 않고 머리만 추가합니다. 이를 위해 뱀의 꼬리를 따로 저장하지 않고, 뱀의 길이를 변수로 관리합니다.

# 3.뱀의 이동을 시뮬레이션하기 위해, 뱀이 이동한 위치를 따로 저장하지 않고, 뱀의 위치와 방향 정보를 기반으로 새로운 위치를 계산합니다.

# 4. 뱀이 벽 또는 자기 자신과 충돌했는지 검사하는 코드를 간단하게 작성합니다.

# 5. 매 초마다 뱀의 방향을 바꾸는 정보를 입력받기 위해, 방향 전환 정보를 큐에 저장하고, 매 초마다 해당 정보를 확인합니다.

import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r][c] = 1

l = int(sys.stdin.readline())
directions = deque()
for _ in range(l):
    x, c = sys.stdin.readline().split()
    directions.append((int(x), c))

dx = [0, 1, 0, -1] # 방향에 따른 x, y 좌표 이동값
dy = [1, 0, -1, 0]
snake = deque()
snake.append((1, 1))  # 뱀의 위치, 머리는 (1, 1)에서 시작
direction = 0
time = 0

while True:
    time += 1
    head = snake[-1]
    x, y = head[0], head[1]
    nx, ny = x + dx[direction], y + dy[direction]

    # 뱀이 벽 또는 자기 자신과 충돌한 경우
    if nx < 1 or nx > n or ny < 1 or ny > n or (nx, ny) in snake:
        break
    
    if board[nx][ny] == 0:
        tail = snake.popleft()
        board[tail[0]][tail[1]] = 0
    snake.append((nx, ny))
    board[nx][ny] = 2
    # 뱀이 사과를 먹은 경우 if문 통과 후 머리가 길어짐

    # 방향 전환 정보 확인
    if directions and time == directions[0][0]:
        t, d = directions.popleft()
        if d == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)


# 입력값을 받아서 초기화합니다.
# 매 초마다 뱀이 이동하는 위치를 계산하고, 이동 가능 여부를 검사합니다.
# 뱀이 이동 가능한 경우, 이동한 위치에 따라 처리를 수행합니다.
# 이동한 위치에 사과가 있는 경우: 뱀의 길이를 늘리고, 사과를 없앱니다.
# 이동한 위치에 사과가 없는 경우: 뱀의 길이를 유지하고, 꼬리를 없앱니다.
# 매 초마다 방향 전환 정보를 확인하고, 방향을 변경합니다.
# 게임 종료 시간을 출력합니다.