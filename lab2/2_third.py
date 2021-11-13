class Group:

    def __init__(self, *students):
        self.students = students

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, students):
        if not isinstance(students, tuple) or not students:
            raise TypeError("The value must be a tuple")
        for persson in students:
            if not isinstance(persson, Student):
                raise TypeError("The value must be of class Student")
        self.__students = students

    def get_students_grades(self):
        """"Returning a list of all students with their GPA"""
        return self.__students

    def sorting(self):
        """"Selects the top five, according to the average score, students"""
        return sorted(self.__students, key=lambda stud: stud.average_score)[-1:-6:-1]


class Student:
    student_number = 0

    def __init__(self, name, surname, **grades):
        Student.student_number += 1
        if Student.student_number <= 20:
            self.name = name
            self.surname = surname
            self.__student_number = Student.student_number
            self.grade = grades
        else:
            raise ValueError("The number of students cannot exceed 20")

    @property
    def average_score(self):
        """"Calculates the average score of all students in the group"""
        return sum(self.__grade.values()) / len(self.__grade)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def get_student_number(self):
        return self.__student_number

    @property
    def grade(self):
        return self

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

    @grade.setter
    def grade(self, grade):
        if not isinstance(grade, dict) or not grade:
            raise TypeError("The value must be a dictionary")
        self.__grade = grade


Maksim = Student('Maksim', 'Brediuk', maths=84, basics_of_programming=85, discrete_math=98)
Vlad = Student('Vlad', 'Melnick', maths=88, basics_of_programming=78, discrete_math=89)
David = Student('David', 'Bondar', maths=77, basics_of_programming=65, discrete_math=79)
Misha = Student('Misha', 'Golub', maths=73, basics_of_programming=89, discrete_math=90)
Andrey = Student('Andrey', 'Leshitsky', maths=89, basics_of_programming=94, discrete_math=86)
Nikolay = Student('Nikolay', 'Voitenko', maths=67, basics_of_programming=75, discrete_math=69)
Alexander = Student('Alexander', 'Pitishin', maths=86, basics_of_programming=84, discrete_math=87)
Valentine = Student('Valentine', 'Bondarchuk', maths=77, basics_of_programming=88, discrete_math=91)
Evgeniy = Student('Evgeniy', 'Stepura', maths=80, basics_of_programming=80, discrete_math=99)
Evgen = Student('Evgeniy', 'Stepura', maths=80, basics_of_programming=80, discrete_math=99)
Evgeni = Student('Evgeni', 'Stepura', maths=87, basics_of_programming=78, discrete_math=96)
Evge = Student('Evge', 'Stepura', maths=96, basics_of_programming=79, discrete_math=95)
Evg = Student('Evg', 'Stepura', maths=66, basics_of_programming=74, discrete_math=87)
Ev = Student('Ev', 'Stepura', maths=79, basics_of_programming=57, discrete_math=89)
E = Student('E', 'Stepura', maths=86, basics_of_programming=86, discrete_math=96)
Alexande = Student('E', 'Stepura', maths=84, basics_of_programming=82, discrete_math=89)
Alexand = Student('Ev', 'Stepura', maths=77, basics_of_programming=76, discrete_math=79)
Alexan = Student('Evg', 'Stepura', maths=69, basics_of_programming=68, discrete_math=67)
Alexa = Student('Evge', 'Stepura', maths=96, basics_of_programming=79, discrete_math=76)
Alex = Student('Evgen', 'Stepura', maths=86, basics_of_programming=96, discrete_math=95)
# Ale = Student('Evgeni', 'Stepura', maths=78, basics_of_programming=81, discrete_math=92)


group = Group(Maksim, Vlad, David, Misha, Andrey, Nikolay, Alexander, Valentine, Evgeniy, Evgen, Evgeni, Evge, Evg, Ev,
              E, Alexande, Alexand, Alexan, Alexa, Alex)

for student in group.get_students_grades():
    print(f"Name: {student.name}, student number: {student.get_student_number} ,"
          f" average score:  {round(student.average_score, 2)}")
print("\n\n")
for student in group.sorting():
    print(f"Name: {student.name}, student number: {student.get_student_number} ,"
          f" average score:  {round(student.average_score, 2)}")