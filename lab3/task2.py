import json
from datetime import datetime
from variables import DATE_COEFFICIENT, PIZZA_OF_THE_DAY, HAWAIIAN, CAPRICIOUS, CALZONE, FOUR_CHEESES, DIABOLA, \
    SICILIAN, MARGARITA, HAM, MOZZARELLA_CHEESE, CHICKEN_BREAST, PINEAPPLE, CHAMPION, FOR_NAME, FOR_NUMBER, YES


class Person:
    def __init__(self, name, id_person):
        self.id_person = id_person
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("The value must be a string")
        self.__name = name

    @property
    def id_person(self):
        return self.__id_person

    @id_person.setter
    def id_person(self, id_person):
        if not isinstance(id_person, int):
            raise TypeError("The value must be a int")
        self.__id_person = id_person


class Information:
    def __init__(self):
        with open("pizza.json", 'r') as file:
            event = json.load(file)['price']
        self.price_hawaiian = event['hawaiian']
        self.price_capricious = event['capricious']
        self.price_calzone = event['calzone']
        self.price_four_cheeses = event['four cheeses']
        self.price_diabola = event['diabola']
        self.price_sicilian = event['sicilian']
        self.price_margarita = event['margarita']

    @property
    def price_hawaiian(self):
        return self.__price_hawaiian

    @price_hawaiian.setter
    def price_hawaiian(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_hawaiian = value

    @property
    def price_capricious(self):
        return self.__price_capricious

    @price_capricious.setter
    def price_capricious(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_capricious = value

    @property
    def price_calzone(self):
        return self.__price_calzone

    @price_calzone.setter
    def price_calzone(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_calzone = value

    @property
    def price_four_cheeses(self):
        return self.__price_four_cheeses

    @price_four_cheeses.setter
    def price_four_cheeses(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_four_cheeses = value

    @property
    def price_diabola(self):
        return self.__price_diabola

    @price_diabola.setter
    def price_diabola(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_diabola = value

    @property
    def price_sicilian(self):
        return self.__price_sicilian

    @price_sicilian.setter
    def price_sicilian(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_sicilian = value

    @property
    def price_margarita(self):
        return self.__price_margarita

    @price_margarita.setter
    def price_margarita(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price_margarita = value


class Pizza(Information):
    def __init__(self):
        super().__init__()
        with open('bought_pizza.json', 'w') as file:
            file_in = {"pizza": []}
            json.dump(file_in, file, indent=4)

    @staticmethod
    def my_order():
        order = int(input('''Choose one of the options:
 1.pizza of the day
 2.hawaiian
 3.capricious
 4.calzone
 5.four cheeses
 6.diabola
 7.sicilian
 8.margarita\n'''))
        if not order or not isinstance(order, int):
            raise TypeError("Order must be a int")
        if not 0 < order <= 8:
            raise RuntimeError("The value must be less than 8 and greater than 0")
        return order

    @staticmethod
    def my_ingredients():
        ingredient = int(input('''Choose what you want to add:
 1.ham
 2.mozzarella cheese
 3.chicken breast
 4.pineapple
 5.champion\n'''))
        if not ingredient or not isinstance(ingredient, int):
            raise TypeError("Ingredient must be a int")
        if not 0 < ingredient <= 5:
            raise RuntimeError("The value must be less than 5 and greater than 0")
        return ingredient

    def my_addition(self):
        add = []
        while True:
            addition = int(input('''Want to add an ingredients?
  1.yes
  2.no\n'''))
            if not addition or not isinstance(addition, int):
                raise TypeError("Ingredient must be a int")
            if not 0 < addition <= 3:
                raise RuntimeError("The value must be less than 3 and greater than 0")
            if addition == YES:
                add.append(' '.join(self.add_ingredients()))
            else:
                break
        return add

    def show_pizza(self):
        order = self.my_order()

        if order == PIZZA_OF_THE_DAY:
            order = datetime.today().weekday() + DATE_COEFFICIENT

        if order == HAWAIIAN[FOR_NUMBER]:
            return self.price_hawaiian, HAWAIIAN[FOR_NAME]
        if order == CAPRICIOUS[FOR_NUMBER]:
            return self.price_capricious, CAPRICIOUS[FOR_NAME]
        if order == CALZONE[FOR_NUMBER]:
            return self.price_calzone, CALZONE[FOR_NAME]
        if order == FOUR_CHEESES[FOR_NUMBER]:
            return self.price_four_cheeses, FOUR_CHEESES[FOR_NAME]
        if order == DIABOLA[FOR_NUMBER]:
            return self.price_diabola, DIABOLA[FOR_NAME]
        if order == SICILIAN[FOR_NUMBER]:
            return self.price_sicilian, SICILIAN[FOR_NAME]
        if order == MARGARITA[FOR_NUMBER]:
            return self.price_margarita, MARGARITA[FOR_NAME]

    def buy_pizza(self, person):
        present_pizza = self.show_pizza()

        with open('pizza.json', 'r') as file:
            jfile = json.load(file)
        if jfile["pizza"][present_pizza[FOR_NAME]] <= 0:
            raise IndexError('This pizza is over')
        jfile["pizza"][present_pizza[FOR_NAME]] -= 1
        with open('pizza.json', 'w') as file:
            json.dump(jfile, file, indent=4)
        with open('bought_pizza.json', 'r') as file:
            buy_pizza = json.load(file)
            with open('bought_pizza.json', 'w') as write_file:
                add = self.my_addition()
                my_pizza = {"Name": person.name, "Id": person.id_person, "Title": present_pizza[FOR_NAME],
                            "Price": present_pizza[FOR_NUMBER], "Ingredients": add}

                buy_pizza["pizza"].append(my_pizza)
                json.dump(buy_pizza, write_file, indent=4)

    def add_ingredients(self):
        with open('pizza.json', 'r') as file:
            jfile = json.load(file)
        ingredient = self.my_ingredients()

        my_ingredient = []

        if ingredient == HAM[FOR_NUMBER]:
            if jfile["ingredients"][HAM[FOR_NAME]] <= 0:
                raise IndexError('This ingredients is over')
            jfile["ingredients"][HAM[FOR_NAME]] -= 1
            my_ingredient.append(HAM[FOR_NAME])
        if ingredient == MOZZARELLA_CHEESE[FOR_NUMBER]:
            if jfile["ingredients"][MOZZARELLA_CHEESE[FOR_NAME]] <= 0:
                raise IndexError('This ingredients is over')
            jfile["ingredients"][MOZZARELLA_CHEESE[FOR_NAME]] -= 1
            my_ingredient.append(MOZZARELLA_CHEESE[FOR_NAME])
        if ingredient == CHICKEN_BREAST[FOR_NUMBER]:
            if jfile["ingredients"][CHICKEN_BREAST[FOR_NAME]] <= 0:
                raise IndexError('This ingredients is over')
            jfile["ingredients"][CHICKEN_BREAST[FOR_NAME]] -= 1
            my_ingredient.append(CHICKEN_BREAST[FOR_NAME])
        if ingredient == PINEAPPLE[FOR_NUMBER]:
            if jfile["ingredients"][PINEAPPLE[FOR_NAME]] <= 0:
                raise IndexError('This ingredients is over')
            jfile["ingredients"][PINEAPPLE[FOR_NAME]] -= 1
            my_ingredient.append(PINEAPPLE[FOR_NAME])
        if ingredient == CHAMPION[FOR_NUMBER]:
            if jfile["ingredients"][CHAMPION[FOR_NAME]] <= 0:
                raise IndexError('This ingredients is over')
            jfile["ingredients"][CHAMPION[FOR_NAME]] -= 1
            my_ingredient.append(CHAMPION[FOR_NAME])

        with open('pizza.json', 'w') as file:
            json.dump(jfile, file, indent=4)
        return my_ingredient


pizza = Pizza()

Max = Person("Max", 1)
David = Person("David", 2)
pizza.buy_pizza(Max)
pizza.buy_pizza(David)
