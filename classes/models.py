"""
    Module for creating objects
    Student, Mark, Course, Test
    objects made from csv values
"""

"""
Student inherits from Person
Holds student name, student id, list of courses enrolled, 
and tests completed
"""
class Student():

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.courses = {}
        self.tests = {}
        self.overall_avg = 0

    def calc_course_avg(self, course_id):
        total_weight_sum = 0
        calculated_grades = []
        for test_id, test_info in self.tests.items():
            if test_info['course_id'] == str(course_id):
                weight = int(test_info['weight'])
                grade = int(test_info['mark'])
                total_weight_sum += weight
                calculated_grade = ((weight/100) * grade)
                calculated_grades.append(calculated_grade)
        
        if total_weight_sum == 100:
            for course in self.courses:
                if course == course_id:
                   self.courses[course]['grade'] = round(sum(calculated_grades), 2)
        
    def calc_overall_avg(self):
        course_grades = []
        for course in self.courses:
            course_grades.append(self.courses[course]['grade'])
        self.overall_avg = round((sum(course_grades))/(len(course_grades)), 2)
        return self.overall_avg
"""
Course
Holds course name, teacher_name, course_id, list of students
"""
class Course:

    def __init__(self, id, name, teacher_name):
        self.id = id
        self.name = name
        self.teacher_name = teacher_name
        self.tests = []

"""
Test
Holds test id, course_id, weight of test
"""
class Test:

    def __init__(self, id, course_id, weight):
        self.id = id
        self.course_id = course_id
        self.weight = weight
        self.marks = {}

"""
Mark 
Holds mark test_id, mark student_id, and mark score
"""
class Mark:

    def __init__(self, test_id, student_id, mark):
        self.test_id = test_id
        self.student_id = student_id
        self.mark = mark
    