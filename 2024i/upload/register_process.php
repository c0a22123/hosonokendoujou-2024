<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "flight_booking";

// データベース接続の作成
$conn = new mysqli($servername, $username, $password, $dbname);

// 接続チェック
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// フォームからのデータ取得
$user_name = $_POST['user_name'];
$email = $_POST['email'];
$password = password_hash($_POST['password'], PASSWORD_DEFAULT); // パスワードをハッシュ化

// SQLクエリの準備と実行
$sql = "INSERT INTO user_table (user_name, email, password) VALUES (?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("sss", $user_name, $email, $password);

if ($stmt->execute()) {
    echo "登録成功。<a href='login.php'>ログイン</a>してください。";
} else {
    echo "エラー: " . $stmt->error;
}

$stmt->close();
$conn->close();
?>