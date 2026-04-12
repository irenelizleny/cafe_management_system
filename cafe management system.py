import sys
from prettytable import PrettyTable
import mysql.connector as ms
 
conn = ms.connect(
    host="localhost",
    user="root",
    password="insert your password",
    database="cdv")
 
cur = conn.cursor()
 
print ()
print("Welcome to Café de Velours")
print ()
while True:
    print("Sign in as: ")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")

    ch = int(input("Enter choice : "))
    print()
 
    if ch == 1:
        id_ = input("Enter ID : ")
        if id_ == "admincdv":
            pw_ = int(input("Enter password : "))
            if pw_ == 1234:
                print("Logged in as Admin")
                print()
                while True:
                    print("Admin Menu:")
                    print("1. Add snacks to menu")
                    print("2. Add beverages to menu")
                    print("3. Update price of snack")
                    print("4. Update price of beverage")
                    print("5. Delete snack from menu")
                    print("6. Delete beverage from menu")
                    print("7. Exit")
                    print()
 
                    c = int(input("Enter choice: "))
                    print()
 
                    if c == 1:
                        itemid = input("Enter item ID : ")
                        cur.execute("Select Item_ID from menu_snacks where Item_ID = %s", (itemid,))
                        result = cur.fetchone()
                        if result:
                            print("\nThis Item ID already exists. Please enter a different one.\n")
                        else:
                            itemn = input("Enter snack name : ")
                            mrp = float(input("Enter price : "))
                            cur.execute("Insert into menu_snacks (Item_ID, Item_Name, MRP) values (%s, %s, %s)", (itemid, itemn, mrp))
                            conn.commit()
                            print("\nItem added successfully!\n")
 
                    elif c == 2:
                        itemid = input("Enter item ID : ")
                        cur.execute("Select Item_ID from menu_beverages where Item_ID = %s", (itemid,))
                        result = cur.fetchone()
                        if result:
                            print("\nThis Item ID already exists. Please enter a different one.\n")
                        else:
                            itemn = input("Enter beverage name : ")
                            mrp = float(input("Enter price : "))
                            cur.execute("Insert into menu_beverages (Item_ID, Item_Name, MRP) values (%s, %s, %s)",(itemid, itemn, mrp))
                            conn.commit()
                            print("\nItem added successfully!\n")
 
                    elif c == 3:
                        itemid = input("Enter Item ID of the snack to update: ")
                        cur.execute("Select Item_ID from menu_snacks where Item_ID = %s", (itemid,))
                        result = cur.fetchone()
                        if result:
                            new_price = float(input("Enter new price: "))
                            cur.execute("Update menu_snacks set MRP = %s where Item_ID = %s", (new_price, itemid,))
                            conn.commit()
                            print("\nPrice updated successfully!\n")
                        else:
                            print("\nNo snack found with that Item ID.\n")
 
                    elif c == 4:
                        itemid = input("Enter Item ID of the beverage to update: ")
                        cur.execute("Select Item_ID from menu_beverages where Item_ID = %s", (itemid,))
                        result = cur.fetchone()
                        if result:
                            new_price = float(input("Enter new price: "))
                            cur.execute("Update menu_beverages set MRP = %s where Item_ID = %s", (new_price, itemid))
                            conn.commit()
                            print("\nPrice updated successfully!\n")
                        else:
                            print("\nNo beverage found with that Item ID.\n")
 
                    elif c == 5:
                        itemid = input("Enter Item ID of the snack to delete: ")
                        cur.execute("Select Item_ID from menu_snacks where Item_ID = %s", (itemid,))
                        result = cur.fetchone()
                        if result:
                            cur.execute("Delete from menu_snacks where Item_ID = %s", (itemid,))
                            conn.commit()
                            print("\nItem deleted successfully!\n")
                        else:
                            print("\nNo snack found with that Item ID.\n")
 
                    elif c == 6:
                        itemid = input("Enter Item ID of the beverage to delete: ")
                        cur.execute("Select Item_ID from menu_beverages where Item_ID = %s", (itemid,))
                        result = cur.fetchone()
                        if result:
                            cur.execute("Delete from menu_beverages where Item_ID = %s", (itemid,))
                            conn.commit()
                            print("\nItem deleted successfully!\n")
                        else:
                            print("\nNo beverage found with that Item ID.\n")
 
                    elif c == 7:
                        print("Logged out.\n")
	        break     
                    else:
                        print("Invalid choice!\n")
 
            else:
                print("\nIncorrect password\n")
        else:
            print("\nIncorrect Admin ID\n")
 
    elif ch == 2:
        order = []
        while True:
            print("\nCustomer Menu: ")
            print("1. View Menu")
            print("2. Add order")
            print("3. Search item")
            print("4. Calculate bill")
            print("5. Exit")
 
            ab = int(input("Enter choice (1/2/3/4/5): "))
            print()
 
            if ab == 1:
                print("1. Snacks")
                print("2. Beverages")
                cd = int(input("Enter choice (1/2): "))
                print()
 
                if cd == 1:
                    cur.execute("Select Item_ID, Item_Name, MRP from menu_snacks")
                    columns = [desc[0] for desc in cur.description]
                    table = PrettyTable()
                    table.field_names = columns
                    for row in cur.fetchall():
                        table.add_row(row)
                    print(table)
                    print()
 
                elif cd == 2:
                    cur.execute("Select Item_ID, Item_Name, MRP from menu_beverages")
                    columns = [desc[0] for desc in cur.description]
                    table = PrettyTable()
                    table.field_names = columns
                    for row in cur.fetchall():
                        table.add_row(row)
                    print(table)
                    print()
 
                else:
                    print("Invalid choice\n")
 
            elif ab == 2:
                while True:
                    print()
                    itemid = input("Enter Item ID to add to order (or 'done' to finish): ").strip()
                   
                    if itemid.lower() == "done":
                        break
 
                    cur.execute("Select Item_ID, Item_Name, MRP from menu_snacks where Item_ID = %s", (itemid,))
                    item = cur.fetchone()
                    if not item:
                        cur.execute("Select Item_ID, Item_Name, MRP from menu_beverages where Item_ID = %s", (itemid,))
                        item = cur.fetchone()
 
                    if item:  
                        item_id, name, mrp = item
                        qty = int(input(f"Enter quantity for {name}: "))
                        total = mrp * qty
                        order.append([item_id, name, qty, mrp, total])
                        if qty==1:
                            print(qty, f"{name} added to order!\n")
                        else:
                            print(qty, f"{name}s added to order!\n")
 
                    else:
                        print("Item not found in menu. Please try again.\n")
               
            elif ab==3:
                    while True:
                        print()
                        print ("Search for:")
                        print(" 1. Snacks")
                        print(" 2. Beverages")
                        print(" 3. Exit")
                        cd=int(input("Enter choice (1/2/3): "))
                        print()
                       
                        cur.execute("Select Item_ID, Item_Name, MRP from menu_snacks")
                        rows=cur.fetchall()
                        cur.execute("Select Item_ID, Item_Name, MRP from menu_beverages")
                        rowb=cur.fetchall()
                   
                        if cd==1:
                            table= PrettyTable()
                            table.field_names=['Item_ID', 'Item_Name', 'MRP']
                            search=input("Enter Snack to be searched: ")
 
                            found=False
                            for item in rows:
                                if search.lower() in item[1].lower():
                                    table.add_row(item)
                                    found=True
                            if found:
                                print(table)
                            else:
                                print(f"No items found matching: '{search}'\n")
 
                        elif cd==2:
                            table= PrettyTable()
                            table.field_names=["Item_ID", "Item_Name", "MRP"]
                            search=input("Enter Beverage to be searched: ")
                           
                            found=False
                            for item in rowb:
                                if search.lower() in item[1].lower():
                                    table.add_row(item)
                                    found=True
                            if found:
                                print(table)
                            else:
                                print(f"No items found matching: '{search}'\n")
 
                        elif cd==3:
                            break
 
                        else:
                            print("Invalid Option\n")
 
            elif ab == 4:  
                if order == []:
                    print("\nNo items in the order yet! \n")
                else:
                    print("\n------------------- BILL -------------------")
 
                    bill_table = PrettyTable()
                    bill_table.field_names = ["Item ID", "Name", "Qty", "MRP", "Total"]
 
                    grand_total = 0
                    for item in order:
                        item_id, name, qty, mrp, total = item
                        grand_total += total
                        bill_table.add_row([item_id, name, qty, mrp, total])
 
                    print(bill_table)
                    print("\nSubtotal:", grand_total)
 
                    coupon = input("\nDo you have a coupon? (yes/no): ").strip().lower()
                    if coupon == "yes":
                        code = input("Enter coupon code: ").strip()
                        if code == "1002":
                            discount = grand_total * 0.10  # 10% discount
                            final_total = grand_total - discount
                            print("Coupon applied successfully!")
                            print("Discount (10%):", discount)
                            print("Total Payable:", final_total)
                        else:
                            print("Invalid coupon code. No discount applied.")
                            print("Total Payable:", grand_total)
                    else:
                        print("No coupon applied.")
                        print("Total Payable:", grand_total)
 
            elif ab == 5:
                print("Thank you, Visit again!\n")
                sys.exit()
            else:
                print("Invalid Option\n")
    elif ch==3:
        print ("Thank you!\n")
        sys.exit()
    else:
        print ("Invalid Option\n")
