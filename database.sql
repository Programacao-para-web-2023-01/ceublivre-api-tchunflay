create database product_list;

show databases;

use product_list;

create table `products`(
    `product_id` int not null auto_increment,
    `product_name` varchar(255) not null,
    `product_brand` varchar(255) not null,
    `product_description` varchar(1023) not null,
    `product_category` varchar(255) not null,
    `product_rate` float,
    `product_price` decimal(15,2) not null,
    primary key(`product_id`)
);


INSERT INTO products(
    `product_name`,
    `product_brand`,
    `product_description`,
    `product_category`,
    `product_rate`,
    `product_price`
)VALUES(
	"PS5", "Sony",
    "Console de Jogos",
    "Videogame",
    5.5,
    5499.99
    );
    
SELECT * from `products` WHERE `product_name` = "PS5";