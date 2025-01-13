import math

def generate_cube_stl(filename):
    #_generate_cylinder_stl(外半徑,內半徑,高度,位移量)
    with open(filename, 'w') as f:
        f.write("solid cubes\n")
        i = 0
        f.write(_generate_cylinder_stl(20,30,25,50,(0,0,-50)))
        f.write(_generate_cylinder_stl(1,25,24,5,(0,0,-30)))

        

        f.write(_generate_cuboid_stl((1,1,5),i,(24*math.cos(-2*i/360*math.pi),24*math.sin(-2*i/360*math.pi),-45)))

        f.write("endsolid cubes\n")
        
 # 生成圓柱體(含空心部分)       
def _generate_cylinder_stl(ran,outer_radius, inner_radius, height, origin=(0,0,0)):
    x, y, z = origin
    stl_part = ""
    segments = 360
    
    for i in range(segments):
        if (i < (ran + 1) * 18 and i > ran * 18 ) or ran == 20:
            angle1 = ( 2 * math.pi / segments) * i       #角度1
            angle2 = ( 2 * math.pi / segments) * (i + 1) #角度2

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


output_filename = "testpuzzle.stl"  #檔案名稱

generate_cube_stl(output_filename)

print(f"STL 文件已生成：{output_filename}")
