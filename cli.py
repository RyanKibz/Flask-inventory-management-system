import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())

def view_item():
    item_id = input("Enter item ID: ")
    response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())

def add_item():
    item = {
        "product_name": input("Product name: "),
        "brand": input("Brand: "),
        "price": float(input("Price: ")),
        "stock": int(input("Stock: "))
    }
    response = requests.post(f"{BASE_URL}/inventory", json=item)
    print(response.json())

def update_item():
    item_id = input("Enter item ID: ")
    data = {
        "price": float(input("New price: ")),
        "stock": int(input("New stock: "))
    }
    response = requests.patch(
        f"{BASE_URL}/inventory/{item_id}", json=data
    )
    print(response.json())

def delete_item():
    item_id = input("Enter item ID: ")
    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(response.json())

def find_product():
    barcode = input("Enter barcode: ")
    response = requests.get(f"{BASE_URL}/products/search/{barcode}")
    product = response.json()

    if response.status_code != 200:
        print(product)
        return
    print(product)

    if input("Add to inventory? (y/n): ").lower() == "y":
        product["price"] = float(input("Price: "))
        product["stock"] = int(input("Stock: "))

        response = requests.post(
            f"{BASE_URL}/inventory", json=product
        )
        print(response.json())

def main():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. View inventory")
        print("2. View item")
        print("3. Add item")
        print("4. Update item")
        print("5. Delete item")
        print("6. Find product online")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            view_inventory()
        elif choice == "2":
            view_item()
        elif choice == "3":
            add_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            find_product()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()