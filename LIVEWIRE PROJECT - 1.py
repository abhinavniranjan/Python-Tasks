#project-1
#abhinav
import datetime
import random


def welcome():
    print("\n========================================")
    print("        SIMPLE SHOPPING SYSTEM         ")
    print("========================================")

    name = input("Enter Customer Name: ")

    print("\nHello", name)
    print("Welcome to Shopping Billing System")
    print("========================================\n")

    return name


def show_time():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def bill_id():
    return "BILL" + str(random.randint(10000, 99999))


def add_item(cart, total):

    print("\n------------ ADD ITEM ------------")

    name = input("Enter product name: ")

    try:
        price = float(input("Enter product price: "))
        qty = int(input("Enter quantity: "))
    except:
        print("Invalid input!")
        return cart, total

    if price <= 0 or qty <= 0:
        print("Invalid values!")
        return cart, total

    subtotal = price * qty

    item = {
        "name": name,
        "price": price,
        "qty": qty,
        "subtotal": subtotal
    }

    cart.append(item)
    total = total + subtotal

    print(name, "added successfully!")
    print("Subtotal:", subtotal)

    return cart, total


def show_cart(cart, total):

    print("\n=========== CART ITEMS ===========")

    if len(cart) == 0:
        print("Cart is empty!")
        return

    i = 1

    for item in cart:
        print(i, ")")
        print(" Name :", item["name"])
        print(" Price:", item["price"])
        print(" Qty  :", item["qty"])
        print(" Sub  :", item["subtotal"])
        print("--------------------------------")
        i += 1

    print("TOTAL:", total)


def search_item(cart):

    print("\n------------ SEARCH ITEM ------------")

    if len(cart) == 0:
        print("Cart empty!")
        return

    name = input("Enter product name: ")

    found = False

    for item in cart:
        if name.lower() in item["name"].lower():
            print("\nFOUND ITEM")
            print("Name :", item["name"])
            print("Price:", item["price"])
            print("Qty  :", item["qty"])
            print("Subtotal:", item["subtotal"])
            found = True

    if not found:
        print("Item not found")


def discount(amount):

    if amount >= 5000:
        return amount * 0.20
    elif amount >= 3000:
        return amount * 0.15
    elif amount >= 2000:
        return amount * 0.10
    elif amount >= 1000:
        return amount * 0.05
    else:
        return 0


def gst(amount):
    return amount * 0.18


def cart_summary(cart, total, name):

    print("\n------------ CART SUMMARY ------------")

    print("Customer:", name)
    print("Total Items:", len(cart))
    print("Total Amount:", total)

    if len(cart) > 0:
        print("Average Price:", total / len(cart))


def generate_bill(cart, total, name):

    print("\n########################################")
    print("              FINAL BILL              ")
    print("########################################")

    print("Customer Name:", name)
    print("Bill ID      :", bill_id())
    print("Date & Time  :", show_time())
    print("----------------------------------------")

    if len(cart) == 0:
        print("No items purchased!")
        return

    i = 1

    for item in cart:
        print(i, item["name"], "|", item["qty"], "x", item["price"], "=", item["subtotal"])
        i += 1

    print("----------------------------------------")

    print("TOTAL:", total)

    d = discount(total)
    print("DISCOUNT:", d)

    after = total - d

    g = gst(after)
    print("GST:", g)

    final = after + g

    print("----------------------------------------")
    print("FINAL AMOUNT:", final)
    print("########################################")

    print("\nThank you for shopping with us!")
    print("Visit again!")


def clear_cart():

    print("Cart cleared successfully!")
    return [], 0


def menu():

    cart = []
    total = 0

    name = welcome()

    while True:

        print("\n============== MENU ==============")
        print("1. Add Item")
        print("2. Show Cart")
        print("3. Search Item")
        print("4. Cart Summary")
        print("5. Generate Bill")
        print("6. Clear Cart")
        print("7. Exit")
        print("==================================")

        try:
            choice = int(input("Enter choice: "))
        except:
            print("Invalid input!")
            continue

        if choice == 1:
            cart, total = add_item(cart, total)

        elif choice == 2:
            show_cart(cart, total)

        elif choice == 3:
            search_item(cart)

        elif choice == 4:
            cart_summary(cart, total, name)

        elif choice == 5:
            generate_bill(cart, total, name)

        elif choice == 6:
            cart, total = clear_cart()

        elif choice == 7:
            print("\nThank you", name)
            print("Have a great day!")
            break

        else:
            print("Wrong option selected")


menu()
