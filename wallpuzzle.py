import math
import sys
import matplotlib.pyplot as plt
import random
from random import randint
from collections import deque

filename = "wallpuzzle.stl"  #檔案名稱
#n夾板數量
nwall = 5

def generate_cube_stl():
    #_generate_cylinder_stl(外半徑,內半徑,高度,位移量)
    with open(filename, 'w') as f:
        f.write("solid cubes\n")

        wallrandom(nwall)

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


 # 生成圓柱體(含空心部分)       
#圓柱生成(ran角度,outer外半徑,inner內半徑,height高度,origin位移量)

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

generate_cube_stl()

print(f"STL 文件已生成：{filename}")
