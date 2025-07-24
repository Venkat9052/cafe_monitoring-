menu = {
    "coffee":80,
    "tea":50,
    "sandwich":120,
    "cake":90,
    "egg puff":100,
    "pastry":70
}


def display_menu():
    print("Cafe Menu:")
    for item, price in menu.items():
        print(f"{item}: Rs {price}")


def get_order(menu):
    
    total_cost = 0
    order_item = {} 
    while True:
        item = input("please enter the item you want to  order: ").strip().lower()
        if item in menu:
            total_cost += menu[item]
            if item in order_item:
                order_item[item] +=1
            else:
                order_item[item] = 1  

            next_item = input("Do you want to order another item? (yes/no): ").strip().lower()
            if next_item.lower() != "yes":
                break
            
        else:
            print("Item not found in the menu. Please try again. check the menu for available items.")
            display_menu()

     # Display the order summary

    print("Your order summary:")
    for item, quantity in order_item.items():
        print(f"{item}: {quantity} x Rs {menu[item]} = Rs {quantity * menu[item]}")     
    
    print(f"Total cost: Rs {total_cost}")




# main function to run the program
print("Welcome to the Cafe! ")
print("Here is the menu: ")
display_menu()
get_order(menu)

print("Thank you for your order! Enjoy your meal!")
print("thank you for visiting our cafe! \n Have a great day !")


    

        
    
        

