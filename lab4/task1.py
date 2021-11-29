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

    def multiplication(self, new_numerator=1, new_denominator=1):
        if not isinstance(new_numerator, int) or not isinstance(new_denominator, int):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * new_numerator
        self.__denominator = self.__denominator * new_denominator

    def division(self, new_numerator=1, new_denominator=1):
        if not isinstance(new_numerator, int) or not isinstance(new_denominator, int):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * new_denominator
        self.__denominator = self.__denominator * new_numerator

    def sum(self, new_numerator=0, new_denominator=1):
        if not isinstance(new_numerator, int) or not isinstance(new_denominator, int):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * new_denominator + self.__denominator * new_numerator
        self.__denominator = self.__denominator * new_denominator

    def minus(self, new_numerator=0, new_denominator=1):
        if not isinstance(new_numerator, int) or not isinstance(new_denominator, int):
            raise TypeError("The entered value is of the wrong type")
        self.__numerator = self.__numerator * new_denominator - self.__denominator * new_numerator
        self.__denominator = self.__denominator * new_denominator


rational = Rational(2, 6)
rational.division(4, 6)
result = "/".join(map(str, rational.fraction_reduction()))
print(f"Simple fraction: {result}")
print(f"In decimal: {rational.result()}")

