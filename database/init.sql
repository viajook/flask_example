CREATE DATABASE gtg_db;
USE gtg_db;

CREATE TABLE product_data (
    Product_Name VARCHAR(50),
    Description VARCHAR(50)
);

INSERT INTO product_data
  (Product_Name, Description)
VALUES
  ('Green Tea', 'Blended tropical tea'),
  ('Black Tea', 'Earl grey '),
  ('Cappuccino', 'Italian blended');
