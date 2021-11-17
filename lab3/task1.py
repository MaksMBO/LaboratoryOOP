import json
from datetime import datetime
from variables import STUDENT_TICKET, ADVANCE_TICKET, LATE_TICKET


class Person:
    def __init__(self, name, student):
        self.name = name
        self.student = student

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

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        if not isinstance(student, bool):
            raise TypeError("The value must be a bool")
        self.__student = student


class Information:
    def __init__(self):
        with open("ticket.json", 'r') as file:
            event = json.load(file)
        self.price = event['price']

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not value or not isinstance(value, (float, int)):
            raise TypeError("Price must be a number")
        self.__price = value


class Buy(Information):
    def __init__(self):
        super().__init__()
        with open("ticket.json", 'r') as file:
            event = json.load(file)
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

    def show_price(self, person):
        last_day = datetime(self.year, self.month, self.day)
        current_date = datetime.now()
        difference = last_day - current_date

        if difference.days > 0 and person.student:
            return self.price * STUDENT_TICKET
        if difference.days >= 60:
            return self.price * ADVANCE_TICKET
        if 10 <= difference.days < 60:
            return self.price
        if 0 < difference.days < 10:
            return self.price * LATE_TICKET

    @staticmethod
    def number(value):
        with open('purchased_tickets.json', 'r') as file:
            for ticket in json.load(file)["ticket"]:
                if ticket["number"] == value:
                    return f"Ticket#{ticket['number']}:\nName: {ticket['name']}\nPrice: {ticket['price']}\n\n"
            raise IndexError("Invalid argument")

    @staticmethod
    def name(person):
        with open('purchased_tickets.json', 'r') as file:
            ticket_list = []
            for ticket in json.load(file)["ticket"]:
                if ticket["name"] == person.name:
                    ticket_list.append(ticket)
            return ticket_list

    def buy_ticket(self, person):
        with open('ticket.json', 'r') as file:
            jfile = json.load(file)
        if jfile["number"] <= 0:
            raise IndexError('This number is over')
        jfile["number"] -= 1
        jfile["purchased_tickets"] += 1
        with open('purchased_tickets.json', 'r') as file:
            purchased_tickets_file = json.load(file)
        with open('purchased_tickets.json', 'w') as file:
            with open('ticket.json', 'w') as file_ticket:
                json.dump(jfile, file_ticket, indent=4)
            with open('ticket.json', 'r') as file_json:
                ticket = {"name": person.name, "number": json.load(file_json)["purchased_tickets"],
                          "price": self.show_price(person)}
            purchased_tickets_file["ticket"].append(ticket)
            json.dump(purchased_tickets_file, file, indent=4)


Maks = Person("Maks", True)
David = Person("David", False)

buy = Buy()

buy.buy_ticket(Maks)
buy.buy_ticket(Maks)
buy.buy_ticket(David)
buy.buy_ticket(Maks)

print(f"This ticket will cost: {buy.show_price(Maks)}")
print(f"This ticket will cost: {buy.show_price(David)}\n\n\n")

print(f"Tickets bought {Maks.name}:")
for tickets in buy.name(Maks):
    print(f"\tTicket#{tickets['number']}:\n\tName: {tickets['name']}\n\tPrice: {tickets['price']}\n")
print(buy.number(26))
