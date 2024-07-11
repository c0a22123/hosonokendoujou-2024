'''SCREATE TABLE `User` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'AI',
  `user_name` VARCHAR(64) NOT NULL DEFAULT '' COMMENT '氏名',
  `password` VARCHAR(255) NOT NULL DEFAULT '' COMMENT 'パスワード',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4;

INSERT INTO `User` (`id`, `user_name`, `password`) VALUES (1,'user','$2y$10$ecRmAWY4n/jLa0tTzIaG7.SMhb1TfdROy3nXeG5aVZorUX1n6/WHO');'''