
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>予約完了 - GALAXY AIRLINES</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Amatic+SC:wght@700&display=swap');

    body {
      font-family: 'Amatic SC', cursive;
      margin: 0;
      padding: 0;
      background: linear-gradient(140deg, #030f39ee 0%, #000000 100%);
      color: white;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }

    h1 {
      text-align: center;
      font-size: 50px;
      text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
      animation: fadeInDown 1s ease-out;
    }

    .content {
      max-width: 800px;
      padding: 20px;
      margin: 20px;
      background: rgba(0, 0, 0, 0.5);
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      animation: fadeIn 1s ease-out;
      text-align: center;
    }

    .details {
      font-size: 24px;
      margin: 20px 0;
    }

    .btn {
      padding: 10px 20px;
      background-color: blueviolet;
      color: white;
      text-decoration: none;
      border-radius: 25px;
      font-size: 18px;
      transition: background-color 0.3s ease;
      animation: fadeIn 1s ease-out;
      margin-top: 20px;
      display: inline-block;
    }

    .btn1 {
      padding: 10px 20px;
      background-color: blueviolet;
      color: white;
      text-decoration: none;
      border-radius: 25px;
      font-size: 18px;
      transition: background-color 0.3s ease;
      animation: fadeIn 1s ease-out;
      margin-top: 20px;
      display: inline-block;
    }

    .btn:hover {
      background-color: #6a0dad;
    }

    @keyframes fadeInDown {
      0% {
        opacity: 0;
        transform: translateY(-50px);
      }
      100% {
        opacity: 1;
        transform: translateY(0);
      }
    }

    @keyframes fadeIn {
      0% {
        opacity: 0;
      }
      100% {
        opacity: 1;
      }
    }
  </style>
</head>
<body>
  <h1>予約完了</h1>
  <div class="content">
    <p class="details">
      ご予約ありがとうございます。予約が正常に完了しました。<br>
      以下の詳細を確認してください。
    </p>

    <p class="details">
      予約番号: 12345678<br>
      フライト: 東京 (HND) →  <?php echo htmlspecialchars($_GET['location']); ?>(KIX)<br>
      出発日時: 2024年7月15日 10:00<br>
      席: 12A<br>
    </p>

    <p class="details">
      メールで確認メッセージを送信しました。ご確認ください。
    </p>

    <?php if (isset($_SESSION['user_name'])): ?>
    <a href="../user.php" class="btn">ログアウトしてホームに戻る</a>
    <?php else: ?>
    <a href="/2024i/templates/home.html" class="btn1">ログアウトしてホームに戻る</a>
    <?php endif; ?>

    
  </div>
</body>
</html>
