<?php
// データベースの接続情報
$servername = "localhost";
$username = "root"; // データベースのユーザー名
$password = ""; // データベースのパスワード
$dbname = "2024i";

// フォームからのデータを受け取る
$user = $_POST['user_name'];
$mail = $_POST['mail_address'];
$passport = $_POST['passport_name'];
$pass = $_POST['password'];


try {
    // データベースに接続
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // エラーモードを例外に設定
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // SQL文を準備
    $sql = "INSERT INTO user_table (user_name, mail_address, passport_name, password) VALUES (:user_name, :mail_address, :passport_name, :password)";
    
    // SQL文を実行
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':user_name', $user);
    $stmt->bindParam(':mail_address', $mail);
    $stmt->bindParam(':passport_name', $passport);
    $stmt->bindParam(':password', $pass);
    $stmt->execute();

    echo "新規会員登録が完了しました";
} catch(PDOException $e) {
    echo "エラーが発生しました: " . $e->getMessage();
}

// 接続を閉じる
$conn = null;
?>


<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>会員登録</title>
    <link rel="stylesheet" href="..\templates_c\styles2.css">
</head>
<style>

/* Reset styles */
* {
    margin: 20;
    padding: 20;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
}

/* Header styles */
header {
    width: 100%;
    background-color: #333;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 10px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-size: 1.2rem;
    padding: 10px 20px;
    transition: background-color 0.3s ease;
}

nav ul li a:hover {
    background-color: #555;
}

/* Container styles */
.container {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 400px;
    max-width: 90%;
    text-align: center;
    margin-top: 20px;
    animation: fadeIn 1s ease-out;
    
}

.container h1 {
    font-size: 2rem;
    margin-bottom: 20px;
    color: #333;
}

/* Form styles */
.register-form {
    display: flex;
    flex-direction: column;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-size: 1.2rem;
    margin-bottom: 5px;
    color: #555;
}

.form-group input[type="text"],
.form-group input[type="email"],
.form-group input[type="password"] {
    width: 100%;
    padding: 10px;
    font-size: 1rem;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    transition: border-color 0.3s ease;
}

.form-group input[type="text"]:focus,
.form-group input[type="email"]:focus,
.form-group input[type="password"]:focus {
    outline: none;
    border-color: blueviolet;
}

.btn-submit {
    background-color: blueviolet;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn-submit:hover {
    background-color: #6a0dad;
}

/* Success message */
.success-message {
    margin-top: 20px;
    animation: fadeIn 1s ease-out;
    opacity: 0;
}

.success-message p {
    background-color: #4caf50;
    color: #fff;
    padding: 10px 20px;
    border-radius: 4px;
    font-size: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    
}

/* Keyframe animations */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}


</style>
<body>
    <header>
        
        <nav>
        <ul>
        <li><a href="/2024i/templates/home.html">ホーム</a></li>
        <li><a href="/2024i/login.php">ログイン</a></li>
        </ul>
    </nav>    
        </nav>
    </header>




