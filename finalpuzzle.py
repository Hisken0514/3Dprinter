import math
import sys
import matplotlib.pyplot as plt
import random
from random import randint
from collections import deque

filename = "finalpuzzle.stl"  #檔案名稱
# 定義迷宮的寬度和高度

maze_WIDTH  = 9 #最小7 
maze_HEIGHT = 9

inner_radius = 21.5
outer_radius = 25
#window puzzle
col = 3
row = 3
#n夾板數量
nwall = 5
# 設定遞歸深度限制
sys.setrecursionlimit(maze_WIDTH * maze_HEIGHT)

def generate_cube_stl():
    #_generate_cylinder_stl(外半徑,內半徑,高度,位移量)
    with open(filename, 'w') as f:
        f.write("solid cubes\n")
            #   圓柱迷宮
        mazepuzzle(maze_WIDTH,maze_HEIGHT,inner_radius,outer_radius)
            #   多板子puzzle + n夾板
        #wallrandom(nwall)
            #   外框拼圖
        #framepuzzle(col,row)    
            #   其他部件
        #multcube()

        f.write("endsolid cubes\n")

# 生成立方體
def _generate_cuboid_stl(lwh,angle,origin):
    x, y, z = origin
    length, width, height = lwh
    stl_part = ""
    angle = (2 * math.pi * angle / 360) #角度
    
    # 底面 因為他只能生成三角向量 所以每個面都要用兩個三角形相疊 所以下面有12組相似的結構
    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    # Top 
    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    # Left 
    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    # Right 
    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    # Front 
    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) - width * math.sin(angle)} {y - width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    # Back 
    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z - height}\n"
    stl_part += f"      vertex {x + length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) - length * math.sin(angle)} {z + height}\n"
    stl_part += f"      vertex {x - length * math.cos(angle) + width * math.sin(angle)} {y + width * math.cos(angle) + length * math.sin(angle)} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"
    
    return stl_part
#生成空洞
def _generate_cuboid_hole_stl(lwh, origin):
    x, y, z = origin
    length, width, height = lwh
    stl_part = ""

    # 底面 (Z方向法线向下)
    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 上表面 (Z方向法线向上)
    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 左面 (X方向法线向左)
    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 右面 (X方向法线向右)
    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 前面 (Y方向法线向前)
    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 后面 (Y方向法线向后)
    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    return stl_part

# 初始化訪問狀態列表
def initVisitedList():
    visited = []
    for y in range(maze_HEIGHT):
        line = []
        for x in range(maze_WIDTH):
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
    for x in range(maze_WIDTH):
        for y in range(maze_HEIGHT):
            cellEdges = get_edges(x, y)
            for edge in cellEdges:
                edges.add(edge)
    return edges

# 檢查位置是否合法
def isValidPosition(x, y):
    if x < 0 or x >= maze_WIDTH:
        return False
    elif y < 0 or y >= maze_HEIGHT:
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


 # 生成圓柱體(含空心部分)       
#圓柱生成(ran角度,outer外半徑,inner內半徑,height高度,origin位移量)
def _generate_cylinder_stl1(ran,outer_radius, inner_radius, height, origin=(0,0,0)):
    x, y, z = origin
    stl_part = ""
    segments = 360
    
    for i in range(segments):
        if (i - 1 < (ran + 1) * 360 / maze_WIDTH and i + 1 > ran * 360 / maze_WIDTH ) or ran == maze_WIDTH:
            angle1 = (math.pi / segments) * i       #角度1
            angle2 = (math.pi / segments) * (i + 1) #角度2

            #外部
            stl_part += "  facet normal {nx1} {ny1} 0.0\n".format(nx1=math.cos((angle1 + angle2) / 2), ny1=math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle1)} {y + outer_radius * math.sin(angle1)} {z}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle2)} {y + outer_radius * math.sin(angle2)} {z}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle2)} {y + outer_radius * math.sin(angle2)} {z + height}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"

            stl_part += "  facet normal {nx2} {ny2} 0.0\n".format(nx2=math.cos((angle1 + angle2) / 2), ny2=math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle1)} {y + outer_radius * math.sin(angle1)} {z}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle2)} {y + outer_radius * math.sin(angle2)} {z + height}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle1)} {y + outer_radius * math.sin(angle1)} {z + height}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"

            #內部
            stl_part += "  facet normal {nx3} {ny3} 0.0\n".format(nx3=-math.cos((angle1 + angle2) / 2), ny3=-math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z + height}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"

            stl_part += "  facet normal {nx4} {ny4} 0.0\n".format(nx4=-math.cos((angle1 + angle2) / 2), ny4=-math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z + height}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z + height}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"
        else:
            continue
        
    return stl_part
