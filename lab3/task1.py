import json
from datetime import datetime
from variables import STUDENT_TICKET, ADVANCE_TICKET, LATE_TICKET, ZERO, SIXTY, TEN


class Person:
    def __init__(self, name):
        """Gets the name of the person and finds out if he is a student"""
        self.name = name

        with open('purchased_tickets.json', 'w') as file:
            file_in = {"ticket": []}
            json.dump(file_in, file, indent=4)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("The value must be a string")
        self.__name = name


class Regular_ticket:
    def __init__(self):
        """gets the price of pizza"""
        with open("ticket.json", 'r') as file:
            event = json.load(file)
        self.price = event['price']
        self.year = event['year']
        self.month = event['month']
        self.day = event['day']

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not value or not isinstance(value, int):
            raise TypeError("Year must be a number")
        self.__year = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if not value or not isinstance(value, int):
            raise TypeError("Month must be a number")
        self.__month = value

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not value or not isinstance(value, int):
            raise TypeError("Day must be a number")
        self.__day = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price = value

    def show_price(self):
        return self.price

    @staticmethod
    def number(value):
        if not value or not isinstance(value, int):
            raise RuntimeError("The number must be int")
        with open('purchased_tickets.json', 'r') as file:
            for tickets in json.load(file)["ticket"]:
                if tickets["number"] == value:
                    return f"Ticket#{tickets['number']}:\nName: {tickets['name']}\nPrice: {tickets['price']}\n\n"
            raise IndexError("Invalid argument")

    @staticmethod
    def name(person):
        if not person or not isinstance(person, Person):
            raise RuntimeError("The number must be int")
        with open('purchased_tickets.json', 'r') as file:
            ticket_list = []
            for tickets in json.load(file)["ticket"]:
                if tickets["name"] == person.name:
                    ticket_list.append(tickets)
            return ticket_list

    def price_tickets(self):
        last_day = datetime(self.year, self.month, self.day)
        current_date = datetime.now()
        difference = last_day - current_date
        if difference.days >= SIXTY:
            return self.price * ADVANCE_TICKET
        if TEN <= difference.days < SIXTY:
            return self.price
        if ZERO < difference.days < TEN:
            return self.price * LATE_TICKET

    def buy_ticket(self, person):
        with open('ticket.json', 'r') as file:
            jfile = json.load(file)
        if jfile["number"] <= 0:
            raise IndexError('This number is over')
        jfile["number"] -= 1
        jfile["purchased_tickets"] += 1
        with open('purchased_tickets.json', 'r') as file:
            purchased_tickets_file = json.load(file)
        with open('ticket.json', 'w') as file_ticket:
            json.dump(jfile, file_ticket, indent=4)
        with open('purchased_tickets.json', 'w') as file:
            with open('ticket.json', 'r') as file_json:
                tickets = {"name": person.name, "number": json.load(file_json)["purchased_tickets"],
                           "price": self.price_tickets()}
            purchased_tickets_file["ticket"].append(tickets)
            json.dump(purchased_tickets_file, file, indent=4)


class Student_ticket(Regular_ticket):
    def __init__(self):
        super().__init__()
        self.student_ticket_price = self.price * STUDENT_TICKET

    def price_tickets(self):
        return self.student_ticket_price


student_ticket = Student_ticket()
regular_ticket = Regular_ticket()

Maks = Person("Maks")
David = Person("David")

print(f'Price student ticket: {student_ticket.price_tickets()}')
print(f'Price regular ticket: {regular_ticket.price_tickets()}\n\n')

regular_ticket.buy_ticket(Maks)
regular_ticket.buy_ticket(Maks)
regular_ticket.buy_ticket(Maks)
regular_ticket.buy_ticket(David)
student_ticket.buy_ticket(Maks)

print(f'{regular_ticket.number(65)}')

print("Tickets bought by Maks: ")
for i in range(len(regular_ticket.name(Maks))):
    print('\n '.join([f' {key.capitalize()}: {value}' for key, value in regular_ticket.name(Maks)[i].items()]) + "\n")
