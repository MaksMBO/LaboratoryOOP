class Student:
    student_number = 0

    def __init__(self, name, surname):

        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("The value must be a string")
        self.__name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError("The value must be a string")
        self.__surname = surname
