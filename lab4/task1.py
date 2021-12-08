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
        if isinstance(other, Rational):
            numerator = self.__numerator * other.__numerator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.__numerator * other
            return Rational(numerator, self.__denominator)
        else:
            raise TypeError("The entered value is of the wrong type")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.__denominator == 0:
                raise ZeroDivisionError("Cannot be divided by zero!")
            numerator = self.__numerator * other.__denominator
            denominator = self.__denominator * other.__numerator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            denominator = self.__denominator * other
            return Rational(self.__numerator, denominator)
        else:
            raise TypeError("The entered value is of the wrong type")

    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.__numerator + self.__denominator * other
            return Rational(numerator, self.__denominator)
        else:
            raise TypeError("The entered value is of the wrong type")

    def __sub__(self, other):
        if isinstance(other, Rational):
            numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
            denominator = self.__denominator * other.__denominator
            return Rational(numerator, denominator)
        elif isinstance(other, int):
            numerator = self.__numerator - self.__denominator * other
            return Rational(numerator, self.__denominator)
        else:
            raise TypeError("The entered value is of the wrong type")

    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator + self.__denominator * other.__numerator
            self.__denominator = self.__denominator * other.__denominator
            return self
        elif isinstance(other, int):
            self.__numerator = self.__numerator + self.__denominator * other
            return self
        else:
            raise TypeError("The entered value is of the wrong type")

    def __isub__(self, other):
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__denominator - self.__denominator * other.__numerator
            self.__denominator = self.__denominator * other.__denominator
            return self
        elif isinstance(other, int):
            self.__numerator = self.__numerator - self.__denominator * other
            return self
        else:
            raise TypeError("The entered value is of the wrong type")

    def __imul__(self, other):
        if isinstance(other, Rational):
            self.__numerator = self.__numerator * other.__numerator
            self.__denominator = self.__denominator * other.__denominator
            return self
        elif isinstance(other, int):
            self.__numerator = self.__numerator * other
            return self
        else:
            raise TypeError("The entered value is of the wrong type")

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            if other.__denominator == 0:
                raise ZeroDivisionError("Cannot be divided by zero!")
            self.__numerator = self.__numerator * other.__denominator
            self.__denominator = self.__denominator * other.__numerator
            return self
        elif isinstance(other, int):
            self.__denominator = self.__denominator * other
            return self
        else:
            raise TypeError("The entered value is of the wrong type")

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.__numerator * other.__denominator == other.__numerator * self.__denominator
        elif isinstance(other, int):
            return self.__numerator == other * self.__denominator
        else:
            raise TypeError("The entered value is of the wrong type")

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.__numerator * other.__denominator != other.__numerator * self.__denominator
        elif isinstance(other, int):
            return self.__numerator != other * self.__denominator
        else:
            raise TypeError("The entered value is of the wrong type")

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.__numerator * other.__denominator < other.__numerator * self.__denominator
        elif isinstance(other, int):
            return self.__numerator < other * self.__denominator
        else:
            raise TypeError("The entered value is of the wrong type")

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.__numerator * other.__denominator <= other.__numerator * self.__denominator
        elif isinstance(other, int):
            return self.__numerator <= other * self.__denominator
        else:
            raise TypeError("The entered value is of the wrong type")

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.__numerator * other.__denominator > other.__numerator * self.__denominator
        elif isinstance(other, int):
            return self.__numerator > other * self.__denominator
        else:
            raise TypeError("The entered value is of the wrong type")

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.__numerator * other.__denominator >= other.__numerator * self.__denominator
        elif isinstance(other, int):
            return self.__numerator >= other * self.__denominator
        else:
            raise TypeError("The entered value is of the wrong type")

    def __str__(self):
        return "/".join(map(str, self.fraction_reduction()))


rational = Rational(2, 6)
rational2 = Rational(-1, 6)
rational3 = Rational(2, 6)

rational4 = rational2 + rational
rational5 = rational4 - rational
rational6 = rational5 * rational
rational7 = rational6 / rational

rational8 = Rational(2, 7)
rational8 += 1
rational8 -= 1
rational8 *= 2
rational8 /= 2

print(f"rational: {rational}, in decimal: {rational.result()}")
print(f"rational2: {rational2}, in decimal: {rational2.result()}")
print(f"rational3: {rational3}, in decimal: {rational3.result()}")
print(f"rational4: {rational4}, in decimal: {rational4.result()}")
print(f"rational5: {rational5}, in decimal: {rational5.result()}")
print(f"rational6: {rational6}, in decimal: {rational6.result()}")
print(f"rational7: {rational7}, in decimal: {rational7.result()}")
print(f"rational8: {rational8}, in decimal: {rational8.result()}\n")

print(f"rational == rational2 --> {rational == rational2}")
print(f"rational != rational2 --> {rational != rational2}")
print(f"rational < rational2 --> {rational < rational2}")
print(f"rational <= rational3 --> {rational <= rational3}")
print(f"rational >= rational3 --> {rational >= rational3}")
print(f"rational > rational2 --> {rational > rational2}")
