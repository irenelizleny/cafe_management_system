☕ Café de Velours – Cafe Management & Billing System

A Python + MySQL based application designed to streamline and digitalize the daily operations of a café, including menu management, order processing, and automated billing.


Overview

Café de Velours is a console-based management system built to simplify how small cafés operate. It replaces manual processes with a structured digital system, improving accuracy, efficiency, and ease of use for both administrators and customers.

The system supports two types of users:
- Admin – manages menu data
- Customer – browses menu, searches for items, places orders, and generates bills

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
 
<img width="694" height="698" alt="image" src="https://github.com/user-attachments/assets/9570c300-7eeb-4e9e-9d84-828400b17b33" />
<img width="567" height="575" alt="image" src="https://github.com/user-attachments/assets/cc928ab5-5e58-48fa-9905-11232b776675" />
<img width="761" height="684" alt="image" src="https://github.com/user-attachments/assets/566ae22c-abde-4d33-b41b-67f729f5b2f0" />
<img width="753" height="677" alt="image" src="https://github.com/user-attachments/assets/32453e42-1cd3-49ee-af8c-da1649bf5fc8" />
<img width="745" height="817" alt="image" src="https://github.com/user-attachments/assets/82ebb457-9b0b-428d-bb48-9d75f4549ae1" />
<img width="635" height="719" alt="image" src="https://github.com/user-attachments/assets/87181ce0-148c-4fba-8f4d-14f1aa41bc8b" />
<img width="736" height="668" alt="image" src="https://github.com/user-attachments/assets/8f728694-c035-4c02-8ea6-a828af450b8e" />
<img width="750" height="634" alt="image" src="https://github.com/user-attachments/assets/d6399683-fcf2-488b-a092-6e7081d74a64" />
<img width="738" height="779" alt="image" src="https://github.com/user-attachments/assets/18bc2cb4-3dc7-4e8d-b47c-049d116402ad" />
<img width="742" height="816" alt="image" src="https://github.com/user-attachments/assets/3735c897-4d5d-4f52-8488-5f6384a7697e" />

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
