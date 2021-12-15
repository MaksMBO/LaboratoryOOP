from datetime import datetime


class Individual:
    def __init__(self, name, surname, patronymic, year, month, day, gender):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.date_nation = datetime(year, month, day)
        self.gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__name = value

    @property
    def date_nation(self):
        return self.__date_nation

    @date_nation.setter
    def date_nation(self, value):
        if not isinstance(value, datetime):
            raise TypeError("The value must be a string")
        self.__date_nation = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__surname = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__patronymic = value

    @property
    def gender(self):
        return self.__patronymic

    @gender.setter
    def gender(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        if value != 'male' and value != 'female':
            raise ValueError("Incorrect data")
        self.__gender = value

    def __str__(self):
        return f"{self.__name}, {self.__surname}, {self.__patronymic}, {self.__date_nation}, {self.__gender} "


class Servant(Individual):
    def __init__(self, name, surname, patronymic, year, month, day, gender, organization, specialty_diploma, position,
                 salary, experience):
        super().__init__(name, surname, patronymic, year, month, day, gender)
        self.organization = organization
        self.specialty_diploma = specialty_diploma
        self.position = position
        self.salary = salary
        self.experience = experience

    @property
    def organization(self):
        return self.__organization

    @organization.setter
    def organization(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__organization = value

    @property
    def specialty_diploma(self):
        return self.__specialty_diploma

    @specialty_diploma.setter
    def specialty_diploma(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__specialty_diploma = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, str):
            raise TypeError("The value must be a string")
        self.__position = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise TypeError("The value must be a int")
        self.__salary = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if not isinstance(value, int):
            raise TypeError("The value must be a int")
        if value < 0:
            raise ValueError("Incorrect data")
        self.__experience = value

    def __str__(self):
        return f"{self.__name}, {self.__surname}, {self.__patronymic}, {self.__date_nation}, {self.__gender}, " \
               f"{self.__organization}, {self.__specialty_diploma}, {self.__position}, {self.__salary}, " \
               f"{self.__experience}"


class Organization:
    def __init__(self, *servant):
        self.servant = servant
        self.my_list_person = []
        self.counter = 0

    @property
    def servant(self):
        return self.__servant

    @servant.setter
    def servant(self, value):
        if not isinstance(value, tuple):
            raise TypeError("The value must be a Several")
        for persson in value:
            if not isinstance(persson, Servant):
                raise TypeError("The value must be of class Servant")
        self.__servant = value

    # def minimum_length_of_service(self, minimum_years):

    def __next__(self):
        limit = len(self.__servant)
        if len(self.my_list_person) < limit:
            self.my_list_person.append(self.__servant[self.counter])
            self.counter += 1
            return self.my_list_person[self.counter - 1]
        else:
            raise StopIteration("Iterations ended")

    def __iter__(self):
        return self

    def __str__(self):
        for person in self.__servant:
            return f"{person.name}, {person.surname}, {person.patronymic}, {person.date_nation}, {person.gender}, " \
                   f"{person.organization}, {person.specialty_diploma}, {person.position}, {person.salary}, " \
                   f"{person.experience}"

    def check_experience(self, minimal):
        count = 0
        for i in range(len(self.__servant)):
            if self.__next__().experience >= minimal:
                count += 1
        return count


first = Servant("Max", "Brediyk", "Oleksandrovich", 2003, 11, 12, 'male', 'Microsoft', "software engineering",
                'trainee',
                12000, 4)
second = Servant("Dvaid", "Bondar", "Taichich", 2000, 1, 3, 'male', "Google", "cook", "chief", 30000, 12)
third = Servant("March", "Simpson", "Ollotions", 1989, 3, 2, 'female', "The Simpson", "actor", "actor", 20000, 35)

organization = Organization(first, second, third)
print(organization)
print(organization.check_experience(5))
