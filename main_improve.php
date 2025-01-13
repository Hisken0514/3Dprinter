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
            background-color: rgba(255, 255, 255, 0.8); /* 背景透明 */
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

        /* 彈窗樣式 */
        .popup {
            display: none;
            position: fixed;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            width: 60%; /* 調整寬度，讓彈窗大小適中 */
            height: auto; /* 高度自動適應內容 */
            max-height: 80%; /* 設定最大高度，避免彈窗太大 */
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
            overflow-y: auto; /* 若內容過多，則允許滾動 */
        }
        
        .popup h2 {
            margin-bottom: 10px;
        }

        .popup-buttons {
            display: flex;
            justify-content: space-between;
        }
         
        .popup-buttons img {
            width: 80px; /* 設定圖片的寬度 */
            height: 80px; /* 設定圖片的高度 */
            object-fit: contain; /* 使用 contain 避免圖片變形，會在圖片大小不一時保持原比例 */
            margin: 10px; /* 可選：增加圖片周圍的間距 */
        }

        .popup-buttons button {
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            width: 45%;
            height: auto; /* 高度自適應文字 */
            font-size: 14px; /* 調整文字大小 */
            text-align: center; /* 文字置中 */
            word-wrap: break-word; /* 避免過長文字溢出 */
        }

        .cancel-button {
            background-color: #f44336;
            color: white;
        }

        .confirm-button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>

<!--使用者輸入參數-->
<div class="container">
    <h1>自訂機關盒</h1>
    <form id="mazeForm" method="POST" action="">
        <div class="form-group">
            <label for="difficulty">難易度設置：</label>
            <select id="difficulty" name="difficulty">
                <option value="簡易">簡易</option>
                <option value="中等">中等</option>
                <option value="困難">困難</option>
            </select>
        </div>

        <div class="form-group">
            <label for="boardCount">滑板的片數：</label>
            <select id="boardCount" name="boardCount" >
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
                <option value="6">6</option>
            </select>
        </div>

        <div class="form-group">
            <label for="cylinderMaze">圓柱迷宮 (迷宮水平牆數x迷宮垂直牆數)：</label>
            <select id="cylinderMaze" name="cylinderMaze">
                <option value="8, 10">8 x 10</option>
                <option value="8, 11">8 x 11</option>
                <option value="8, 12">8 x 12</option>
                <option value="8, 13">8 x 13</option>
                <option value="8, 14">8 x 14</option>
                <option value="8, 15">8 x 15</option>
                <option value="9, 10">9 x 10</option>
                <option value="9, 11">9 x 11</option>
                <option value="9, 12">9 x 12</option>
                <option value="9, 13">9 x 13</option>
                <option value="9, 14">9 x 14</option>
                <option value="9, 15">9 x 15</option>
                <option value="10, 10">10 x 10</option>
                <option value="10, 11">10 x 11</option>
                <option value="10, 12">10 x 12</option>
                <option value="10, 13">10 x 13</option>
                <option value="10, 14">10 x 14</option>
                <option value="10, 15">10 x 15</option>
                <option value="11, 10">11 x 10</option>
                <option value="11, 11">11 x 11</option>
                <option value="11, 12">11 x 12</option>
                <option value="11, 13">11 x 13</option>
                <option value="11, 14">11 x 14</option>
                <option value="11, 15">11 x 15</option>
                
            </select>
        </div>

        <div class="form-group">
            <label for="windowPuzzle">移動拼圖大小 (高 x 寬)：</label>
            <select id="windowPuzzle" name="windowPuzzle" >
                <option value="3, 3">3 x 3</option>
                <option value="3, 4">3 x 4</option>
                <option value="4, 3">4 x 3</option>
                <option value="4, 4">4 x 4</option>
            </select>
        </div>

        <!--產生迷宮按鈕-->
        <button type="button" class="generate-button" onclick="submitFormWithPopup(event)">產生迷宮</button>
    </form>
</div>

