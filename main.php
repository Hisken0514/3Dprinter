<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>機關盒產生器</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('C:/Users/User/Desktop/1.png'); /* 替換為您的圖片路徑 */
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: rgba(255, 255, 255, 0.8); /* 背景加上透明度 */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }

        .container h1 {
            text-align: center;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        .generate-button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }

        .generate-button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>機關盒產生器</h1>
    <form method="POST" action="">
        <div class="form-group">
            <label for="size">尺寸大小 (mm):</label>
            <input type="number" id="size" name="size" min="70" placeholder="輸入尺寸大小 (最小70mm)">
        </div>

        <div class="form-group">
            <label for="boardCount">夾板的片數:</label>
            <input type="number" id="boardCount" name="boardCount" min="1" max="20" placeholder="輸入夾板片數">
        </div>

        <div class="form-group">
            <label for="cylinderMaze">圓柱迷宮 (width,height):</label>
            <input type="text" id="cylinderMaze" name="cylinderMaze" placeholder="例如：100x200">
        </div>

        <div class="form-group">
            <label for="windowPuzzle">Window Puzzle大小 (col , row):</label>
            <input type="text" id="windowPuzzle" name="windowPuzzle" placeholder="例如：10x10">
        </div>

        <button type="submit" class="generate-button">產生迷宮</button>
    </form>
</div>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 獲取用戶輸入
    $size = floatval($_POST["size"]);
    $boardCount = intval($_POST["boardCount"]);
    $cylinderMaze = array_map('intval', explode('x', $_POST["cylinderMaze"]));
    $windowPuzzle = array_map('intval', explode('x', $_POST["windowPuzzle"]));
    
    // 檢查輸入是否有效
    if (is_nan($size) || is_nan($boardCount) || count($cylinderMaze) !== 2 || count($windowPuzzle) !== 2) {
        echo "<script>alert('請填寫所有必填欄位並確保格式正確。');</script>";
    } else {
        // 連接到資料庫
        $conn = new mysqli("localhost", "web", "1234", "CS_topics");
        
        // 檢查連接
        if ($conn->connect_error) {
            die("資料庫連接失敗: " . $conn->connect_error);
        }
        
        // 準備 SQL 語句
        $stmt = $conn->prepare("INSERT INTO `mechanism box` (box_size, number_of_splints, width, height, col, row) VALUES (?, ?, ?, ?, ?, ?)");
        $stmt->bind_param("diiiii", $size, $boardCount, $cylinderMaze[0], $cylinderMaze[1], $windowPuzzle[0], $windowPuzzle[1]);
        
        // 執行語句
        if ($stmt->execute()) {
            echo "<script>alert('資料已成功儲存至資料庫。');</script>";
        } else {
            echo "<script>alert('儲存資料時發生錯誤: " . $stmt->error . "');</script>";
        }
        
        // 關閉連接
        $stmt->close();
        $conn->close();

        // 生成 STL 文件內容
        $stlContent = generateSTLContent($size, $boardCount, $cylinderMaze, $windowPuzzle);
        
        // 下載 STL 文件
        downloadSTLFile($stlContent, 'maze.stl');
    }
}

function generateSTLContent($size, $boardCount, $cylinderMaze, $windowPuzzle) {
    $stlContent = "solid maze\n";

    $cylinderWidth = $cylinderMaze[0];
    $cylinderHeight = $cylinderMaze[1];
    $windowCols = $windowPuzzle[0];
    $windowRows = $windowPuzzle[1];

    // 生成 STL 文件的內容
    $cuboidLength = 15;
    $cuboidWidth = 6;
    $cuboidHeight = 15;

    for ($i = 0; $i < $boardCount; $i++) {
        $xOffset = $i * ($cuboidLength + 5); // 每個 cuboid 之間的間隔為 5cm
        $zOffset = 0; // 假設所有 cuboids 在同一個平面上

        $stlContent .= generateCuboidSTL($xOffset, $zOffset, $cuboidLength, $cuboidWidth, $cuboidHeight);
    }
    
    $stlContent .= "endsolid maze";
    return $stlContent;
}

function generateCuboidSTL($xOffset, $zOffset, $length, $width, $height) {
    $vertices = [
        [$xOffset, $zOffset, 0],
        [$xOffset + $length, $zOffset, 0],
        [$xOffset + $length, $zOffset + $width, 0],
        [$xOffset, $zOffset + $width, 0],
        [$xOffset, $zOffset, $height],
        [$xOffset + $length, $zOffset, $height],
        [$xOffset + $length, $zOffset + $width, $height],
        [$xOffset, $zOffset + $width, $height],
    ];

    $faces = [
        [0, 1, 2, 3], // 底面
        [4, 5, 6, 7], // 頂面
        [0, 1, 5, 4], // 前面
        [1, 2, 6, 5], // 右面
        [2, 3, 7, 6], // 後面
        [3, 0, 4, 7], // 左面
    ];

    $stl = '';
    foreach ($faces as $face) {
        list($v0, $v1, $v2) = $face;
        $stl .= "facet normal 0 0 1\nouter loop\n";
        $stl .= "vertex {$vertices[$v0][0]} {$vertices[$v0][1]} {$vertices[$v0][2]}\n";
        $stl .= "vertex {$vertices[$v1][0]} {$vertices[$v1][1]} {$vertices[$v1][2]}\n";
        $stl .= "vertex {$vertices[$v2][0]} {$vertices[$v2][1]} {$vertices[$v2][2]}\n";
        $stl .= "endloop\nendfacet\n";
    }

    return $stl;
}

function downloadSTLFile($content, $filename) {
    header('Content-Type: application/octet-stream');
    header('Content-Disposition: attachment; filename="' . $filename . '"');
    echo $content;
    exit;
}
?>

</body>
</html>
