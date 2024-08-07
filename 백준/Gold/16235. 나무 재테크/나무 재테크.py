# 봄 : 나무가 자신의 나이만큼 양분 먹고 나이 1 증가 (나이가 어린 나무부터 양분)
# 여름 : 죽은 나무가 양분으로 변함(죽은 나무 나이를 2로 나눈 몫)
# 가을 : 나이가 5의 배수인 나무는 번식(인접한 8개의 칸)
# 겨울 : 양분 추가

import sys

# N * N 의 땅
# M개의 나무
# K년
N, M, K = map(int, sys.stdin.readline().split())
# 겨울에 추가되는 양분
eat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for i in range(N)]
for i in range(M):
    x, y, age = map(int, sys.stdin.readline().split())
    # 3차원 리스트에 나무의 나이를 추가
    trees[x - 1][y - 1].append(age)
# 초기 양분
pan = [[5] * N for _ in range(N)]
# 죽은 나무들의 좌표,나이를 저장할 리스트
die_trees = []
# 8방향
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, -1, 1, 1, -1, 0]


# 봄
def spring():  
    for i, line in enumerate(trees):
        for j, ages in enumerate(line):
            # 각 좌표에 존재하는 나무들의 나이 리스트를 오름차순으로 정렬한다.
            # 어린 나무부터 양분을 먹게하기 위하여
            trees[i][j].sort()
            for k, age in enumerate(ages):
                # 양분이 나이 만큼 충분할 때
                if age <= pan[i][j]:
                    pan[i][j] -= age
                    trees[i][j][k] += 1
                # 양분이 나이만큼 충분하지 않을 때
                else:
                    # 전부 죽은 나무리스트에 넣기
                    for _ in range(k, len(trees[i][j])):
                        die_trees.append([i, j, trees[i][j].pop()])
                    break

# 여름
def summer():  
    while die_trees:
        x, y, age = die_trees.pop()
        # 양분화됨
        pan[x][y] += age // 2


# 가을, 겨울
def autumn_winter():
    for i, line in enumerate(trees):
        for j, ages in enumerate(line):
            for k, age in enumerate(ages):
                # 나이가 5의 배수
                if age % 5 == 0 and age != 0:
                    # 주위 8방향
                    for t in range(8):
                        ni = i + dx[t]
                        nj = j + dy[t]
                        if ni >= N or nj >= N or ni < 0 or nj < 0:
                            continue
                        # 배열에서 벗어나지 않는다면 새로운 나무 번식
                        trees[ni][nj].append(1)
            # 로봇이 양분 추가 - 겨울
            pan[i][j] += eat[i][j]  


for _ in range(K):
    spring()
    summer()
    autumn_winter()
    
# 결과를 담을 변수
result = 0  
for i in range(N):
    for j in range(N):
        # 각 좌표의 나무들의 개수
        result += len(trees[i][j])
# 결과 출력
print(result)