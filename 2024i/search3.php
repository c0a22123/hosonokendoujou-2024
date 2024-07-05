<?php
// smarty初期設定
require_once("pnwsmarty.php");
$pnw =new pnwsmarty();
$smarty =$pnw->getTpl();


// 検索対象データ
$fligth_table = [
    [12,'航空機名1','那覇空港',12,13],
    [22,'航空機名2','函館空港',22,23],
    [32 ,'航空機名3','仙台空港',32,33],
    [42 ,'航空機名4','出雲空港',42,43],
    [52 ,'航空機名5','福岡空港',52,53],
    [62 ,'航空機名6','関西空港',62,63],
    [72 ,'航空機名7','長崎空港',72,73],
    [82 ,'航空機名8','青森空港',82,83],
    [92 ,'航空機名9','新潟空港',92,93],
    [102 ,'航空機名10','成田空港',102,103]
];
$search = '';
$results = [];

// 検索処理
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $search = $_POST['search'];
    foreach ($fligth_table as $article) {//flight_tableを回す
        if (stripos($article[2], $search) !== false  || stripos($article[1], $search)!== false){//条件分岐で配列の2番目と3番目を検索する
            $results[] = $article;
        }
    }
}

// Smartyに変数を渡す
$smarty->assign('search', $search);
$smarty->assign('results', $results);

// テンプレートを表示
$smarty->display('search3.html');
?>