<!--將參數傳入資料庫--> 
<?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $conn = new mysqli("localhost", "web", "1234", "cs_topics");
        if ($conn->connect_error) {
            die("連接失敗: " . $conn->connect_error);
        }

        $difficulty = $_POST['difficulty'];
        $cylinderMaze = $_POST['cylinderMaze'];
        $boardCount = $_POST['boardCount'];
        $windowPuzzle = $_POST['windowPuzzle'];

        $success = true;

        #圓柱迷宮資料庫
        if (isset($_POST['cylinderMaze'])) {
            $cylinderMaze = explode(",", $_POST['cylinderMaze']); // 將選擇的值轉換為數組
            if (count($cylinderMaze) === 2) {
                $width = (int)trim($cylinderMaze[0]);  // 第一部分轉換為整數
                $height = (int)trim($cylinderMaze[1]); // 第二部分轉換為整數
            
                // 然後將 $width 和 $height 插入資料庫
                $stmt = $conn->prepare("INSERT INTO mazepuzzle (difficulty, width, height) VALUES (?, ?, ?)");
                $stmt->bind_param("sii", $difficulty, $width, $height);
                if ($stmt->execute()) {
                    $last_id1 = $conn->insert_id; // 獲取最後插入的ID
                    echo "參數已成功存入資料庫。ID 為: " . $last_id1;
                    echo "<br>選擇的機關為: " . $features;
                } else {
                    echo "存入資料庫時發生錯誤: " . $stmt->error;
                }
                $stmt->close();
            }
        }

        #滑板迷宮資料庫
        $stmt = $conn->prepare("INSERT INTO slide (count) VALUES (?)");
        $stmt->bind_param("s", $boardCount);
        if ($stmt->execute()) {
            $last_id2 = $conn->insert_id; // 獲取最後插入的ID
            echo "參數已成功存入資料庫。ID 為: " . $last_id2;
            echo "<br>選擇的機關為: " . $features;
        } else {
            echo "存入資料庫時發生錯誤: " . $stmt->error;
        }
        $stmt->close();

        #移動拼圖迷宮資料庫
        if (isset($_POST['windowPuzzle'])) {
            $windowPuzzle = explode(",", $_POST['windowPuzzle']); // 將選擇的值轉換為數組
            if (count($windowPuzzle) === 2) {
                $col = (int)trim($windowPuzzle[0]);  // 第一部分轉換為整數
                $row = (int)trim($windowPuzzle[1]); // 第二部分轉換為整數
            
                // 然後將 $col 和 $row 插入資料庫
                $stmt = $conn->prepare("INSERT INTO windowpuzzle (col, row) VALUES (?, ?)");
                $stmt->bind_param("ii", $col, $row);
                if ($stmt->execute()) {
                    $last_id3 = $conn->insert_id; // 獲取最後插入的ID
                    echo "參數已成功存入資料庫。ID 為: " . $last_id3;
                    echo "<br>選擇的機關為: " . $features;
                } else {
                    echo "存入資料庫時發生錯誤: " . $stmt->error;
                }
                $stmt->close();
            } 
        }

        // 執行 Python 程式，傳遞 ID
        $command1 = "python C:/xampp/htdocs/CS_project/mazepuzzle.py " . escapeshellarg($last_id1);
        $command2 = "python C:/xampp/htdocs/CS_project/slide.py " . escapeshellarg($last_id2);
        $command3 = "python C:/xampp/htdocs/CS_project/windowpuzzle.py " . escapeshellarg($last_id3);

        $output = shell_exec($command1);
        $output = shell_exec($command2);
        $output = shell_exec($command3);
        
        #關閉資料庫連接
        $conn->close();
    }
?>

<!-- 彈出視窗 -->
<div class="popup" id="popup">
    <h2>選擇下載選項</h2>
    <p>選擇需要下載的文件部分：</p>

    <!-- 第一組下載選項 -->
    <div class="popup-buttons">
        <a href="core_stl.php" download>
            <img src="maze.png" alt="圓柱" style="width: 200px; height:200px;">
        </a>
        <a href="puzzle_stl.php" download>
            <img src="slide.png" alt="n夾板" style="width:200px; height:200px;">
        </a>
        <a href="puzzle_stl.php" download>
            <img src="puzzle1.png" alt="窗型" style="width:200px; height:200px;">
        </a>
        <a href="download.php?file=gear.stl" download>
            <img src="gear.png" alt="齒輪" style="width:200px; height:200px;">
        </a>
    </div>
    <div class="popup-buttons">
        <a href="core_stl.php" download>
            圓柱
        </a>
        <a href="puzzle_stl.php" download>
            滑板
        </a>
        <a href="puzzle_stl.php" download>
            移動拼圖
        </a>
        <a href="download.php?file=gear.stl" download>
            齒輪
        </a>
    </div>
    <!-- 第二組下載選項 -->
    <div class="popup-buttons">
         <a href="download.php?file=lid.stl" download>
            <img src="lid.png" alt="蓋子" style="width: 200px; height:200px;">
        </a>
        <a href="download.php?file=star.stl" download>
            <img src="star.png" alt="搖搖星" style="width:200px; height:200px;">
        </a>
        <a href="download.php?file=core.stl" download>
            <img src="core.png" alt="中心圓柱" style="width:200px; height:200px;">
        </a>
        <a href="download.php?file=base.stl" download>
            <img src="box.png" alt="底板" style="width:200px; height:200px;">
        </a>
    </div>
    <div class="popup-buttons">
        <a href="download.php?file=lid.stl" download>
            蓋子
        </a>
        <a href="download.php?file=star.stl" download>
            搖搖星
        </a>
        <a href="download.php?file=core.stl" download>
            中心圓柱
        </a>
        <a href="download.php?file=base.stl" download>
            底板
        </a>
    </div>

    <!-- 取消按鈕 -->
    <button class="cancel-button" onclick="closePopup()">取消</button>
</div>

<script>
    function openPopup() {
        document.getElementById("popup").style.display = "block";
    }

    function closePopup() {
        document.getElementById("popup").style.display = "none";
    }

    function submitFormWithPopup() {
        // 使用 AJAX 發送表單資料，避免頁面重載
        const formData = new FormData(document.getElementById("mazeForm"));
        
        fetch("", { // 改為空字符串以指向當前頁面
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            // 成功後打開彈出視窗
            openPopup();
            console.log(data); // 檢查伺服器返回的資料
        })
        .catch(error => {
            console.error("Error:", error);
        });
    }
</script>

</body>
</html>
