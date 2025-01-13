import math

# 建立STL檔
def generate_cuboid_with_hole_stl(filename, inner_radius, height, hole_origin):
    with open(filename, 'w') as f:
        f.write("solid cuboid_with_hole\n")
        
        # 立方體的STL描述
        lwh = (76, 70, 12)
        angle = 0
        origin = (0, 0, 0)
        f.write(_generate_cuboid_stl(lwh, angle, origin))
        f.write(_generate_cylindrical_hole_stl(inner_radius, height, hole_origin)) # 圓孔在指定位置

        # 生成附加的小立方體
        small_cuboids = [
            {'lwh': (71, 9, 66), 'origin': (2.5, 30.5, 39)},
            {'lwh': (9, 52, 66), 'origin': (33.5, 0, 39)},
            {'lwh': (5, 9, 66), 'origin': (35.5, -30.5, 39)},

        ]
        
        for cuboid in small_cuboids:
            f.write(_generate_cuboid_stl(cuboid['lwh'], 0, cuboid['origin']))

        # 在指定位置生成一个洞
        cuboids_hole = [
            {'lwh': (4.0, 4.0, 12), 'origin': (22.5, -31.25, -6)},
            {'lwh': (10.6, 52, 7.5), 'origin': (-30.6, 0, -0.5)},
            {'lwh': (13.0, 5.0, 5.0), 'origin': (-31.4, 0, -3.5)},

        ]
        
        for cuboid in cuboids_hole:
            f.write(_generate_cuboid_hole_stl(cuboid['lwh'], cuboid['origin']))
  

        f.write("endsolid cuboid_with_hole\n")

# 生成立方體
def _generate_cuboid_stl(lwh, angle, origin):
    x, y, z = origin
    length, width, height = lwh
    stl_part = ""
    angle = (2 * math.pi * angle / 360)  # 角度

    # 底面
    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 上表面
    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 左面
    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 右面
    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 前面
    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 後面
    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z - height / 2}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height / 2}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

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

# 生成內部小立方體(方形孔)
def _generate_cuboid_hole_stl(lwh, origin):
    x, y, z = origin
    length, width, height = lwh
    stl_part = ""

    # 底面
    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 0.0 -1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 上表面
    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 0.0 1.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 左面
    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal -1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 右面
    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 1.0 0.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 前面
    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 -1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z}\n"
    stl_part += f"      vertex {x - length / 2} {y - width / 2} {z + height}\n"
    stl_part += f"      vertex {x + length / 2} {y - width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    # 後面
    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    stl_part += "  facet normal 0.0 1.0 0.0\n"
    stl_part += "    outer loop\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z}\n"
    stl_part += f"      vertex {x + length / 2} {y + width / 2} {z + height}\n"
    stl_part += f"      vertex {x - length / 2} {y + width / 2} {z + height}\n"
    stl_part += "    endloop\n"
    stl_part += "  endfacet\n"

    return stl_part

# 設定挖空立方體內部的尺寸
#inner_lwh = (4.0, 4.0, 12) # 內部方洞尺寸
#hole_cube_origin = (22.5, -31.25, -6) # 方洞的起始位置（底面與外立方體的底面對齊）

# 生成 STL 檔案
output_filename = "cuboid_with_hole.stl"  #檔案名稱

# 在這裡設置圓孔的生成座標位置和高度
hole_origin = (0, 0, -6)
hole_height = 12
generate_cuboid_with_hole_stl(output_filename, 25.5, hole_height, hole_origin)

print(f"STL 文件已生成：{output_filename}")
