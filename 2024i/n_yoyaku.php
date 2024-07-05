<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>登録情報を入力してください</title>
    
</head>
<style>
    /* Reset styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(to right, #8360c3, #2ebf91);
    color: #333;
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
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
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    width: 400px;
    max-width: 90%;
    text-align: center;
    animation: fadeIn 1s ease forwards;
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
    border-color: #8360c3;
}

.btn-submit {
    background-color: #2ebf91;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1rem;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn-submit:hover {
    background-color: #249d7d;
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

</style>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="templates/home.html">ホーム</a></li>
            </ul>
        </nav>
    </header>
    <div class="container">
        <h1>必要情報の入力</h1>
        <h2>東京発→<?php echo htmlspecialchars($_GET['location']); ?><h2>
            <div class="form-group">
                <label for="user_name">ユーザー名:</label>
                <input type="text" id="user_name" name="user_name" required>
            </div>

            <div class="form-group">
                <label for="mail_address">メールアドレス:</label>
                <input type="email" id="mail_address" name="mail_address" required>
            </div>

            <div class="form-group">
                <label for="passport_name">パスポート記載名前:</label>
                <input type="text" id="passport_name" name="passport_name" required>
            </div>

            <div class="form-group">
                <label for="password">電話番号:</label>
                <input type="text" id="password" name="password" required>
            </div>

             <a href="complete_n.php?location=<?php echo htmlspecialchars($_GET['location'])?> " class="btn-submit">予約完了</a> 
    </div>
</body>
</html>