import sys
import matplotlib.pyplot as plt
from random import randint
from collections import deque

# 定義迷宮的寬度和高度
WIDTH  = 7
HEIGHT = 9
# 設定遞歸深度限制
sys.setrecursionlimit(WIDTH * HEIGHT)

# 初始化訪問狀態列表
def initVisitedList():
    visited = []
    for y in range(HEIGHT):
        line = []
        for x in range(WIDTH):
            line.append(False)
        visited.append(line)
    return visited

# 畫一條線
def drawLine(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], color="black")

# 移除一條線
def removeLine(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2], color="white")

# 獲取單元格的邊界
def get_edges(x, y):
    result = []
    result.append((x, y, x, y+1))
    result.append((x+1, y, x+1, y+1))
    result.append((x, y, x+1, y))
    result.append((x, y+1, x+1, y+1))
    return result

# 畫一個單元格
def drawCell(x, y):
    edges = get_edges(x, y)
    for item in edges:
        drawLine(item[0], item[1], item[2], item[3])

# 獲取兩個單元格的公共邊界
def getCommonEdge(cell1_x, cell1_y, cell2_x, cell2_y):
    edges1 = get_edges(cell1_x, cell1_y)
    edges2 = set(get_edges(cell2_x, cell2_y))
    for edge in edges1:
        if edge in edges2:
            return edge
    return None

# 初始化邊界列表
def initEdgeList():
    edges = set()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cellEdges = get_edges(x, y)
            for edge in cellEdges:
                edges.add(edge)
    return edges

# 檢查位置是否合法
def isValidPosition(x, y):
    if x < 0 or x >= WIDTH:
        return False
    elif y < 0 or y >= HEIGHT:
        return False
    else:
        return True

# 隨機打亂方向向量
def shuffle(dX, dY):
    for t in range(4):
        i = randint(0, 3)
        j = randint(0, 3)
        dX[i], dX[j] = dX[j], dX[i]
        dY[i], dY[j] = dY[j], dY[i]

# 深度優先搜索算法
def DFS(X, Y, edgeList, visited):
    dX = [0,  0, -1, 1]
    dY = [-1, 1, 0,  0]
    shuffle(dX, dY)
    for i in range(len(dX)):
        nextX = X + dX[i]
        nextY = Y + dY[i]
        if isValidPosition(nextX, nextY):
            if not visited[nextY][nextX]:
                visited[nextY][nextX] = True
                commonEdge = getCommonEdge(X, Y, nextX, nextY)
                if commonEdge in edgeList:
                    edgeList.remove(commonEdge)
                DFS(nextX, nextY, edgeList, visited)

# 使用BFS計算最短路徑的步數
def bfs_shortest_path(maze, start, end):
    queue = deque([(start, 0)])  # (位置, 距離)
    visited = set([start])
    
    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) == end:
            return dist
        
        # 四個方向
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if isValidPosition(nx, ny) and (x, y, nx, ny) not in maze and (nx, ny, x, y) not in maze:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), dist + 1))
    
    return float('inf')  # 如果沒有路徑返回無限大

# 判斷迷宮難易度
def judge_difficulty(shortest_path_length):
    if shortest_path_length < 20:
        return "容易"
    elif 20 <= shortest_path_length <= 40:
        return "中等"
    else:
        return "困難"

plt.axis('equal')
plt.title('Maze')
edgeList = initEdgeList()  # 初始化邊界列表
visited  = initVisitedList()  # 初始化訪問狀態列表
DFS(0, 0, edgeList, visited)  # 從(0, 0)開始深度優先搜索
edgeList.remove((0, 0, 1, 0))  # 移除起點的邊界
edgeList.remove((WIDTH-1, HEIGHT, WIDTH, HEIGHT))  # 移除終點的邊界
for edge in edgeList:
    drawLine(edge[0], edge[1], edge[2], edge[3])  # 畫迷宮的邊界

# 計算最短路徑並判斷難度
start = (0, 0)
end = (WIDTH - 1, HEIGHT - 1)
shortest_path_length = bfs_shortest_path(edgeList, start, end)
difficulty = judge_difficulty(shortest_path_length)

# 打印迷宮難度
print(f"最短路徑步數: {shortest_path_length}")
print(f"迷宮難度: {difficulty}")

plt.show()
print(edgeList)