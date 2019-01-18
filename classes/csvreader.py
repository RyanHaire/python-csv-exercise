import csv
import os
from .models import *

"""CsvReader object"""
class CsvReader:

    # obj_type - Types supported:
    # Student, Course, Mark, Test 
    # -- based on sample csv files
    def __init__(self, csv_file, obj_type):
        self.obj_type = obj_type
        self.datasets_path = '/../datasets/'
        self.file = os.path.dirname(os.path.abspath(__file__)) + self.datasets_path + csv_file

    def change_file(self, new_file, obj_type):
        self.file = os.path.dirname(os.path.abspath(__file__)) + self.datasets_path + new_file
        self.obj_type = obj_type
    
    # return file as list without header
    def rows_as_list(self):
        rows_list = []
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            next(reader) # skip header in csv file
            rows_list = list(reader)
        return rows_list

    # create relevant objects from file
    def list_of_objects(self):
        file_data = self.rows_as_list()
        objs = []
        if self.obj_type in ['Student', 'student', 'students', 'Students']:
            # create Student objects from file data
            # Student(id, name)
            for row in file_data:
                objs.append(Student(row[0], row[1].strip()))
        elif self.obj_type in ['Course', 'course', 'courses', 'Courses']:
            # create Course objects from file data
            # Course(id, name, teacher_name)
            for row in file_data:
                objs.append(Course(row[0], row[1].strip(), row[2].strip()))
        elif self.obj_type in ['Test', 'test', 'tests', 'Tests']:
            # create Test objects from file data
            # Test(id, course_id, weight)
            for row in file_data:
                objs.append(Test(row[0], row[1], row[2]))
        elif self.obj_type in ['Mark', 'mark', 'marks', 'Marks']:
            # create Mark objects from file data
            # Mark(test_id, student_id, mark)
            for row in file_data:
                objs.append(Mark(row[0], row[1], row[2]))
        else:
            # type doesnt exist
            # use supported types
            return False
        return objs