<?php
/* Smarty version 3.1.39, created on 2024-07-05 10:10:39
  from 'C:\xampp\htdocs\2024i\templates\search2.html' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6687aa7f14cb51_58518299',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '9cc5be8ba3956c1eaa548430953e605182d1f453' => 
    array (
      0 => 'C:\\xampp\\htdocs\\2024i\\templates\\search2.html',
      1 => 1720166099,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6687aa7f14cb51_58518299 (Smarty_Internal_Template $_smarty_tpl) {
?>
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>国際検索</title>
    <!-- <link rel="stylesheet" href="..\templates_c\styles.css">//cssと繋げる -->
</head>
<style>
    body {
                font-family: 'Amatic SC', cursive;
                margin: 0;
                padding: 0;
                background: url('https://aomaterial.com/wp-content/uploads/2022/08/%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%82%82%E3%82%84%E3%82%82%E3%82%84%E8%83%8C%E6%99%AF.png') no-repeat center center fixed;
                background-size: cover;
                display: flex;
                flex-direction: column;
                align-items: center;    
            }

            .font{
                text-align: center;
                margin-top: 30px;
                color: rgb(255, 255, 255);
                font-size: 30px;
                -webkit-text-stroke: 1px #ffb300;
             text-shadow: 0px 4px 8px #674800a4;
                animation: fadeInDown 1s ease-out;
                animation: fadeInDown 1s ease-out;
            }
            .h1{
                text-align: center;
                margin-top: 30px;
                color: rgb(255, 255, 255);
                font-size: 30px;
             -webkit-text-stroke: 1px #ffb300;
             text-shadow: 0px 4px 8px #674800a4;
                animation: fadeInDown 1s ease-out;
            }
            .h2{
                text-align: center;
                margin-top: 30px;
                color: rgb(255, 255, 255);
                font-size: 30px;
             -webkit-text-stroke: 1px #ffb300;
             text-shadow: 0px 4px 8px #674800a4;
                animation: fadeInDown 1s ease-out;
            }
            .ken{
                text-align: center;
                margin-top: 30px;
                font-size: 30px;
                animation: fadeInDown 1s ease-out;
            }
</style>
<body>
    <header>
        <div class="h1">
        <h1>国際検索</h1></div>
    </header>
    <main>
        <section>
            <!-- <h2>フライト検索</h2>
            <form action="hit.php" method="GET">
                <label for="arrival_city">到着地:</label>
                <input type="text" id="arrival_city" name="arrival_city" required>

                <label for="departure_date">出発日:</label>
                <input type="date" id="departure_date" name="departure_date" required>

                <label for="departure_date">クラス(ランク):</label>
                <input type="date" id="departure_date" name="departure_date" required>
                <button type="submit">検索</button>
            </form> -->
            <div class="h2">
            <h2>フライト検索</h2>
            <p>行きたい場所を入力してください</p></div>
            <form method="post" action="">
            <!-- <label for="search">到着地:</label> -->
                <div class="ken">
                <input type="text" name="search" value="<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['search']->value, ENT_QUOTES, 'UTF-8', true);?>
">
                <input type="submit" value="検索"></div>
                <!-- <form method="post" action="">
                    <input type="text" name="search" value="<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['search']->value, ENT_QUOTES, 'UTF-8', true);?>
">
                    <input type="submit" value="検索"> -->
            </form>
            <?php if ($_smarty_tpl->tpl_vars['search']->value) {?>
                <div class="font">
                <h2>検索結果</h2>
                <?php if (count($_smarty_tpl->tpl_vars['results']->value) > 0) {?>
                    <ul>
                        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['results']->value, 'article');
$_smarty_tpl->tpl_vars['article']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['article']->value) {
$_smarty_tpl->tpl_vars['article']->do_else = false;
?>
                        <li><a href="n_yoyaku.php?location=<?php echo htmlspecialchars($_smarty_tpl->tpl_vars['article']->value[2], ENT_QUOTES, 'UTF-8', true);?>
"><strong><?php echo htmlspecialchars($_smarty_tpl->tpl_vars['article']->value[1], ENT_QUOTES, 'UTF-8', true);?>
</strong>: <?php echo htmlspecialchars($_smarty_tpl->tpl_vars['article']->value[2], ENT_QUOTES, 'UTF-8', true);?>
 </a></li>
                        <?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
                    </ul>
                <?php } else { ?>
                    <p>一致する結果が見つかりませんでした。</p></div>
                <?php }?>
            <?php }?>
        </section>
    </main>
</body>
</html><?php }
}
