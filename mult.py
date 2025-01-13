import math
import sys
import matplotlib.pyplot as plt
import random
from random import randint
from collections import deque

filename = "multpuzzle.stl"  #檔案名稱
nwall = 5

def generate_cube_stl():
    #_generate_cylinder_stl(外半徑,內半徑,高度,位移量)
    with open(filename, 'w') as f:
        f.write("solid cubes\n")
            #   圓柱迷宮
        #mazepuzzle(maze_WIDTH,maze_HEIGHT,inner_radius,outer_radius)
            #   多板子puzzle + n夾板
        #wallrandom(nwall)
            #   外框拼圖
        #framepuzzle(col,row)    
            #   其他部件
        multcube()

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

generate_cube_stl()

print(f"STL 文件已生成：{filename}")
