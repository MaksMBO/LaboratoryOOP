class Rectangle(object):
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

    @staticmethod
    def check(value):
        if not 0 < value < 20:
            raise ValueError("Length must be greater than 0 and less than 20")

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def area(self):
        return self.__length * self.__width

    @width.setter
    def width(self, width):
        self.check(width)
        self.__width = width

    @length.setter
    def length(self, length):
        self.check(length)
        self.__length = length


rectangle = Rectangle()

try:
    rectangle.length = float(input("Length: "))
    rectangle.width = float(input("Width: "))
except ValueError or TypeError:
    print("You did not enter incorrect data!")
else:
    print(f"Length: {rectangle.length} \nWidth: {rectangle.width}")
    print(f"Perimeter: {rectangle.perimeter()}")
    print(f"Square: {rectangle.area()}")