def _generate_cylinder_stl2(ran,outer_radius, inner_radius, height, origin=(0,0,0)):
    x, y, z = origin
    stl_part = ""
    segments = 360
    
    for i in range(segments):
        if (i - 1 < (ran + 1) * 360 / maze_WIDTH and i + 1 > ran * 360 / maze_WIDTH ) or ran == maze_WIDTH:
            angle1 = (math.pi / segments) * (360 + i)       #角度1
            angle2 = (math.pi / segments) * (360 + i + 1)   #角度2

            #外部
            stl_part += "  facet normal {nx1} {ny1} 0.0\n".format(nx1=math.cos((angle1 + angle2) / 2), ny1=math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle1)} {y + outer_radius * math.sin(angle1)} {z}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle2)} {y + outer_radius * math.sin(angle2)} {z}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle2)} {y + outer_radius * math.sin(angle2)} {z + height}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"

            stl_part += "  facet normal {nx2} {ny2} 0.0\n".format(nx2=math.cos((angle1 + angle2) / 2), ny2=math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle1)} {y + outer_radius * math.sin(angle1)} {z}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle2)} {y + outer_radius * math.sin(angle2)} {z + height}\n"
            stl_part += f"      vertex {x + outer_radius * math.cos(angle1)} {y + outer_radius * math.sin(angle1)} {z + height}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"

            #內部
            stl_part += "  facet normal {nx3} {ny3} 0.0\n".format(nx3=-math.cos((angle1 + angle2) / 2), ny3=-math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z + height}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"

            stl_part += "  facet normal {nx4} {ny4} 0.0\n".format(nx4=-math.cos((angle1 + angle2) / 2), ny4=-math.sin((angle1 + angle2) / 2))
            stl_part += "    outer loop\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z + height}\n"
            stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z + height}\n"
            stl_part += "    endloop\n"
            stl_part += "  endfacet\n"
        else:
            continue
        
    return stl_part
# 生成圓孔
def _generate_cylindrical_hole_stl(inner_radius, height, origin=(0,0,0)):
    x, y, z = origin
    stl_part = ""
    segments = 64   #表示圓柱外表被分割為幾個平面
    
    #設定圓柱外表每個面的偏轉角度
    for i in range(segments):
        angle1 = (2 * math.pi / segments) * i       #角度1
        angle2 = (2 * math.pi / segments) * (i + 1) #角度2
        
        #內部
        stl_part += "  facet normal {nx3} {ny3} 0.0\n".format(nx3=-math.cos((angle1 + angle2) / 2), ny3=-math.sin((angle1 + angle2) / 2))
        stl_part += "    outer loop\n"
        stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z}\n"
        stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z + height}\n"
        stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z}\n"
        stl_part += "    endloop\n"
        stl_part += "  endfacet\n"

        stl_part += "  facet normal {nx4} {ny4} 0.0\n".format(nx4=-math.cos((angle1 + angle2) / 2), ny4=-math.sin((angle1 + angle2) / 2))
        stl_part += "    outer loop\n"
        stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z}\n"
        stl_part += f"      vertex {x + inner_radius * math.cos(angle1)} {y + inner_radius * math.sin(angle1)} {z + height}\n"
        stl_part += f"      vertex {x + inner_radius * math.cos(angle2)} {y + inner_radius * math.sin(angle2)} {z + height}\n"
        stl_part += "    endloop\n"
        stl_part += "  endfacet\n"

    return stl_part
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

