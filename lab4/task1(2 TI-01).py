from datetime import datetime
import calendar
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
        if self.__month == FEBRUARY and calendar.isleap(self.__year) and not ZERO < days <= TWENTY_NINE:
            raise ValueError("Date must be greater than 0 and no greater than 29")
        if self.__month == FEBRUARY and not calendar.isleap(self.__year) and not ZERO < days <= TWENTY_EIGHT:
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
        if not ZERO < month <= TWELVE:
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
        self.__month += other.__month
        self.__year += other.__year

        while True:
            if self.__month > 12:
                self.__month -= TWELVE
                self.__year += ONE

            if self.__month in (APRIL, JUNE, SEPTEMBER, NOVEMBER) and self.__day > THIRTY:
                self.__day -= THIRTY
                self.__month += ONE
            elif self.__month == FEBRUARY and calendar.isleap(self.__year) and self.__day > 29:
                self.__day -= TWENTY_NINE
                self.__month += ONE
            elif self.__month == FEBRUARY and not calendar.isleap(self.__year) and self.__day > 28:
                self.__day -= TWENTY_EIGHT
                self.__month += ONE
            elif self.__day > THIRTY_ONE:
                self.__day -= THIRTY_ONE
                self.__month += ONE
            else:
                break
        return self

    def __isub__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        self.__day -= other.__day
        self.__month -= other.__month
        self.__year -= other.__year

        while True:
            if self.__month <= 0:
                self.__month += TWELVE
                self.__year -= ONE

            if self.__month in (FEBRUARY, APRIL, JUNE, AUGUST, SEPTEMBER, NOVEMBER, JANUARY) and self.__day <= 0:
                self.__day += THIRTY_ONE
                self.__month -= ONE
            elif self.__month == MARCH and calendar.isleap(self.__year) and self.__day <= 0:
                self.__day += TWENTY_NINE
                self.__month -= ONE
            elif self.__day == MARCH and not calendar.isleap(self.__year) and self.__day <= 0:
                self.__day += TWENTY_EIGHT
                self.__month -= ONE
            elif self.__day <= 0:
                self.__day += THIRTY
                self.__month -= ONE
            else:
                break
        return self

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        if self.__day == other.__day and self.__month == other.__month and self.__year == other.__year:
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        if self.__day == other.__day and self.__month == other.__month and self.__year == other.__year:
            return False
        return True

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        if self.__year < other.__year:
            return True
        if self.__year == other.__year:
            if self.__month < other.__month:
                return True
            if self.__month == other.__month:
                if self.__day < other.__day:
                    return True
        return False

    def __le__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        if self.__year < other.__year:
            return True
        if self.__year == other.__year:
            if self.__month < other.__month:
                return True
            if self.__month == other.__month:
                if self.__day <= other.__day:
                    return True
        return False

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        if self.__year > other.__year:
            return True
        if self.__year == other.__year:
            if self.__month > other.__month:
                return True
            if self.__month == other.__month:
                if self.__day > other.__day:
                    return True
        return False

    def __ge__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError("The entered value is of the wrong type")
        if self.__year > other.__year:
            return True
        if self.__year == other.__year:
            if self.__month > other.__month:
                return True
            if self.__month == other.__month:
                if self.__day >= other.__day:
                    return True
        return False

    def __str__(self):
        return f"Year: {self.__year}, month: {self.__month}, day: {self.__day}"


today = Calendar()
day2 = Calendar(1, 1, 1)
day2 += today
print(day2)

day3 = Calendar(1, 1, 1)
day2 -= day3
print(day2)

day4 = Calendar(2, 2, 2020)
day5 = Calendar(2, 2, 2020)
day6 = Calendar(29, 2, 2020)

print(f"\n{day4} --> day4")
print(f"{day5} --> day5")
print(f"{day6} --> day6\n")

print(f"day4==day5 --> {day4==day5}")
print(f"day4!=day5 --> {day4!=day5}\n")

print(f"day4<day6 --> {day4<day6}")
print(f"day4<=day6 --> {day4<=day6}")
print(f"day4<=day5 --> {day4<=day5}\n")

print(f"day4>day6 --> {day4>day6}")
print(f"day4>=day6 --> {day4>=day6}")
print(f"day4>=day5 --> {day4>=day5}")

