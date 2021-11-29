from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int):
            raise TypeError("The entered value is of the wrong type")
        if not denominator or not denominator:
            raise ValueError("Cannot be divided by zero")

        self.__numerator = numerator
        self.__denominator = denominator

    def fraction_reduction(self):
        greatest_common_divisor = gcd(self.__numerator, self.__denominator)
        if greatest_common_divisor:
            return self.__numerator // greatest_common_divisor, self.__denominator // greatest_common_divisor

    def result(self):
        return self.__numerator / self.__denominator

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
        if self.__numerator == other.__numerator:
            if self.__denominator == other.__denominator:
                return "They are equal"
        return "They are not equal"

    def __str__(self):
        return "/".join(map(str, rational.fraction_reduction()))


rational = Rational(2, 6)
rational2 = Rational(-1, 6)
rational3 = Rational(2, 6)

print(rational == rational2)
print(rational == rational3)

print(f"Simple fraction: {rational}")
print(f"In decimal: {rational.result()}")
