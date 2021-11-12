class Product:
    def __init__(self, price, description, dimensions):
        self.__price = price
        self.__description = description
        self.__dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def dimensions(self):
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, (int, float)) or not dimensions:
            raise TypeError("The value must be a number")
        self.__dimensions = dimensions

    @description.setter
    def description(self, description):
        if not isinstance(description, str) or not description:
            raise TypeError("The value must be a string")
        self.__description = description

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)) or price < 0 or not price:
            raise TypeError("The value must be a number and greater than zero")
        self.__price = price

    def __str__(self):
        return f"{self.description} = {self.__price}"


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("The value must be a string")
        self.__surname = surname

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if not isinstance(mobile_phone, str):
            raise ValueError('The value must be a string')
        self.__mobile_phone = mobile_phone

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError("The value must be a string")
        self.__patronymic = patronymic

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("The value must be a string")
        self.__name = name


class Order:
    def __init__(self, person, *products):
        self.__person = person
        self.__products = products

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, person):
        if not person:
            raise TypeError("No value")
        self.__person = person

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        if not products:
            raise TypeError("No value")
        self.__products = products

    def result(self):
        list_prices = []
        list_descriptions = []
        list_dimensions = []
        for i in self.__products:
            list_prices.append(i.price)
            list_descriptions.append(i.description)
            list_dimensions.append(i.dimensions)
        return list_prices, ", ".join(list_descriptions), ", ".join(
            [self.__person.surname, self.__person.name, self.__person.patronymic, self.__person.mobile_phone])

    def add(self):
        return sum(self.result()[0])

    def about_person(self):
        return self.result()[2]

    def about_list(self):
        return self.result()[1]


orange = Product(3, "orange", 1)
apple = Product(2, "apple", 1)
salt = Product(13, "salt", 1)
David = Customer("Bondar", "David", "Vitaliyovich", "+380956385033")
order = Order(David, orange, apple, salt, apple)

print(f"Information about the person: {order.about_person()}\n"
      f"Shopping list: {order.about_list()}\n"
      f"Purchase price: {order.add()}\n"
      f"\nProduct information:\n"
      f"{orange}\n"
      f"{apple}\n"
      f"{salt}"
      )

