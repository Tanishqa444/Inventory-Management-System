from storage import load_products, save_products


def delete_product():
    products = load_products()

    if not products:
        print("Inventory is empty!")
        return

    product_name = input("Enter product name to delete: ")

    for product in products:
        if product["name"].lower() == product_name.lower():
            products.remove(product)
            save_products(products)
            print("Product deleted successfully!")
            return

    print("Product not found!")


def search_product():
    products = load_products()

    if not products:
        print("Inventory is empty!")
        return

    search_name = input("Enter product name to search: ")

    for product in products:
        if search_name.lower() in product["name"].lower():
            print("\nProduct Found:")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
            print("Category:", product["category"])
            return

    print("Product not found!")

def low_stock_alert():
    products = load_products()

    if not products:
        print("Inventory is empty!")
        return

    threshold = 5
    found = False

    print("\n--- LOW STOCK ALERT ---")

    for product in products:
        if product["quantity"] <= threshold:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Quantity: {product['quantity']}"
            )
            found = True

    if not found:
        print("No low stock products!")

