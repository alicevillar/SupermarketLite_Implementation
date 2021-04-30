-- nome de tabela : leva TB_
-- nome de campo
-- nome de primary key: leva PK_ (nome da tabela, pq eh a PK da tabela) 
-- nome de foreign key: leva FK_ (leva o nome do relacionamento: nome das duas tabelas)

--A primary key tem seu nome com referencia `a tabela de onde ela pertence (CONSTRAINT/nome da primary key/PRIMARY KEY(o campo da presente tabela) 
--Sintaxe da foreign key: CONSTRAINT/nome da FK (q referencia as 2 tabelas)/foreign key(campo)/references tabela de origem(campo) 

CREATE DATABASE Supermarket_Database;
USE Supermarket_Database;

CREATE TABLE TB_Person (
Per_Code int identity(1,1),
Per_Name varchar (300) not null,
Per_Phone int not null,
Per_E_mail varchar (100) not null,
Per_Username varchar (20) not null,
Password varchar (20) not null,
constraint PK_Person primary key clustered (Per_Code)
); 

CREATE TABLE TB_Category (
Cat_Code int identity (1,1),
Cat_Name varchar (300) not null,
constraint PK_Category primary key clustered (Cat_Code)
);
 
CREATE TABLE TB_Position (
Pos_Code int identity (1,1),
Pos_Description varchar (500) not null,
constraint PK_Position primary key clustered (Pos_Code)
);

CREATE TABLE TB_Cart (
Car_Code int identity (1,1),
constraint PK_Cart primary key clustered (Car_Code)
);

CREATE TABLE TB_Ticket (
Tic_Id int identity (1,1),
Tic_Code int not null,
Tic_Due_Date date,
Tic_Value decimal,
constraint PK_Ticket primary key clustered (Tic_Id)
);
 
CREATE TABLE TB_Stored_Cards (
StC_Id int identity (1,1),
StC_Code int not null,
StC_Name varchar (20) not null,
constraint PK_Stored_Cards primary key clustered (StC_Id)
);

CREATE TABLE TB_Loyalty_Origin (
LoO_Id int identity (1,1),
LoO_Name varchar (20),
constraint PK_Loyalty_Origin primary key clustered (LoO_Id)
);

CREATE TABLE TB_Loyalty_Schemes (
LoS_Id int identity (1,1),
LoS_Cause_Id int not null,
LoS_Value_Type varchar (20),
LoS_Value decimal,
constraint PK_Loyalty_Schemes primary key (LoS_Id),
constraint FK_Loyalty_Schemes_Loyalty_Origin foreign key (LoS_Cause_Id) references TB_Loyalty_Origin (LoO_Id)
);

  
CREATE TABLE TB_Online_Order (
OnO_Id int identity (1,1),
OnO_Date date,
OnO_Purchase_Date date,
OnO_Cart_Code  int not null,
OnO_Customer_Code int not null,
constraint PK_Online_Order primary key (OnO_Id),
constraint FK_Online_Order_Cart foreign key (OnO_Cart_Code) references TB_Cart (Car_Code),
constraint FK_Online_Order_Customer foreign key (OnO_Customer_Code) references TB_Person (Per_Code)
);

CREATE TABLE TB_Payment (
Pay_Online_Order_Id int not null,
Pay_Date date,
constraint FK_Payment_Online_Order foreign key (Pay_Online_Order_Id) references TB_Online_Order (OnO_Id)
);
 
CREATE TABLE TB_Payment_Type (
PaT_Id int identity (1,1),
PaT_Name varchar (30),
PaT_Status varchar (20),
PaT_Ticket_Id int not null,
PaT_Loyalty_Id int not null,
PaT_Card_Id int not null,
constraint PK_Payment_Type primary key (PaT_Id),
constraint FK_Payment_Type_Ticket foreign key (PaT_Ticket_Id) references TB_Ticket  (Tic_Id),
constraint FK_Payment_Type_Loyalty_Schemes foreign key (PaT_Loyalty_Id) references TB_Loyalty_Schemes (LoS_Id),
constraint FK_Payment_Type_Stored_Cards foreign key (PaT_Card_Id) references TB_Stored_Cards (StC_Id) 
);

CREATE TABLE TB_Products (
Pro_Code int identity (1,1),
Pro_Name varchar (50),
Pro_Category_Code int not null,
constraint PK_Products primary key (Pro_Code),
constraint FK_Products_Category foreign key (Pro_Category_Code) references TB_Category (Cat_Code)
);

 
CREATE TABLE TB_Staff (
Sta_Salary decimal,
Sta_Position_Code int not null,
Sta_Person_Code int not null,
constraint FK_Staff_Position foreign key (Sta_Position_Code) references TB_Position (Pos_Code),
constraint FK_Staff_Person foreign key (Sta_Person_Code) references TB_Person (Per_Code)
);

CREATE TABLE TB_Cart_Items (
CaI_Cart_Code int not null,
CaI_Product_Code int not null,
constraint PK_Cart_Items primary key (CaI_Cart_Code),
constraint FK_Cart_Items_Cart foreign key (CaI_Cart_Code) references TB_Cart (Car_Code),
constraint FK_Cart_Items_Products foreign key (CaI_Product_Code) references TB_Products(Pro_Code)
);
