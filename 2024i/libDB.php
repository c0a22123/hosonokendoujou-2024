<?php
class libDB{
    private PDO $pdo;
    /**
     * コンストラクタ
     */
    public function __construct()
    {
        $this->pdo = new PDO("mysql:host=localhost;dbname=2024i;charset=utf8","2024i","2024i", 
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_WARNING]);

    }

    public function getPDO(){
        return $this->pdo;
    }
}
?>