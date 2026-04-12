-- Database Setup
CREATE DATABASE cdv;
USE cdv;

-- Snacks Table
CREATE TABLE menu_snacks (
    Item_ID VARCHAR(10) PRIMARY KEY, 
    Item_Name VARCHAR(30), 
    MRP FLOAT
);

INSERT INTO menu_snacks VALUES('S100', 'Veg Burger', 110);
INSERT INTO menu_snacks VALUES('S101', 'Chicken Burger', 120);
INSERT INTO menu_snacks VALUES('S102', 'Beef Burger', 125);
INSERT INTO menu_snacks VALUES('S103', 'Veg Sandwich', 70);
INSERT INTO menu_snacks VALUES('S104', 'Chicken Sandwich', 80);
INSERT INTO menu_snacks VALUES('S105', 'Beef Sandwich', 90);
INSERT INTO menu_snacks VALUES('S106', 'Chicken Shawarma', 100);
INSERT INTO menu_snacks VALUES('S107', 'Beef Shawarma', 110);
INSERT INTO menu_snacks VALUES('S108', 'French Fries', 60);
INSERT INTO menu_snacks VALUES('S109', 'Chicken Nuggets 5pc', 70);
INSERT INTO menu_snacks VALUES('S110', 'Chicken Nuggets 10pc', 140);
INSERT INTO menu_snacks VALUES('S111', 'Croissant', 130);
INSERT INTO menu_snacks VALUES('S112', 'Apple Pie', 180);
INSERT INTO menu_snacks VALUES('S113', 'Pumpkin Pie', 190);
INSERT INTO menu_snacks VALUES('S114', 'Banana Cream Pie', 200);
INSERT INTO menu_snacks VALUES('S115', 'Strawberry Cheesecake (Slice)', 150);
INSERT INTO menu_snacks VALUES('S116', 'Blueberry Cheesecake (Slice)', 150);
INSERT INTO menu_snacks VALUES('S117', 'Biscoff Cheesecake', 190);
INSERT INTO menu_snacks VALUES('S118', 'Cinnamon Rolls', 140);
INSERT INTO menu_snacks VALUES('S119', 'Muffins', 80);
INSERT INTO menu_snacks VALUES('S120', 'Waffles/Pancakes', 190);

-- Beverages Table
CREATE TABLE menu_beverages (
    Item_ID VARCHAR(10) PRIMARY KEY, 
    Item_Name CHAR(30), 
    MRP FLOAT
);

INSERT INTO menu_beverages VALUES ("B100", "Hot Coffee", 45);
INSERT INTO menu_beverages VALUES ("B101", "Cold Coffee", 50);
INSERT INTO menu_beverages VALUES ("B102", "Americano", 65);
INSERT INTO menu_beverages VALUES ("B103", "Iced Latte", 60);
INSERT INTO menu_beverages VALUES ("B104", "Classic Spanish Latte", 75);
INSERT INTO menu_beverages VALUES ("B105", "Hazelnut Latte", 75);
INSERT INTO menu_beverages VALUES ("B106", "Vanilla Latte", 70);
INSERT INTO menu_beverages VALUES ("B107", "Dark Mocha", 65);
INSERT INTO menu_beverages VALUES ("B108", "Caramel Machiatto", 80);
INSERT INTO menu_beverages VALUES ("B109", "White Chocolate Mocha", 75);
INSERT INTO menu_beverages VALUES ("B110", "Strawberries&Cream Frappucino", 80);
INSERT INTO menu_beverages VALUES ("B111", "Mango Frappuccino", 95);
INSERT INTO menu_beverages VALUES ("B112", "Hot Tea", 40);
INSERT INTO menu_beverages VALUES ("B113", "Iced Tea", 45);
INSERT INTO menu_beverages VALUES ("B114", "Lemon Tea", 50);
INSERT INTO menu_beverages VALUES ("B115", "Mango Tea", 75);
INSERT INTO menu_beverages VALUES ("B116", "Green Tea", 60);
INSERT INTO menu_beverages VALUES ("B117", "Jasmine Tea", 70);
INSERT INTO menu_beverages VALUES ("B118", "Mint Tea", 65);
INSERT INTO menu_beverages VALUES ("B119", "Boba Tea", 125);
INSERT INTO menu_beverages VALUES ("B120", "Chocolate Milkshake", 70);