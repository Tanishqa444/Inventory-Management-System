import json
import os

FILE_NAME = "inventory.json"


def load_products():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_products(products):
    with open(FILE_NAME, "w") as file:
        json.dump(products, file, indent=4)