from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, value):
        if not isinstance(value, int):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = value

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, value):
        if not isinstance(value, int):
            raise TypeError("The entered value is of the wrong type")
        if value == 0:
            raise ValueError("Cannot be divided by zero")
        self.__denominator = value

    def fraction_reduction(self):
        greatest_common_divisor = gcd(self.__numerator, self.__denominator)
        if greatest_common_divisor:
            return self.__numerator // greatest_common_divisor, self.__denominator // greatest_common_divisor

    def result(self):
        return round(self.__numerator / self.__denominator, 2)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * other.__numerator
        self.__denominator = self.__denominator * other.__denominator

    def __truediv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        if other.__denominator == 0:
            raise ZeroDivisionError("Cannot be divided by zero!")
        self.__numerator = self.__numerator * other.__denominator
        self.__denominator = self.__denominator * other.__numerator

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        self.__denominator = self.__denominator * other.__denominator

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        self.__denominator = self.__denominator * other.__denominator

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator

    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        return self.__numerator * other.__denominator != other.__numerator * self.__denominator

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        return self.__numerator * other.__denominator <= other.__numerator * self.__denominator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError("The entered value is of the wrong type")
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator

    def __str__(self):
        return "/".join(map(str, self.fraction_reduction()))


rational = Rational(2, 6)
rational2 = Rational(-1, 6)
rational3 = Rational(2, 6)

rational2 + rational
rational2 - rational
rational2 * rational
rational2 / rational
print(f"rational2 : {rational2}\n")

print(f"rational: {rational}, in decimal: {rational.result()}")
print(f"rational2: {rational2}, in decimal: {rational2.result()}")
print(f"rational3: {rational3}, in decimal: {rational3.result()}\n")

print(f"rational == rational2 --> {rational == rational2}")
print(f"rational != rational2 --> {rational != rational2}")
print(f"rational < rational2 --> {rational < rational2}")
print(f"rational <= rational3 --> {rational <= rational3}")
print(f"rational >= rational3 --> {rational >= rational3}")
print(f"rational > rational2 --> {rational > rational2}")
