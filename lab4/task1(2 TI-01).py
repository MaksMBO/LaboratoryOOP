from datetime import datetime


class Calendar:
    def __init__(self, day=datetime.now().day, month=datetime.now().month, year=datetime.now().year):
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError("The value must be a int")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("The value must be a int")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("The value must be a int")
        self.__year = year

    def __str__(self):
        return f"Year: {self.__year}, month: {self.__month}, day: {self.__day}"


today = Calendar()
print(today)
