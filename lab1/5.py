class Student(object):
    c = 2

    def __init__(self, first_name, second_name, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        for first in kwargs:
            self.__dict__[first] = kwargs[first]
            Student.c += 1

    def __str__(self):
        return ", ".join(list(map(str, self.__dict__.values())))

    @classmethod
    def method(cls):
        return cls.c


x = Student("asdfas", "sdfsd", h=180, w=70)
print(x.__dict__)
print(x)
print(x.method())
