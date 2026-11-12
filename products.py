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

if __name__ == "__main__":
    add_product()