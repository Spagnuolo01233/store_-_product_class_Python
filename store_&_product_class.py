class Product:
    def __init__(self, product_name, product_code, product_price):
        """
        Initialize a Product object.

        Args:
            product_name (str): The name of the product.
            product_code (str): The product code or identifier.
            product_price (float): The price of the product.
        """
        self.product_name = product_name
        self.product_code = product_code
        self.product_price = product_price

    def update_price(self, new_price):
        """
        Update the price of the product.

        Args:
            new_price (float): The new price for the product.
        """
        self.product_price = new_price

    def get_product_info(self):
        """
        Get information about the product.

        Returns:
            str: A formatted string containing product information.
        """
        return f'Product Name: {self.product_name}\nProduct Code: {self.product_code}\nPrice: £{self.product_price}'


class Store:
    def __init__(self, store_name, store_location):
        """
        Initialize a Store object.

        Args:
            store_name (str): The name of the store.
            store_location (str): The location or address of the store.
        """
        self.store_name = store_name
        self.store_location = store_location
        self.product_list = []

    def add_product(self, product):
        """
        Add a product to the store.

        Args:
            product (Product): The Product object to be added.
        """
        self.product_list.append(product)

    def remove_product(self, product_to_remove):
        """
        Remove a product from the store.

        Args:
            product (Product): The Product object to be removed.
        """
        found = False
        for product in self.product_list:
            if product == product_to_remove:
                self.product_list.remove(product_to_remove)
                print(f'The product {product.product_name} has been removed.')
                found = True
                break
        if not found:
            print('The product is not present in the list.')

    def show_products(self):
        """
        Display the list of products in the store.
        """
        for product in self.product_list:
            print(f'Product: {product.product_name}, Price: £{product.product_price}')
       
        

