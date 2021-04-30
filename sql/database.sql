CREATE DATABASE Supermarket_Database;
USE Supermarket_Database;

CREATE TABLE Person (
Person_cod int not null auto_increment,
Person_name varchar (300) not null,
Phone int not null,
E_mail varchar (100) not null,
Username varchar (20) not null,
Password varchar (20) not null,
primary key (Person_cod)
);

CREATE TABLE Category (
Category_cod int not null auto_increment,
Category_name varchar (300) not null,
primary key (Category_cod)
);

CREATE TABLE Position (
Position_cod int not null auto_increment,
Position_description varchar (500) not null,
primary key (Position_cod)
);

CREATE TABLE Cart (
Cart_cod int not null auto_increment,
primary key (Cart_cod)
);

CREATE TABLE Ticket (
Ticket_id int not null auto_increment,
Ticket_code int not null,
Due_date date,
Ticket_value decimal,
primary key (Ticket_id)
);

CREATE TABLE Stored_Cards (
Card_Id int not null auto_increment,
Card_code int not null,
Card_name varchar (20) not null,
primary key (Card_Id)
);

CREATE TABLE Loyalty_origin (
Loyalty_cause_Id int not null auto_increment,
Loyalty_cause_name varchar (20),
primary key (Loyalty_cause_Id)
);


CREATE TABLE Loyalty_schemes (
Loyalty_Id int not null auto_increment,
Loyalty_cause_Id int not null,
Value_type varchar (20),
Loyalty_value decimal,
primary key (Loyalty_Id),
foreign key (Loyalty_cause_Id) references Loyalty_origin (Loyalty_cause_Id)
);

CREATE TABLE Online_Order (
Online_order_Id int not null auto_increment,
Online_order date,
Purchase_date date,
Cart_cod  int not null,
Customer_cod int not null,
primary key (Online_order_Id),
foreign key (Cart_cod) references Cart (Cart_cod),
foreign key (Customer_cod) references Person (Person_cod)
);

CREATE TABLE Payment (
Online_order_Id int not null,
Payment date,
foreign key (Online_order_Id) references Online_Order (Online_order_Id)
);

CREATE TABLE Payment_Type (
Payment_type_Id int not null auto_increment,
Payment_type_name varchar (30),
Payment_status varchar (20),
Ticket_id int not null,
Loyalty_id int not null,
Card_Id int not null,
primary key (Payment_type_Id),
foreign key (Ticket_id) references Ticket (Ticket_id),
foreign key (Loyalty_Id) references Loyalty_schemes (Loyalty_Id),
foreign key (Card_Id) references Stored_Cards (Card_Id)
);

CREATE TABLE products (
Product_cod int NOT NULL AUTO_INCREMENT,
Product_name varchar(400) DEFAULT NULL,
Category_cod int NOT NULL,
PRIMARY KEY (Product_cod),
KEY `Category_cod` (Category_cod),
FOREIGN KEY (`Category_cod`) REFERENCES `category` (`Category_cod`)
);

CREATE TABLE Staff (
Salary decimal,
Position_cod int not null,
Person_cod int not null,
foreign key (Position_cod) references Position (Position_cod),
foreign key (Person_cod) references Person (Person_cod)
);

CREATE TABLE Cart_Items (
Cart_cod int not null,
Product_cod int not null,
primary key (Cart_cod,Product_cod),
foreign key (Cart_cod) references Cart (Cart_cod),
foreign key (Product_cod) references Products (Product_cod)
);


