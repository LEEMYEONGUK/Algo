# 스타트링크

# 총 F 층, 스타트 링크는 G층, 현재위치 S층
# 버튼 2개 U층 위 혹은 D층 아래
# 못 갈때 use the stairs

from collections import deque


def bfs(x):
    visited[x] = 1
    q = deque([x])

    while q:
        i = q.popleft()
        # 스타트 링크에 도달하였을 때 함수 종료
        if i == G:
            return
        for j in [i + U, i - D]:
            # 이동한 층이 총 건물의 층수를 벗어나지 않으면서 방문하지 않은 층일때
            if 1 <= j < F + 1 and visited[j] == 0:
                q.append(j)
                visited[j] = visited[i] + 1

# 입력 받기
F, S, G, U, D = map(int, input().split())

# 방문 체크용 리스트
visited = [0] * (F + 1)

# 함수 실행
bfs(S)

# 만약 스타트 링크에 도착할 수 있다면 누르는 버튼 수의 최솟값 출력
if visited[G]:
    print(visited[G] - 1)
# 엘베로 못갈 경우 문구 출력
else:
    print("use the stairs")