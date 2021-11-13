import json
from datetime import datetime


class Person:
    def __init__(self, name, student):
        self.name = name
        self.student = student

        with open('purchased_tickets.json', 'w') as file:
            file_in = {"ticket": []}
            json.dump(file_in, file, indent=4)
        with open('ticket.json', 'w') as file:
            file_in = {"number": 500, "purchased_tickets": 0, "price": 1000, "year": 2021, "month": 12, "day": 28}
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

    def get_price(self):
        with open('ticket.json', 'r') as file:
            data_file = json.load(file)
            last_day = datetime(data_file["year"], data_file["month"], data_file["day"])
            current_date = datetime.now()
            difference = last_day - current_date

            if difference.days > 0 and self.__student:
                return data_file["price"] * 0.5
            if difference.days >= 60:
                return data_file["price"] * 0.6
            if 10 <= difference.days < 60:
                return data_file["price"]
            if 0 < difference.days < 10:
                return data_file["price"] * 1.1

    def buy_ticket(self):
        with open('ticket.json', 'r') as file:
            jfile = json.load(file)
        jfile["number"] -= 1
        jfile["purchased_tickets"] += 1
        with open('purchased_tickets.json', 'r') as file:
            purchased_tickets_file = json.load(file)
        with open('purchased_tickets.json', 'w') as file:
            with open('ticket.json', 'w') as file_ticket:
                json.dump(jfile, file_ticket, indent=4)
            with open('ticket.json', 'r') as file_json:
                ticket = {"name": self.name, "number": json.load(file_json)["purchased_tickets"],
                          "price": self.get_price()}
            purchased_tickets_file["ticket"].append(ticket)
            json.dump(purchased_tickets_file, file, indent=4)

    @staticmethod
    def get_number(value):
        with open('purchased_tickets.json', 'r') as file:
            for ticket in json.load(file)["ticket"]:
                if ticket["number"] == value:
                    return f"Ticket#{ticket['number']}:\nName: {ticket['name']}\nPrice: {ticket['price']}\n\n"
            raise IndexError("Invalid argument")

    def get_name(self):
        with open('purchased_tickets.json', 'r') as file:
            ticket_list = []
            for ticket in json.load(file)["ticket"]:
                if ticket["name"] == self.__name:
                    ticket_list.append(ticket)
            return ticket_list


Maks = Person("Maks", True)
David = Person("David", False)

Maks.buy_ticket()
Maks.buy_ticket()
David.buy_ticket()
print(Maks.get_number(3))
print(f"This ticket will cost: {Maks.get_price()}")
print(f"This ticket will cost: {David.get_price()}\n\n\n")

print(f"Tickets bought {Maks.name}:")
for tickets in Maks.get_name():
    print(f"\tTicket#{tickets['number']}:\n\tName: {tickets['name']}\n\tPrice: {tickets['price']}\n")
