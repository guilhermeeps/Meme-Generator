USE Memegeneratordb;

CREATE TABLE memes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    image_url varchar(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT NOW()
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

-- Comment the lines below if you want to create a blank database
INSERT INTO memes (image_url) VALUES ('https://i.redd.it/3ua7gfoza1tc1.png');
INSERT INTO memes (image_url) VALUES ('https://i.redd.it/q99oxbpwi3tc1.png');
