class Category:
    total_categories = 0
    total_unique_products = 0

    def __init__(self, title, description, goods):
        self.title = title
        self.description = description
        self.goods = goods
        Category.total_categories += 1
        Category.total_unique_products += len(goods)


class Product:
    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)
