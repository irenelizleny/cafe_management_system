☕ Café de Velours – Cafe Management & Billing System

A Python + MySQL based application designed to streamline and digitalize the daily operations of a café, including menu management, order processing, and automated billing.


Overview

Café de Velours is a console-based management system built to simplify how small cafés operate. It replaces manual processes with a structured digital system, improving accuracy, efficiency, and ease of use for both administrators and customers.

The system supports two types of users:
- Admin – manages menu data
- Customer – browses menu, places orders, and generates bills


Features

Admin Functionalities
- Add new snack and beverage items
- Update existing item prices
- Delete unavailable items
- Maintain menu data securely in a MySQL database

Customer Functionalities
- View complete menu in a structured tabular format
- Search items by name
- Add items to cart
- Generate detailed bill including:
  - Item-wise pricing
  - Quantity calculation
  - Subtotal
  - Discount (via coupon code)

Tech Stack

- Python – Core application logic
- MySQL – Database for storing menu and order data
- MySQL Connector – Integration between Python and MySQL

---

How to Run

1. Install Python (3.9 or above)
2. Install MySQL (8.0 or above) 
3. Install required dependency:
   pip install mysql-connector-python
4. Set up the MySQL database
5. Create the required database and tables (based on project structure)
6. Run the application:
   python main.py
   
Demo Credentials
Admin ID: admincdv
Password: 1234
