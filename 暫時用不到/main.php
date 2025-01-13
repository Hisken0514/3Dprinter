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

        .wrapper {
            display: flex;
            justify-content: center;
            align-items: flex-start; /* 將表單與選項區對齊 */
            gap: 20px; /* 增加左右區塊之間的間距 */
        }

        .options-container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .options-container h2 {
            margin-top: 0;
            text-align: center;
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

        .download-section {
            position: absolute;
            right: 20px;
            top: 10px;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 150px; /* 將寬度調窄 */
            margin-bottom: 20px; /* 增加區塊之間的間距 */
        }

        .message {
            margin-top: 20px;
            text-align: center;
        }
    </style>
    <script>
        function togglePuzzleSelection() {
            var puzzleCheckbox = document.getElementById("puzzle");
            var windowPuzzleSelect = document.getElementById("windowPuzzle");

            windowPuzzleSelect.disabled = !puzzleCheckbox.checked;
        }

        function togglesliderSelection() {
            var sliderCheckbox = document.getElementById("slider");
            var boardCountSelect = document.getElementById("boardCount");

            boardCountSelect.disabled = !sliderCheckbox.checked;
        }
    </script>
</head>
<body>

<div class="wrapper">
    <!-- 左側核取方塊選項 -->
    <div class="options-container">
        <h2>選擇您所要機關</h2>
        <input type="checkbox" id="puzzle" name="features[]" value="puzzle" onclick="togglePuzzleSelection()">
        <label for="puzzle">移動拼圖</label><br>
        <input type="checkbox" id="slider" name="features[]" value="slider" onclick="togglesliderSelection()">
        <label for="slider">滑板</label><br>
        <input type="checkbox" id="star" name="features[]" value="star">
        <label for="star">搖搖星</label><br>
        <input type="checkbox" id="gear" name="features[]" value="gear">
        <label for="gear">齒輪</label>
    </div>

    <!-- 參數表單 -->
    <div class="container">
        <h1>請輸入以下參數</h1>
        <form method="POST" action="">

            <!-- 難易度設置 -->
            <div class="form-group">
                <label for="difficulty">難易度設置：</label>
                <select id="difficulty" name="difficulty">
                    <option value="簡易">簡易</option>
                    <option value="中等">中等</option>
                    <option value="困難">困難</option>
                </select>
            </div>

            <!-- 滑板的片數 -->
            <div class="form-group">
                <label for="boardCount">滑板的片數：</label>
                <select id="boardCount" name="boardCount" disabled>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                </select>
            </div>

            <!-- 圓柱迷宮 -->
            <div class="form-group">
                <label for="cylinderMaze">選擇中心圓柱迷宮高度：</label>
                <select id="cylinderMaze" name="cylinderMaze">
                    <option value="15x8">8</option>
                    <option value="15x9">9</option>
                    <option value="15x10">10</option>
                    <option value="15x11">11</option>
                    <option value="15x12">12</option>
                </select>
            </div>

            <!-- 移動拼圖大小 -->
            <div class="form-group">
                <label for="windowPuzzle">移動拼圖大小 (高, 寬)：</label>
                <select id="windowPuzzle" name="windowPuzzle" disabled>
                    <option value="3x3">3x3</option>
                    <option value="3x4">3x4</option>
                    <option value="4x3">4x3</option>
                    <option value="4x4">4x4</option>
                </select>
            </div>

            <button type="submit" class="generate-button">產生迷宮</button>
        </form>
    </div>

    <!-- 新增的模型下載選擇區 -->
    <div class="container">
        <h1>選擇要下載的模型</h1>
        <form method="POST" action="">
            <div class="form-group">
                <label for="modelSelection">選擇模型：</label>
                <select id="modelSelection" name="modelSelection">
                    <option value="model1">移動拼圖</option>
                    <option value="model2">滑板</option>
                    <option value="model3">搖搖星</option>
                    <option value="model3">齒輪</option>
                </select>
            </div>
            <button type="submit" class="generate-button">下載選定模型</button>
        </form>
    </div>

        <!-- 第一下載區 -->
        <div class="download-section">
            <h2>下載圓柱模型 </h2>
            <img src="core.png" alt="圓柱模型圖片" style="width:80%; display: block; margin-bottom:5px;">
            <a href="core_stl.php" class="generate-button" style="display: block; padding: 5px 10px; font-size: 14px; width: 150px; text-align: center;">點擊下載</a></div>

        <!-- 第二下載區 -->
        <div class="download-section" style="top: 300px;"> <!-- 改變 top 的值來避免重疊 -->
            <h2>下載機關盒底板</h2>
            <a href="puzzle_stl.php" class="generate-button">點擊下載</a>
        </div>

    <!-- 訊息顯示區 -->
    <div class="message">
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $difficulty = $_POST["difficulty"];
            $cylinderMaze = array_map('intval', explode('x', $_POST["cylinderMaze"]));

            // 連接資料庫
            $conn = new mysqli("localhost", "web", "1234", "cs_topics");
            if ($conn->connect_error) {
                die("連接失敗: " . $conn->connect_error);
            }

            // 插入數據到資料庫
            $stmt = $conn->prepare("INSERT INTO `mazepuzzle` (difficulty, width, height) VALUES (?, ?, ?)");
            $stmt->bind_param("sii", $difficulty, $cylinderMaze[0], $cylinderMaze[1]);
            $stmt->execute();

            // 關閉資料庫連接
            $stmt->close();
            $conn->close();

            echo "<p>迷宮已成功生成！</p>";
        }
        ?>
    </div>

</div>

</body>
</html>
