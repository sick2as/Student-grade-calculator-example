from imghdr import tests
import random
import time
import json
names = ["james", "john", "joe", "Jason", "Mick", "Nina"]
classes = ['math', 'science', 'social studies', 'reading', 'grammar']

def get_time():
    return time.localtime

def get_average(grade):
    return float(sum(grade)) / len(grade)

def calculate_total_average(students):
    assignment = get_average(students["assignment"])
    test = get_average(students["test"])
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

