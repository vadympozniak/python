"""Product Store
Write a class Product that has three attributes:
type
name
price
Then create a class ProductStore, which will have some Products and will operate with all products in the store.
All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
Tips: Use aggregation/composition concepts while implementing the ProductStore class.
You can also implement additional classes to operate on a certain type of product, etc.
Also, the ProductStore class must have the following methods:
add(product, amount) - adds a specified quantity of a single product with a predefined price premium
for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified
by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store if available,
in other case raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store."""


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        try:
            if int(price) < 0:
                print(f'The price cannot be a negative value.')
                self.price = 0
            else:
                self.price = round(float(price), 2)
        except ValueError:
            print(f'The price must be entered in numbers.')
            self.price = 0


class ProductStore(Product):
    def __init__(self):
        self.product_list = []
        self.total_income = 0

    def add(self, product, amount):
        try:
            if int(amount) < 0:
                print(f'The quantity of the product cannot be less than zero.')
                amount = 0
            else:
                self.product_list.append({'type': product.type, 'name': product.name,
                                          'price': round(product.price * 0.7, 2), 'amount': amount})
                print(f'New product: {product.name} ({product.type}), '
                      f'30% off price: {round(product.price * 0.7, 2)} UAH. Amount: {amount}.\n\n')
        except ValueError:
            print(f'The product quantity must be a number.')

    def set_discount(self, identifier, percent, identifier_type='name'):
        try:
            if int(percent) < 0:
                print(f'The discount cannot be a negative value.')
                percent = 0
        except ValueError:
            print(f'The discount must be entered in numbers.')
            percent = 0

        for product in self.product_list:
            if identifier in product[identifier_type]:
                product['price'] *= (1 - (percent / 100))
                product['price'] = round(product['price'], 2)
                print(f"Promotional product: {product['name']} ({product['type']}), "
                      f" {percent}% off price: {product['price']} UAH. "
                      f"Amount: {product['amount']}.\n\n")

    def sell_product(self, product_name, amount):
        try:
            if int(amount) < 0:
                print(f'The quantity of goods sold cannot be less than zero.')
                amount = 0
        except ValueError:
            print(f'The quantity of the item sold must be a number. ')

        for product in self.product_list:
            if product['name'] == product_name:
                if product['amount'] > amount:
                    product['amount'] -= amount
                    print(f"Sold product: {product['name']} ({product['type']}). Sold amount: {amount}.")
                    self.total_income += round(amount * product['price'], 2)
                    print(f"Profit: {round(amount * product['price'], 2)} UAH.\n\n")
                elif product['amount'] > 0:
                    print(f"Product {product['name']} ({product['type']}) less ({product['amount']} amount), "
                          f"than buyers want ({amount} amount). "
                          f"We sell only this quantity")
                    self.total_income += round(product['amount'] * product['price'], 2)
                    print(f"Profit: "
                          f"{round(product['amount'] * product['price'], 2)} UAH.\n\n")
                    product['amount'] = 0
                else:
                    print(f"Product {product['name']} ({product['type']}) does not have.")

    def get_income(self):
        return self.total_income

    def get_all_products(self):
        return self.product_list

    def get_product_info(self, product_name):
        product_info = []
        for product in self.product_list:
            if product['name'] == product_name:
                product_info.append((product['name'], product['amount']))
        return product_info


product_1 = Product('Drink', 'Cola', 100)
product_2 = Product('Food', 'Salad', 1)


store = ProductStore()

store.add(product_1, 10)
store.add(product_2, 300)

store.set_discount('Food', 20, 'type')
store.sell_product('Salad', 10)
store.sell_product('Salad', 300)
store.sell_product('Salad', 20)

print(f'Profit — {store.get_income()} UAH.')
print(f'All products: {store.get_all_products()}.')
print(f"Information about product balances: {store.get_product_info('Salad')}")