#迷宮puzzle
def mazepuzzle(maze_WIDTH,maze_HEIGHT,inner_radius,outer_radius):
    angle = 180 / maze_WIDTH
    with open(filename, 'w') as f:
    #圓柱外殼
        f.write(_generate_cylinder_stl1(maze_WIDTH,outer_radius,inner_radius,maze_HEIGHT * 10 + 5,(100,100,0)))
        f.write(_generate_cylinder_stl2(maze_WIDTH,outer_radius,inner_radius,maze_HEIGHT * 10 + 5,(100,100,0)))        
        i = 0
        while i < len(edgeList):
            edge = edgeList[i]
            if edge[0] == edge[2]:      #內部迷宮 垂直牆壁生成
                if edge[0] == maze_WIDTH:
                    i += 1
                    continue
                f.write(_generate_cuboid_stl((1, 1, 5), edge[0] * -angle, (-20.8 * math.cos(-2 * (edge[0] * angle + 183) / 360 * math.pi) + 100, 20.8 * math.sin(-2 *  (edge[0] * angle + 183) / 360 * math.pi) + 100, edge[1] * 10 + 10)))
                f.write(_generate_cuboid_stl((1, 1, 5), edge[0] * -angle, (20.8 * math.cos(-2 *  (edge[0] * angle + 183) / 360 * math.pi) + 100, -20.8 * math.sin(-2 *  (edge[0] * angle + 183) / 360 * math.pi) + 100, edge[1] * 10 + 10)))
            else:                       #內部迷宮 水平牆壁生成
                f.write(_generate_cylinder_stl1(edge[0],inner_radius,20,5,(0 + 100,0 + 100,edge[1] * 10)))
                f.write(_generate_cylinder_stl2(edge[0],inner_radius,20,5,(0 + 100,0 + 100,edge[1] * 10)))
            i += 1
def wallrandom(nwall):
    #三片板子牆壁參數(長 高 寬 洞大小)
    wall_WIDTH = 32
    wall_HEIGHT = 52.5
    wall_THICK = 3
    wallhole = 5

    #挖洞隨機變數
    wall1 = random.randint(-25, 25)
    wall2 = random.randint(-25, 25)
    wall3 = random.randint(-25, 25)

    while (wall1 > wall2 + 10) and (wall1 < wall2 -10) and (wall2 > wall3 + 10) and (wall2 < wall3 - 10):
        wall1 = random.randint(-25, 25)
        wall2 = random.randint(-25, 25)
        wall3 = random.randint(-25, 25)
    with open(filename, 'a') as f:
        for i in range(nwall):
            if(i % 2 == 0):
                f.write(_generate_cuboid_stl((1.75, 26, 17.5), 0,(3.5*i +100+40, 0-100, 17.5)))

                f.write(_generate_cuboid_stl((wall_WIDTH / 2,wall_THICK / 2,(wall_HEIGHT-15) / 2),0,(0+100,10*i -100,-7.5 + 26.25)))
                f.write(_generate_cuboid_hole_stl((wallhole,wall_THICK,wallhole),(wall2 / 2+100,10*i-100,7.5 / 2 + 26.25)))
            if(i % 2 == 1):
                f.write(_generate_cuboid_stl((1.75, 26, 10), 0, (3.5*i +100+40,-100,10)))

                f.write(_generate_cuboid_stl((wall_WIDTH / 2,wall_THICK / 2,wall_HEIGHT / 2),0,(100,-100+10*i,0 + 26.25)))
                f.write(_generate_cuboid_hole_stl((wallhole,wall_THICK,wallhole),(wall1 / 2+100,0-100+10*i,37.5 / 2 + 26.25)))
#外殼+底板
def finalshell():
    with open(filename, 'a') as f:
        f.write(_generate_cuboid_stl(((76+((nwall - 3) * 3.5))/2, 70/2, 12/2), 0,(-80-((nwall - 3) * 3.5/2), -100, 6)))
        f.write(_generate_cylindrical_hole_stl(25.5, 12, (-80, -100, 0)))
        f.write(_generate_cuboid_stl((71/2, 9/2, 66/2), 0, (2.5-80, 30.5-100, 45)))
        f.write(_generate_cuboid_stl((9/2, 52/2, 66/2), 0, (33.5-80, 0-100, 45)))
        f.write(_generate_cuboid_stl((5/2, 9/2, 66/2), 0, (35.5-80, -30.5-100, 45)))
        f.write(_generate_cuboid_hole_stl((4.0, 4.0, 12), (22.5-80, -31.25-100, 0)))
        
        f.write(_generate_cuboid_hole_stl((10.0+((nwall - 3) * 3.5/2), 52, 7), (-30.6-80-((nwall - 3) * 3.5/2), 0-100, 5)))

        f.write(_generate_cuboid_hole_stl((16.0+((nwall - 3) * 3.5/2), 5.0, 5.0), (-31.4-80-((nwall - 3) * 3.5/2), 0-100, 2.5)))

        f.write(_generate_cuboid_stl(((76+((nwall - 3) * 3.5)) / 2, 70 / 2, 12 / 2), 0, (-80-((nwall - 3) * 3.5/2), 0, 6)))
        f.write(_generate_cylindrical_hole_stl(25, 4,(-80, 0, 8))) # 圓孔在頂部中心

