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
        
if __name__ == "__main__":
        update_product()