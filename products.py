from storage import load_products, save_products


def add_product():
    products = load_products()

    print("\n--- ADD PRODUCT ---")

    try:
        product_id = int(input("Enter Product ID: "))

        for product in products:
            if product["id"] == product_id:
                print("Product ID already exists!")
                return

        name = input("Enter Product Name: ").strip()

        if not name:
            print("Product name cannot be empty!")
            return

        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        category = input("Enter Product Category: ").strip()

        if price <= 0 or quantity < 0:
            print("Price must be positive and quantity cannot be negative!")
            return

        new_product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        }

        products.append(new_product)
        save_products(products)

        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numeric values.")



def update_product():
    products = load_products()

    print("\n--- UPDATE PRODUCT ---")

    try:
        product_id = int(input("Enter Product ID to update: "))

        for product in products:
            if product["id"] == product_id:

                print("Leave a field blank to keep its current value.")

                name = input("Enter new name: ").strip()
                price = input("Enter new price: ").strip()
                quantity = input("Enter new quantity: ").strip()
                category = input("Enter new category: ").strip()

                if name:
                    product["name"] = name

                if price:
                    new_price = float(price)
                    if new_price <= 0:
                        print("Price must be positive!")
                        return
                    product["price"] = new_price

                if quantity:
                    new_quantity = int(quantity)
                    if new_quantity < 0:
                        print("Quantity cannot be negative!")
                        return
                    product["quantity"] = new_quantity

                if category:
                    product["category"] = category

                save_products(products)
                print("Product updated successfully!")
                return

        print("Product not found!")

    except ValueError:
        print("Please enter valid numeric values.")
        


def sort_products():
    products = load_products()

    if not products:
        print("No products available to sort!")
        return

    print("\n--- SORT PRODUCTS ---")
    print("1. Price: Low to High")
    print("2. Price: High to Low")
    print("3. Quantity: Low to High")
    print("4. Quantity: High to Low")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        products.sort(key=lambda p: p["price"])
    elif choice == "2":
        products.sort(key=lambda p: p["price"], reverse=True)
    elif choice == "3":
        products.sort(key=lambda p: p["quantity"])
    elif choice == "4":
        products.sort(key=lambda p: p["quantity"], reverse=True)
    else:
        print("Invalid choice!")
        return

    print("\nSorted Products:")
    for product in products:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: {product['price']} | "
            f"Quantity: {product['quantity']}"
        )


def view_products():
    products = load_products()

    print("\n--- ALL PRODUCTS ---")

    if not products:
        print("No products available in inventory!")
        return

    print("-" * 75)
    print(f"{'ID':<10}{'NAME':<20}{'PRICE':<15}{'QUANTITY':<12}{'CATEGORY'}")
    print("-" * 75)

    for product in products:
        print(
            f"{product['id']:<10}"
            f"{product['name']:<20}"
            f"{product['price']:<15.2f}"
            f"{product['quantity']:<12}"
            f"{product['category']}"
        )

    print("-" * 75)
