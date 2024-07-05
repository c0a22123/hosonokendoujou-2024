<?php
// smarty初期設定
require_once("pnwsmarty.php");
$pnw =new pnwsmarty();
$smarty =$pnw->getTpl();


// 検索対象データ
$fligth_table = [
    [12,'航空機名1','ヴィクトリア国際空港（カナダ）',12,13],
    [22,'航空機名2','仁川国際空港（韓国）',22,23],
    [32 ,'航空機名3','北京首都国際空港（中国）',32,33],
    [42 ,'航空機名4','フランクフルト（ドイツ）',42,43],
    [52 ,'航空機名5','ハワイ（アメリカ合衆国）',52,53],
    [62 ,'航空機名6','ハノイ（ベトナム）',62,63],
    [72 ,'航空機名7','ロサンゼルス（アメリカ合衆国）',72,73],
    [82 ,'航空機名8','フランシスコ・バンコイン（フィリピン）',82,83],
    [92 ,'航空機名9','インディラ・ガンディー（インド）',92,93],
    [102 ,'航空機名10','ヴェネツィア・テッセラ（イタリア）',102,103]
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
$smarty->display('search2.html');
?>