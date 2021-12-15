import json
from abc import ABC, abstractmethod


class ITeacher(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, course_name):
        pass

    @abstractmethod
    def course_of_teacher(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Teacher(ITeacher):
    def __init__(self, name):
        self.name = name
        self.course = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("The value must be a string")
        self.__name = name

    def course_of_teacher(self):
        teacher = {self.__name: []}
        with open('course.json', 'r') as file:
            all_course = json.load(file)
        for course in all_course:
            if self.__name in course['teacher'] and not course['course_name'] in self.course:
                self.course.append(course['course_name'])
                teacher[self.__name].append(course)
        with open('teacher.json', 'r') as file_teacher_read:
            all_teacher = json.load(file_teacher_read)

        all_teacher.append(teacher)
        with open('teacher.json', 'w') as file_teacher_write:
            json.dump(all_teacher, file_teacher_write, indent=4)

    #

    # def teacher_add_json(self):
    #     with open('teacher.json', 'r') as file:
    #         all_teacher = json.load(file)
    #     teacher['']
    #     with open('teacher.json', 'w') as file:

    def __str__(self):
        return f"Name: {self.__name}, course: {', '.join(self.course)}"


class ICourse(ABC):

    @property
    @abstractmethod
    def course_name(self):
        pass

    @course_name.setter
    @abstractmethod
    def course_name(self, course_name):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        pass

    @property
    @abstractmethod
    def course_program(self):
        pass

    @course_program.setter
    @abstractmethod
    def course_program(self, course_name):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Course(ICourse):
    def __init__(self, course_name, teacher, course_program):
        self.course_name = course_name
        self.teacher = teacher
        self.course_program = course_program

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self, course_name):
        if not isinstance(course_name, str):
            raise TypeError("The value must be a string")
        self.__course_name = course_name

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("The value must be Teacher")
        self.__teacher = teacher.name

    @property
    def course_program(self):
        return self.__course_program

    @course_program.setter
    def course_program(self, course_program):
        if not isinstance(course_program, list):
            raise TypeError("The value must be list")
        self.__course_program = course_program

    def adding_teacher(self, new_teacher):
        if not isinstance(new_teacher, Teacher):
            raise TypeError("The value must be Teacher")
        with open('course.json', 'r') as file:
            current_rates = json.load(file)
        for iterator in range(len(current_rates)):
            if current_rates[iterator]['course_name'] == self.course_name:
                current_rates[iterator]['teacher'].append(new_teacher.name)
        with open('course.json', 'w') as file:
            json.dump(current_rates, file, indent=4)

    def __str__(self):
        return f"Course name: {self.__course_name}, teacher: {self.__teacher}, course program: {self.__course_program}"


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def local_labs(self):
        pass

    @local_labs.setter
    @abstractmethod
    def local_labs(self, laboratory):
        pass

    @abstractmethod
    def create_course(self):
        pass


class LocalCourse(Course, ILocalCourse):
    def __init__(self, course_name, teacher, course_program, local_labs):
        super().__init__(course_name, teacher, course_program)
        self.local_labs = local_labs

    @property
    def local_labs(self):
        return self.__local_labs

    @local_labs.setter
    def local_labs(self, local_labs):
        if not isinstance(local_labs, str):
            raise TypeError("The value must be str")
        self.__local_labs = local_labs

    def create_course(self):
        my_course = {'course_name': self.course_name, 'course_program': self.course_program, 'teacher': [self.teacher],
                     'local laboratory': self.local_labs}
        with open('course.json', 'r') as file:
            current_rates = json.load(file)
        current_rates.append(my_course)
        with open('course.json', 'w') as file:
            json.dump(current_rates, file, indent=4)

    def __str__(self):
        return f"Name course: {self.course_name}, teacher: {self.teacher}, course program: " \
               f"{', '.join(self.course_program)}, local laboratory: {self.local_labs}"


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def city(self):
        pass

    @city.setter
    @abstractmethod
    def city(self, city):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, course_name, teacher, course_program, city):
        super().__init__(course_name, teacher, course_program)
        self.city = city

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if not isinstance(city, str):
            raise TypeError("The value must be str")
        self.__city = city

    def create_course(self):
        my_course = {'course_name': self.course_name, 'course_program': self.course_program, 'teacher': [self.teacher],
                     'city': self.city}
        with open('course.json', 'r') as file:
            current_rates = json.load(file)
        current_rates.append(my_course)
        with open('course.json', 'w') as file:
            json.dump(current_rates, file, indent=4)

    def __str__(self):
        return f"Name course: {self.course_name}, teacher: {self.teacher}, course program: " \
               f"{', '.join(self.course_program)}, city: {self.city}"


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def adding_teacher(name):
        pass

    # @staticmethod
    # @abstractmethod
    # def adding_course(course_name, teacher, course_program):
    #     pass

    @staticmethod
    @abstractmethod
    def adding_local_course(course_name, teacher, course_program, local_labs):
        pass

    @staticmethod
    @abstractmethod
    def adding_offsite_course(course_name, teacher, course_program, city):
        pass


class CourseFactory(ICourseFactory):
    @staticmethod
    def adding_teacher(name):
        return Teacher(name)

    @staticmethod
    def adding_local_course(course_name, teacher, course_program, local_labs):
        # LocalCourse(course_name, teacher, course_program, local_labs).create_course()
        return LocalCourse(course_name, teacher, course_program, local_labs)

    @staticmethod
    def adding_offsite_course(course_name, teacher, course_program, city):
        # OffsiteCourse(course_name, teacher, course_program, city).create_course()
        return OffsiteCourse(course_name, teacher, course_program, city)


course_factory = CourseFactory()
first_teacher = course_factory.adding_teacher('Igor')
second_teacher = course_factory.adding_teacher('Slava')
first_course = course_factory.adding_local_course('Probability theory', first_teacher,
                                                  ['Bayesian formula', 'Random events'], 'Mayakovsky, 34')
second_course = course_factory.adding_offsite_course('Music', second_teacher, ['Breathing', 'Voice', 'High case'],
                                                     'Lviv')
third_course = course_factory.adding_offsite_course('German courses', second_teacher,
                                                    ['Grammar', 'Listening', 'Speaking'], 'Zhytomyr')
first_course.create_course()
second_course.create_course()
third_course.create_course()
first_teacher.course_of_teacher()
second_teacher.course_of_teacher()
print(first_teacher)
print(second_teacher)
print(first_course)
print(second_course)
print(third_course)

