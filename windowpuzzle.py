import math
import sys
import matplotlib.pyplot as plt
import random
from random import randint
from collections import deque
import mysql.connector

# 接收來自 PHP 的 id
if len(sys.argv) < 2:
    print("需要提供ID")
    sys.exit()

record_id = sys.argv[1]
print(f"接收到的ID: {record_id}")  # 檢查是否正確接收到 ID

def save_stl_to_db(filename, record_id):
    try:
        # 建立與資料庫的連接
        cnx = mysql.connector.connect(
            host="localhost",
            user="web",
            password="1234",
            database="cs_topics"
        )
        cursor = cnx.cursor()

        # 讀取 STL 文件內容
        with open(filename, 'rb') as file:
            stl_data = file.read()

        # 插入 STL 文件存儲到指定 ID 的行
        sql = "UPDATE `windowpuzzle` SET generate = %s WHERE id = %s"
        cursor.execute(sql, (stl_data, record_id))

        # 提交更改
        cnx.commit()
        print(f"STL 檔案已成功儲存到 ID {record_id} 的資料庫。")

    except mysql.connector.Error as err:
        print(f"資料庫錯誤: {err}")
    except Exception as e:
        print(f"其他錯誤: {e}")
    finally:
        # 確保連接被關閉
        cursor.close()
        cnx.close()

def fetch_maze_data_from_db(stl_id):
    try:
        # 建立與資料庫的連接
        cnx = mysql.connector.connect(
            host="localhost",
            user="web",
            password="1234",
            database="cs_topics"

        )
        cursor = cnx.cursor()

        # 查詢 col, row 等數據
        query = "SELECT col, row FROM `windowpuzzle` WHERE id = %s"
        cursor.execute(query, (stl_id,))

        # 取得結果
        result = cursor.fetchone()
        if result:
            # 賦值資料庫的值到對應的變數
            col = result[0]     # 資料庫的 col
            row = result[1]     # 資料庫的 row

            # 印出抓取後的變數值
            print(f"抓取的數據: col={col}, row={row}")

            # 返回抓取到的數據
            return col, row

        else:
            print("找不到該 ID 的數據。")
            return None

    except mysql.connector.Error as err:
        print(f"資料庫錯誤: {err}")
        return None
    except Exception as e:
        print(f"其他錯誤: {e}")
        return None
    finally:
        cursor.close()
        cnx.close()

def main():
    result = fetch_maze_data_from_db(record_id)

    if result is not None:
        col, row = result

        # 使用這些抓取到的數據
        print(f"使用數據: col={col}, row={row}")
        
    else:
        print("無法初始化邊界列表，因為抓取資料失敗。")

    filename = "windowpuzzle.stl"  #檔案名稱

    #window puzzle
    #col = 3
    #row = 3

    def generate_cube_stl():
        #_generate_cylinder_stl(外半徑,內半徑,高度,位移量)
        with open(filename, 'w') as f:
            f.write("solid cubes\n")
            windowpuzzle(col,row)    
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

    def windowpuzzle(col,row):
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
            
    generate_cube_stl()
    print(f"STL 文件已生成：{filename}")
    
    ##資料庫
    #將STL檔存入資料庫(從php中接收到的該筆id)
    save_stl_to_db(filename, record_id)


if __name__ == "__main__":
    main()