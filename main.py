from products import add_product, update_product, sort_products, view_products
from inventory import delete_product, low_stock_alert, search_product, calculate_total_value


def display_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Sort Products")
    print("4. View All Products")
    print("5. Delete Product")
    print("6. Low Stock Alert")
    print("7. Search Product")
    print("8. Calculate Total Inventory Value")
    print("9. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            sort_products()
        elif choice == "4":
            view_products()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            low_stock_alert()
        elif choice == "7":
            search_product()
        elif choice == "8":
            calculate_total_value()
        elif choice == "9":
            print("Thank you for using the Inventory Management System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()