<?php
require_once 'config.php';
require_once 'UserDAO.php';

session_start();
$login_error = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $user_name = $_POST['user_name'];
    $mail_address = $_POST['mail_address'];
    $passport_name = $_POST['passport_name'];
    $password = $_POST['password'];

    $userDAO = new UserDAO($pdo);
    $user = $userDAO->loginUser($user_name, $mail_address, $passport_name, $password);

    if ($user) {
        $_SESSION['user_id'] = $user['user_id'];
        $_SESSION['user_name'] = $user['user_name'];
        header('Location: dashboard.php');
        exit();
    } else {
        $login_error = 'ユーザー名またはパスワードが間違っています。';
    }
}
?>

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ログイン</title>
    <link rel="stylesheet" href="templates_c\styles2.css">
    <nav>
            <ul>
                <li><a href="templates/home.html">ホーム</a></li>
                <li><a href="templates/register.html">会員登録</a></li>
            </ul>
        </nav>
    

    
</head>
<body>
    <h1>ログイン</h1>
    <?php if ($login_error): ?>
        <p style="color:red;"><?php echo htmlspecialchars($login_error); ?></p>
    <?php endif; ?>
    <form action="login.php" method="post">
        <label for="user_name">ユーザー名:</label>
        <input type="text" id="user_name" name="user_name" required><br>

        <label for="mail_address">メールアドレス:</label>
        <input type="text" id="mail_address" name="mail_address" required><br>

        <label for="passport_name">パスポート記載名前:</label>
        <input type="text" id="passport_name" name="passport_name" required><br>

        <label for="password">パスワード:</label>
        <input type="password" id="password" name="password" required><br>

        <input type="submit" value="ログイン">
    </form>
</body>
</html>
