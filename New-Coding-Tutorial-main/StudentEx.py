from imghdr import tests
import random
import time
import json

names = ["James", "John", "Joe", "Jason", "Mick", "Nina"]
classes = ["Math", "Science", "Social Studies", "Reading", "Grammar"]
rd_1 = random.randint(0, 100)
rd_2 = random.randint(70, 100)
assignment_grades = [rd_1] + [rd_2] * 2
test_grades = [rd_2] * 2
participation_grade = [rd_2] * 2
student = [participation_grade, test_grades, assignment_grades]
student_name = random.choice(names)
student_class = random.choice(classes)


def get_time():
    return time.localtime


def get_average(grade):
    return float(sum(grade)) / len(grade)


def calculate_total_average(s):
    assignment = get_average(assignment_grades)
    test = get_average(test_grades)
    return 0.1 * assignment + 0.7 * test + 0.2


def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
