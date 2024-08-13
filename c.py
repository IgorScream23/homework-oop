class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def get_average_grade(self):
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count != 0 else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count != 0 else 0

    def __str__(self):
        avg_grade = self.get_average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}"

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.get_average_grade() < other.get_average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


def average_grade_students(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return round(total / count, 1) if count != 0 else 0


def average_grade_lecturers(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return round(total / count, 1) if count != 0 else 0


# Создание экземпляров
student_1 = Student('Ruoy', 'Eman', 'male')
student_2 = Student('John', 'Doe', 'male')

# Добавление курсов
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Git']

student_1.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Dr.', 'Strange')
lecturer_2 = Lecturer('Professor', 'X')

reviewer_1 = Reviewer('Tony', 'Stark')
reviewer_2 = Reviewer('Steve', 'Rogers')

# Присвоение курсов
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Python']

reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']

# Оценки студентов и лекторов
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

student_1.rate_lecture(lecturer_1, 'Python', 9)
student_1.rate_lecture(lecturer_1, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Python', 7)
student_2.rate_lecture(lecturer_2, 'Python', 6)

# Вывод информации
print(student_1)
print(lecturer_1)
print(reviewer_1)

# Сравнение
print(student_1 > student_2)
print(lecturer_1 < lecturer_2)

# Подсчет средней оценки
print(f"Средняя оценка за ДЗ по курсу Python: {average_grade_students([student_1, student_2], 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {average_grade_lecturers([lecturer_1, lecturer_2], 'Python')}")
