# Online Merchandise Store

Welcome to the Online Merchandise Store project! This simple Python application allows you to manage a list of products in a virtual store and update their prices.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project consists of two classes: `Product` and `Store`. The `Product` class represents a product with a name, a code, and a price. The `Store` class represents a store with a name, a location, and a list of products. You can add, remove, and update product prices in the store.

## Features
- Create and manage products with names, codes, and prices.
- Add and remove products from the store's inventory.
- Update product prices as needed.
- View the list of products in the store.

## Getting Started
To get started with this project, you can follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Spagnuolo01233/store_&_product_class_Python.git
   cd online-merchandise-store

2. Run the application using Python. You can create your own scripts or use the provided classes to interact with the store.

## Usage

from store import Product, Store

# Create a store
my_store = Store("My Store", "123 Main Street")

# Create a product and add it to the store
product1 = Product("T-shirt", "TS001", 19.99)
my_store.add_product(product1)

# Update the product's price
product1.update_price(24.99)

# View the products in the store
my_store.show_products()

## Contributing

If you'd like to contribute to this project, please feel free to open issues or submit pull requests. We welcome your suggestions and improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
