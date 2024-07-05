<?php
require_once 'config.php';

class UserDAO {
    private $pdo;

    public function __construct($pdo) {
        $this->pdo = $pdo;
    }

    public function loginUser($user_name, $mail_address, $passport_name, $password) {
        $sql = 'SELECT * FROM user_table WHERE user_name = ? AND mail_address = ? AND passport_name = ? AND password = ?';
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([$user_name, $mail_address, $passport_name, $password]);

        $user = $stmt->fetch(PDO::FETCH_ASSOC);
        return $user;
    }
}
?>
