# Why and how it works

## First how it works

well first we need some data and functions so we have the StudentEx.py file

the code looks like this

```py
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
    elif score >= 60:
        return "D"
    else:
        return "F"

```

### Basic Explanation

it gets a random name random class and grades
then the other python file imports that data and returns it

## Next

next we need somthing to go through all that data so we have StudentExample.py
the basics of it is this

### Basic Explanation

return all data from StudentEx.py
write to a json file
if the user wants can also read last output of json file
the code to do that is here

```py
import StudentEx, json

print("Thank you for using my coding By: sick2as")
o = input("Would you like to read (last output) or write to the json? ").lower()
if o == "read":
    # read file
    with open('student.json', 'r') as myfile:
        data=myfile.read()

    # parse file
    obj = json.loads(data)

    # show values
    print("Name: " + str(obj['Name']))
    print("Grades: " + str(obj['Grades']))
    print("Class: " + str(obj['Class']))
    print("Letter Grade: " + str(obj['Letter Grade']))
elif o == "write":
    print(
        f"Name: {StudentEx.student_name}  \n Class: {StudentEx.student_class} \n Assignments: {StudentEx.assignment_grades} \n Tests: {StudentEx.test_grades} \n"
    )
    print(
        f"{StudentEx.student_name}'s averages in every type of class is ",
        round(StudentEx.calculate_total_average(StudentEx.student)),
        "\n",
    )
    print(
        f"{StudentEx.student_name}'s letter grade is ",
        StudentEx.assign_letter_grade(
            (StudentEx.calculate_total_average(StudentEx.student))
        ),
        "\n",
    )
    print(
        f"Now that you know {StudentEx.student_name}'s grade you can now leave. \nHave a great day! :)"
    )

    js = {
        "Name": StudentEx.student_name,
        "Grades": StudentEx.student,
        "Class": StudentEx.student_class,
        "Letter Grade": StudentEx.assign_letter_grade(
            StudentEx.calculate_total_average(StudentEx.student)
        ),
    }
    with open("student.json", "w") as f:
        f.write(json.dumps(js))

```

## Why it works

well its really simple it just gets a few averages a random name,class then returns the data from that in a file
