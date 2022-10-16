from imghdr import tests
import random
import time
import json
print("Disclaimer this is a fake person with fake grades no real person had grades recorded ")
print("also thank you for using my software By: PTSCODING")

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

def get_all_studinfo():
    print(
        f'Name: {student["name"]}  \n Class {student["tclass"]} \n Assignments: {student["assignment"]} \n Tests: {student["test"]} \n'
    )
    print(
        f"{student['name']}'s averages in every type of class is ",
        round(calculate_total_average(student)), "\n"
    )
    print(
        f"{student['name']}'s letter grade is ",
        assign_letter_grade((calculate_total_average(student))), "\n"
    )
    print(
        f"Now that you know {student['name']}'s grade you can now leave. \nHave a great day! :)")


