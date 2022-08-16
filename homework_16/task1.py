"""School
Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong  to different classes, and keep in mind which are common and which are not.
For example, the first_name shouldbe a Person attribute, while salary should only be available to the teacher. """


class Person:
    def __init__(self, first_name, last_first_name, age, city, education, marital_status):
        self.first_name = first_name
        self.last_first_name = last_first_name
        self.age = age
        self.city = city
        self.education = education
        self.marital_status = marital_status


class SchoolWorker(Person):
    def __init__(self, first_name, last_first_name, age, city, education, marital_status, work_experience, salary):
        super().__init__(first_name, last_first_name, age, city, education, marital_status)
        self.salary = salary
        self.work_experience = work_experience

    def id_for_school_worker(self):
        return f'Full name {self.first_name} {self.last_first_name}. Age: {self.age}. ' \
               f'City: {self.city}. Education: {self.education}. Martial status: {self.marital_status}.' \
               f'Work experience: {self.work_experience}. salary: {self.salary} UAH.'

    def salary_for_year(self):
        if str(self.salary).isdigit():
            return f'Annual salary — {self.salary * 12} UAH.'
        else:
            print('Incorrect data of salary.')


class SchoolPrincipal(SchoolWorker):
    def __init__(self, first_name, last_first_name, age, city, education,
                 marital_status, work_experience, head_experience, salary):
        super().__init__(first_name, last_first_name, age, city, education, marital_status, work_experience, salary)
        self.head_experience = head_experience

    def id_for_school_principal(self):
        return f'Full name {self.first_name} {self.last_first_name}. Age: {self.age}. ' \
               f'City: {self.city}. Education: {self.education}. Martial status: {self.marital_status}. ' \
               f'Work experience: {self.work_experience}. Head experience: {self.head_experience}. ' \
               f'Salary: {self.salary} UAH.'


class SchoolHeadmaster(SchoolWorker):
    def __init__(self, first_name, last_first_name, age, city, education,
                 marital_status, work_experience, zone_of_respons, salary):
        super().__init__(first_name, last_first_name, age, city, education, marital_status, work_experience, salary)
        self.zone_of_respons = zone_of_respons

    def id_for_school_headmaster(self):
        return f'Full name {self.first_name} {self.last_first_name}. Age: {self.age}. ' \
               f'City: {self.city}. Education: {self.education}. Martial status: {self.marital_status}. ' \
               f'Work experience: {self.work_experience}. Zone of respons: {self.zone_of_respons}. ' \
               f'Salary: {self.salary} UAH.'


class Teacher(SchoolWorker):
    def __init__(self, first_name, last_first_name, age, city, education,
                 marital_status, work_experience, num_of_class, salary):
        super().__init__(first_name, last_first_name, age, city, education, marital_status, work_experience, salary)
        self.num_of_class = num_of_class

    def id_for_school_teacher(self):
        return f'Full name {self.first_name} {self.last_first_name}. Age: {self.age}. ' \
               f'City: {self.city}. Education: {self.education}. Martial status: {self.marital_status}. ' \
               f'Work experience: {self.work_experience}. Number of class: {self.num_of_class}. ' \
               f'Salary: {self.salary} UAH.'


class Caretaker(SchoolWorker):
    def __init__(self, first_name, last_first_name, age, city, education,
                 marital_status, work_experience, salary, schedule):
        super().__init__(first_name, last_first_name, age, city, education, marital_status, work_experience, salary)
        self.schedule = schedule


class Student(Person):
    def __init__(self, first_name, last_first_name, age, city, education, marital_status,
                 course, group, scholarship, amount_scholarship):
        super().__init__(first_name, last_first_name, age, city, education, marital_status)
        self.course = course
        self.group = group
        self.scholarship = scholarship
        self.amount_scholarship = amount_scholarship

    def id_for_student(self):
        return f'Full name {self.first_name} {self.last_first_name}. Age: {self.age}. ' \
               f'City: {self.city}. Education: {self.education}. Martial status: {self.marital_status}. ' \
               f'Курс: {self.course}. Group {self.group}. ' \
               f'Scholarship: {self.scholarship}. Amount Scholarship {self.amount_scholarship} UAH.'

    def scholarship_for_year(self):
        if bool(self.scholarship):
            if str(self.amount_scholarship).isdigit():
                return f'Amount Scholarship — {self.amount_scholarship * 12} UAH.'
            else:
                return 'Incorrect data.'
        else:
            return 'Without scholarship.'


principal_1 = SchoolPrincipal('Dmytro', 'Vyshneveckiy', 55, 'Dnipro', 'Bachelor ', 'married.', 26, 15, 16500)
print(principal_1.id_for_school_principal())
print(principal_1.salary_for_year())

headmaster_1 = SchoolHeadmaster('Diana', 'Taran', 42, 'Chernihiv', 'Bachelor', 'married', 17, 'science',
                                12500)
print(headmaster_1.id_for_school_headmaster())
print(headmaster_1.salary_for_year())

caretaker_1 = Caretaker('Oleg', 'Dmytrenko', 33, 'Kyiv', 'Secondary school',
                        'married', 17, 9500, 'weekday')
print(caretaker_1.id_for_school_worker())
print(caretaker_1.salary_for_year())

teacher_1 = Teacher('Volodymyr', 'Ivanchenko', 27, 'Kyiv', 'Bachelor', 'unmarried', 2, 8, 8500)
print(teacher_1.id_for_school_teacher())
print(teacher_1.salary_for_year())

student_1 = Student('Olena', 'Krot', 19, 'Lviv', 'Secondary school', 'unmarried', 1, 'B', True, 2000)
print(student_1.id_for_student())
print(student_1.scholarship_for_year())