def framepuzzle(col,row):
    with open(filename, 'a') as f:
    # 框的參數
        outer_size = 66.0 / 2  # 外部立方體的長寬
        inner_size = 61.0 / 2  # 內部挖掉的立方體的長寬
        frame_thickness = (outer_size - inner_size) / 2  # 框的厚度
        frame_height = 9 / 2 # 框的高度
        # 生成frame大小
        f.write(_generate_cuboid_stl((outer_size, frame_thickness, frame_height), 0,(0+100,0,4.5)))
        f.write(_generate_cuboid_stl((outer_size, frame_thickness, frame_height), 90,(outer_size - frame_thickness+100,outer_size - frame_thickness,4.5)))
        f.write(_generate_cuboid_stl((outer_size, frame_thickness, frame_height), 0,(0+100,2*(outer_size - frame_thickness),4.5)))
        f.write(_generate_cuboid_stl((outer_size, frame_thickness, frame_height), 90,(-(outer_size - frame_thickness)+100,(outer_size - frame_thickness),4.5)))

        #內部框線
        for i in range(col + 1):
            f.write(_generate_cuboid_stl((inner_size + 2,1,0.5), 0,(0+100,1.25+(inner_size / col * 2*i),0.5)))
        for i in range(row + 1):
            f.write(_generate_cuboid_stl((inner_size + 2,1,0.5), 90,(1.25+(inner_size / row * 2*i)+100-31.5,31.5,0.5)))
            
        #內部板塊   
        for i in range(row*col):
            f.write(_generate_cuboid_stl((inner_size / col,6 / 2,inner_size / row), 0,(0+20,i*10-100,0+7)))
            if(i < col):
                f.write(_generate_cuboid_hole_stl((4, 4,inner_size / row), (0+20,i*10-100,-7.5+7)))
        
def multcube():
    with open(filename, 'a') as f:
            #   底面跟長方體混和
        f.write(_generate_cuboid_stl((61 / 2,61 / 2,2 / 2), 0,(0,0+100,0+0.5)))
        f.write(_generate_cuboid_stl((4.5 / 2,39 / 2,4.5 / 2), 0,(40,0+100,0+1.5)))
        f.write(_generate_cuboid_stl((3 / 2,15 / 2,3 / 2), 0,(50,0+100,0+1)))

        f.write(_generate_cuboid_stl((2 / 2,70 / 2,66 / 2), 0,(0-((nwall - 3) * 3.5),0+30,0+32)))
        f.write(_generate_cuboid_stl(((2 + ((nwall - 3) * 3.5)) / 2,9 / 2,66 / 2), 0,(2-((nwall - 3) * 3.5/2),0+30.5+30,0+32)))
        f.write(_generate_cuboid_stl(((2 + ((nwall - 3) * 3.5)) / 2,9 / 2,66 / 2), 0,(2-((nwall - 3) * 3.5/2),0-30.5+30,0+32)))
        #   外殼+底板
        finalshell()

edgeList = initEdgeList()  # 初始化邊界列表
visited  = initVisitedList()  # 初始化訪問狀態列表-
DFS(0, 0, edgeList, visited)  # 從(0, 0)開始深度優先搜索
edgeList.remove((0, 0, 1, 0))  # 移除起點的邊界
edgeList.remove((maze_WIDTH-1, maze_HEIGHT, maze_WIDTH, maze_HEIGHT))  # 移除終點的邊界
for edge in edgeList:
    drawLine(edge[0], edge[1], edge[2], edge[3])  # 畫迷宮的邊界
# 將 edgeList 轉換為列表，並打印第一項
edgeList = list(edgeList)
generate_cube_stl()
start = (0, 0)
end = (maze_WIDTH - 1, maze_HEIGHT - 1)
shortest_path_length = bfs_shortest_path(edgeList, start, end)
difficulty = judge_difficulty(shortest_path_length)
# 打印迷宮難度

print(f"最短路徑步數: {shortest_path_length}")
print(f"迷宮難度: {difficulty}")

print(f"STL 文件已生成：{filename}")
