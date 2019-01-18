from classes import csvreader, models
import json 

# read 'courses.csv' and make a list of Course objects
reader = csvreader.CsvReader('courses.csv', 'Course')
courses = reader.list_of_objects()

# read 'marks.csv' and make a list of Mark objects
reader.change_file('marks.csv', 'Mark')
marks = reader.list_of_objects()

# read 'students.csv' and make a list of Student objects
reader.change_file('students.csv', 'Student')
students = reader.list_of_objects()

# read 'tests.csv' and make a list of Course objects
reader.change_file('tests.csv', 'Test')
tests = reader.list_of_objects()


# this block is adding relevant information of courses, marks, tests, into appropriate student objects
for course in courses: # loops 3 times
    for test in tests: # loops 7 
        for mark in marks: # loops 19 times
            # add tests and courses to student
            for student in students: # loops 3 times
                if mark.student_id == student.id and course.id == test.course_id and test.id == mark.test_id:
                    if test.id not in student.tests:
                        student.tests[test.id] = {'course_id': test.course_id, 'weight': test.weight, 'mark': mark.mark}
                    if course.id not in student.courses:
                        student.courses[course.id] = {'course_name': course.name, 'teacher_name': course.teacher_name}


# write report card output to 'report_card.txt
f = open('report_card.txt', 'w+');
for student in students:
    f.write('Student Id: ' + student.id + ', name: '  + student.name + '\n')
    f.write('Total Average:\t\t' + str(student.calc_overall_avg()) + '%\n\n')
    for course in student.courses:
        student.calc_course_avg(course)
        f.write('\t\tCourse: ' + student.courses[course]['course_name'] + ', Teacher: ' + student.courses[course]['teacher_name']+ '\n')
        f.write('\t\tFinal Grade:\t\t' + str(student.courses[course]['grade']) + '%\n\n')


