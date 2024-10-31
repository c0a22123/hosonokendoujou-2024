-- データベースを作成
CREATE DATABASE MyDatabase;

-- データベースを選択
USE MyDatabase;

-- テーブル：login
CREATE TABLE login (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- テーブル：user_infomation
CREATE TABLE user_infomation (
    user_id INT,
    gendar VARCHAR(10),
    birthday VARCHAR(10),
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES login(user_id)
);

-- テーブル：event
CREATE TABLE event (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(100)
);

-- テーブル：bingo
CREATE TABLE bingo (
    user_id INT,
    event_id INT,
    bingo_row0 VARCHAR(10),
    bingo_row1 VARCHAR(10),
    bingo_row2 VARCHAR(10),
    bingo_row3 VARCHAR(10),
    bingo_row4 VARCHAR(10),
    bingo_row5 VARCHAR(10),
    bingo_row6 VARCHAR(10),
    bingo_row7 VARCHAR(10), 
    bingo_row8 VARCHAR(10),
    total_bingo INT,
    PRIMARY KEY (user_id, event_id),
    FOREIGN KEY (user_id) REFERENCES login(user_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id)
);



CREATE TABLE prize_exchange (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    exchanged BOOLEAN DEFAULT FALSE,
    exchange_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES login(user_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id)
);
