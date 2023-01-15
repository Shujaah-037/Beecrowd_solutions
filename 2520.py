#The Last Analógimôn
def bfs(x, y, dist, grid, q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        curr = q.pop(0)
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            if nx >= 0 and nx < x and ny >= 0 and ny < y:
                if grid[nx][ny] == 2:
                    return dist[curr[0]][curr[1]] + 1
                if grid[nx][ny] == 0:
                    dist[nx][ny] = dist[curr[0]][curr[1]] + 1
                    grid[nx][ny] = 1
                    q.append((nx, ny))
    return -1

while True:
    try:
        x, y = map(int, input().split())
        grid = []
        for i in range(x):
            row = list(map(int, input().split()))
            grid.append(row)
        dist = [[0 for i in range(y)] for j in range(x)]
        start = None
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break
        q = [start]
        print(bfs(x, y, dist, grid, q))
    except EOFError:
        break

        #Code provided with the help of AI baba.
