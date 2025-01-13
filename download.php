<?php
// 連接到資料庫
$conn = new mysqli("localhost", "web", "1234", "CS_topics");

// 檢查連接
if ($conn->connect_error) {
    die("資料庫連接失敗: " . $conn->connect_error);
}

// 獲取要下載的檔案名稱，並去掉副檔名，然後過濾檔名
$file = isset($_GET['file']) ? pathinfo($conn->real_escape_string($_GET['file']), PATHINFO_FILENAME) : '';

// 構建 SQL 查詢語句
$sql = "SELECT `$file` FROM `download` LIMIT 1"; // 確保從資料表中獲取檔案內容
$result = $conn->query($sql);

if ($result && $result->num_rows > 0) {
    $row = $result->fetch_assoc();
    $stlFileContent = $row[$file];

    // 設置 HTTP 標頭來觸發下載
    header('Content-Type: application/octet-stream');
    header("Content-Disposition: attachment; filename=\"$file.stl\""); // 下載檔案時加上 .stl 副檔名
    header("Content-Length: " . strlen($stlFileContent)); // 設定檔案大小

    echo $stlFileContent;
    exit;
} else {
    echo "找不到對應的 STL 檔案或查詢錯誤。";
}

// 關閉連接
$conn->close();
?>
