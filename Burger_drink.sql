use restaurant;

create table burger
(
burger_id INT PRIMARY KEY AUTO_INCREMENT,
burger_type ENUM('veg', 'non veg'),
burger_name VARCHAR(50)
); -- Burger Table

CREATE TABLE drinks (
    drink_id INT PRIMARY KEY AUTO_INCREMENT,
    drink_name VARCHAR(50)
); -- Drinks Table

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    burger_id INT,
    drink_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (burger_id) REFERENCES burgers(burger_id),
    FOREIGN KEY (drink_id) REFERENCES drinks(drink_id)
); -- Order table

insert into burger(burger_type,burger_name)
values('veg',"paneer"),
('veg',"cheesse"),
('veg',"chinese"),
('veg',"vegetable"),
('veg',"healthy"),
('veg',"pav bhaji"),
('non veg',"chicken"),
('non veg',"mutton"),
('non veg',"friedchicken"),
('non veg',"beef");

show tables;

select * from burger;


insert into drinks(drink_name)
values("coke"),
("sprite"),
("icedcoke"),
("icecream"),
("hot tea"),
("hot chocolate");



