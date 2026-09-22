inventory ={"laptop" : {"quantity": 10, "price": 1000, "category": "electronics"}, 
            "mouse" : {"quantity": 50, "price": 20, "category": "electronics"},
             "keyboard" : {"quantity": 30, "price": 50, "category": "electronics"}}
categories = {"electronics"}

def view_invenotry():
    print(inventory)
    print("Available categories in store:", categories)
def add_item():
    item_name = input("enter_item_name: ")
    quantity = int(input("enter_quantity: "))
    price = int(input("enter price: "))
    category = input("enter category (e.g., electronics, food): ")
    inventory[item_name] = {"quantity" : quantity, "price" : price , "category": category}
    categories.add(category)
def update_item():
    item_name = input("enter item to update: ")
    if item_name in inventory:
        action = input("type 'buy' to add or 'sell' to decrease: ")
        amount = int(input("enter quantity: "))
        
        if action == "buy":
            inventory[item_name]["quantity"] += amount
            print("Stock updated!")
        elif action == "sell":
            if amount <= inventory[item_name]["quantity"]:
                inventory[item_name]["quantity"] -= amount
                print("Stock updated!")
            else:
                print("Error: Not enough quantity!")
    else:
        print("Item not found!")
def serch_item():
     item_name = input("enter item you want to search: ")
     if item_name in inventory:
            print(inventory[item_name])
     else:
         print("item not found")
def delete_item():
    item_name = input("enter item you want to delete: ")
    if item_name in inventory:
        del inventory[item_name]
        print("item deleted")
    else:
        print("item not found")
def total_value():
     total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
     print(f"Total value of inventory: {total_value}")

while True:
    print("1. view inventory")
    print("2. add item") 
    print("3. update item")
    print("4. search item")
    print("5. delete item")
    print("6. Total value of inventory")
    print("7. exit")
    choice = input("enter your choice: ")
    if choice == "1" or choice == "view inventory":
        view_invenotry()
    elif choice == "2" or choice == "add item":
        add_item()
    elif choice == "3" or choice == "update item":
        update_item()
    elif choice == "4" or choice == "search item":
         serch_item()
    elif choice == "5" or choice == "delete item":
         delete_item()
    elif choice == "6" or choice == "total value of inventory": 
         total_value()
    elif choice == "7" or choice == "exit":
         break
         


        