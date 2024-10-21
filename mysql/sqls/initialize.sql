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

-- テーブル：coupon
CREATE TABLE coupon (
    user_id INT,
    event_id INT,
    1bingo_count INT,
    4bingo_count INT,
    8bingo_count INT,
    PRIMARY KEY (user_id, event_id),
    FOREIGN KEY (user_id) REFERENCES login(user_id),
    FOREIGN KEY (event_id) REFERENCES event(event_id)
);

-- テーブル：coupon_store
CREATE TABLE coupon_store (
    store_name VARCHAR(100),
    store_infomation TEXT,
    store_opentime TIME,
    store_closed TIME,
    store_transportation VARCHAR(255),
    store_money DECIMAL(10, 2),
    store_png VARCHAR(255),
    PRIMARY KEY (store_name)
);

-- テーブル：store_infomation
CREATE TABLE store_infomation (
    event_id INT,
    store_name VARCHAR(100),
    PRIMARY KEY (event_id, store_name),
    FOREIGN KEY (event_id) REFERENCES event(event_id),
    FOREIGN KEY (store_name) REFERENCES coupon_store(store_name)
);

-- テーブル：spot_infomation
CREATE TABLE spot_infomation (
    spot_name VARCHAR(100),
    spot_opentime TIME,
    spot_closed TIME,
    spot_transportation VARCHAR(255),
    spot_png VARCHAR(255),
    PRIMARY KEY (spot_name)
);

-- テーブル：another_infomation
CREATE TABLE another_infomation (
    event_id INT,
    anspot_name VARCHAR(100),
    anspot_opentime TIME,
    anspot_closed TIME,
    anspot_transportation VARCHAR(255),
    anspot_png VARCHAR(255),
    PRIMARY KEY (event_id, anspot_name),
    FOREIGN KEY (event_id) REFERENCES event(event_id)
);



