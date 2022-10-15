import time
import random
names = ["Jake", "Jack", "Jason"]
classes = "Math", "Science", "SS", "Writing", "Grammar"
student_name = names[random.randint(0, 2)]
student_class = [random.choice(classes)]
assignment_grades = [
    random.randint(70, 100),
    random.randint(0, 100),
    random.randint(0, 100),
    random.randint(0, 100),
]
test_grades = [random.randint(70, 100), random.randint(70, 100)]
participation_grade = [
    random.randint(0, 100),
    random.randint(0, 100),
    random.randint(0, 100), ]
student = [participation_grade, test_grades, assignment_grades]


def get_time():
    return time.localtime


def get_average(a: list):
    total_sum = sum(a)
    total_sum = float(total_sum)
    return total_sum / len(a)


def power(a, power):
    return pow(a, power)


def calculate_total_average(students):
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
    else:
        return "F"
