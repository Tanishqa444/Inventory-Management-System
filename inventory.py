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