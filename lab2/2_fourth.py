class Node:

    def __init__(self, key, price):
        self.left = None
        self.right = None
        self.key = key
        self.price = price
        self.products = (self.key, self.price)


class TREE:

    def __init__(self):
        self.root = None

    def adding_product(self, key, price):
        """"Adds data to the tree"""
        if self.root is None:
            self.root = Node(key, price)
        else:
            self.adding_products(key, price, self.root)

    def adding_products(self, key, price, root):
        """"Adds data to the tree"""
        if key < root.key:
            if root.left is None:
                root.left = Node(key, price)
            else:
                self.adding_products(key, price, root.left)

        elif key > root.key:
            if root.right is None:
                root.right = Node(key, price)
            else:
                self.adding_products(key, price, root.right)

    def search(self, key):
        """"Find the item you want"""
        return self.searching(key, self.root)

    def searching(self, key, root):
        """"Find the item you want"""
        if key == root.key:
            return root.price
        elif key < root.key:
            return self.searching(key, root.left)
        elif key > root.key:
            return self.searching(key, root.right)


class BINARYTREE:

    def __init__(self, tree):
        self.__tree = tree

    def new_object(self, key, price):
        """"Adding items to the tree"""
        self.__tree.adding_product(key, price)

    def get_value(self, key, value):
        """"Getting a price for a certain amount of goods"""
        return value * self.__tree.search(key)


my_tree = BINARYTREE(TREE())
my_tree.new_object(3, 2)
my_tree.new_object(4, 4)
my_tree.new_object(2, 5)
my_tree.new_object(1, 34)
my_tree.new_object(5, 7)

product_code = int(input("Enter the product code: "))
product_quantity = int(input("Enter the product quantity: "))
if product_code <= 0 or product_code > 5 or product_quantity < 0:
    raise ValueError("Incorrect data")

print(f"Result: {my_tree.get_value(product_code, product_quantity)}")
