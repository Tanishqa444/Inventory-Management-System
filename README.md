Inventory Management System

1. Project Overview

The Inventory Management System is a command-line application developed using Python. It helps users manage product records, monitor stock levels, search and sort products, and calculate the total value of inventory.

Product information is stored persistently in a JSON file.

2. Project Objectives

* Develop a functional inventory management application.
* Implement product and stock management operations.
* Store and retrieve product information using JSON.
* Practise collaborative software development using Git and GitHub.
* Demonstrate branching, commits, pull requests, code reviews and merge conflict resolution.

3. Team Members and Contributions

Team Member	Roll Number	Contributions
Tanishqa Chahal	60	Add Product, Update Product, Sort Products, View All Products
Jahnavi	32	Delete Product, Search Product, Low Stock Alert, Calculate Total Inventory Value

4. Features

The application includes eight functional features:

1. Add Product: Add a product with its ID, name, price, quantity and category.
2. Update Product: Modify existing product details.
3. Sort Products: Sort products by price or quantity.
4. View All Products: Display all stored products.
5. Delete Product: Remove a product using its name.
6. Low Stock Alert: Identify products whose stock quantity is 5 or below.
7. Search Product: Search for a product.
8. Calculate Total Inventory Value: Calculate the combined value of the inventory.

5. Technologies Used

* Python: Application development.
* JSON: Persistent product data storage.
* Git: Version control.
* GitHub: Remote repository and team collaboration.
* Visual Studio Code: Development environment.

6. Project Structure

File	Purpose
main.py	Main menu and application execution
products.py	Add, update, sort and view products
inventory.py	Delete, search, low-stock alert and inventory value
storage.py	Load and save product data
inventory.json	Stores product records
README.md	Project overview and documentation
CONTRIBUTING.md	Contribution guidelines
.gitignore	Excludes specified files from version control

7. Installation and Execution

Prerequisites

* Python installed on the system.
* Git installed on the system.

Clone the Repository

git clone https://github.com/Tanishqa444/Inventory-Management-System.git

Navigate to the Project Directory

cd Inventory-Management-System

Run the Application

python main.py

8. Sample Output

The application displays the following menu:

===== INVENTORY MANAGEMENT SYSTEM =====
1. Add Product
2. Update Product
3. Sort Products
4. View All Products
5. Delete Product
6. Low Stock Alert
7. Search Product
8. Calculate Total Inventory Value
9. Exit
Enter your choice (1-9):

9. Git and GitHub Collaboration

The project was developed collaboratively using separate feature branches:

* feature-member1 – Product management features.
* feature-member2 – Inventory management features.

Both members contributed through meaningful commits, pushed their branches, created pull requests, reviewed each other’s work and merged the feature branches into main.

A deliberate merge conflict was also created by modifying the same line in a shared file on separate branches. The conflict was resolved by combining both contributions.

10. Repository Link

Inventory Management System – GitHub Repository
https://github.com/Tanishqa444/Inventory-Management-System