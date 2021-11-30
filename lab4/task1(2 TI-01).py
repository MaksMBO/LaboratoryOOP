from datetime import datetime
from datetime import timedelta
from variables import *


class Calendar:
    def __init__(self, days=datetime.now().day, month=datetime.now().month, year=datetime.now().year):
        self.year = year
        self.month = month
        self.day = days




    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, days):
        if not isinstance(days, int):
            raise TypeError("The value must be a int")
        if self.__month in (APRIL, JUNE, SEPTEMBER, NOVEMBER):
            if not ZERO < days <= THIRTY:
                raise ValueError("Date must be greater than 0 and no greater than 30")
        if self.__month == FEBRUARY:
            if not ZERO < days <= TWENTY_EIGHT:
                raise ValueError("Date must be greater than 0 and no greater than 28")
        if not ZERO < days <= THIRTY_ONE:
            raise ValueError("Date must be greater than 0 and no greater than 31")
        self.__day = days

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError("The value must be a int")
        if not ZERO < month < TWELVE:
            raise ValueError("month must be between 0 and 12")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError("The value must be a int")
        self.__year = year

    def __iadd__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        self.__day += other.__day
        if self.__month in (APRIL, JUNE, SEPTEMBER, NOVEMBER) and self.__day > THIRTY:
            self.__day -= THIRTY
            self.__month += ONE
        elif self.__month == FEBRUARY and self.__day > TWENTY_EIGHT:
            self.__day -= TWENTY_EIGHT
            self.__month += ONE
        elif self.__day > THIRTY_ONE:
            self.__day -= THIRTY_ONE
            self.__month += ONE

        self.__month += other.__month
        if self.__month > TWELVE:
            self.__month -= TWELVE
            self.__year += 1

        self.__year += other.__year
        return self


    def __isub__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        self.day -= other.__day
        if self.__month in (FEBRUARY, APRIL, JUNE, AUGUST, SEPTEMBER, NOVEMBER, JANUARY) and self.__day <= ZERO:
            self.__day += THIRTY_ONE
            self.__month -= ONE
        elif self.__month == MARCH and self.__day <= ZERO:
            self.__day += TWENTY_EIGHT
            self.__month -= ONE
        elif self.__day <= ZERO:
            self.__day += THIRTY
            self.__month -= ONE

        self.__month -= other.__month
        if self.__month <= ZERO:
            self.__month += TWELVE
            self.__year -= ONE

        self.__year -= other.__year
        if self.__year < ZERO:
            raise ValueError("First date, less than second")
        return self




    def __str__(self):
        return f"Year: {self.__year}, month: {self.__month}, day: {self.__day}"


day = Calendar(1, 11, 2020)
day2 = Calendar(13, 11, 2020)

# day += day2
day2 -= day

print(day2)
