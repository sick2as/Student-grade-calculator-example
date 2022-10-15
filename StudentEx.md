# First things first

we need a student and a few parameters so lets add that
```py
import random
names = ["Jake", "Jack", "Jason"]
classes = "Math", "Science", "SS", "Writing", "Grammar"
student_name = names[random.randint(0, 2)]
```
## Second

Next we need some grades so lets go ahead and program that
```py
assignment_grades = [random.randint(70, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),]
test_grades = [random.randint(70, 100), random.randint(70, 100)]
participation_grade = [random.randint(0, 100),random.randint(0, 100),random.randint(0, 100), ]
student = [participation_grade, test_grades, assignment_grades]
```
## Third

Next we need to find one of the grade averages
```py
def get_average(a: list):
    total_sum = sum(a)
    total_sum = float(total_sum)
    return total_sum / len(a)
```
## Review

so right now we should have something like this

```py
import random
names = ["Jake", "Jack", "Jason"]

classes = "Math", "Science", "SS", "Writing", "Grammar"

student_name = names[random.randint(0, 2)]

assignment_grades = [random.randint(70, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),]

test_grades = [random.randint(70, 100), random.randint(70, 100)]

participation_grade = [random.randint(0, 100),random.randint(0, 100),random.randint(0, 100), ]

student = [participation_grade, test_grades, assignment_grades]

def get_average(a: list):
    total_sum = sum(a)
    total_sum = float(total_sum)
    return total_sum / len(a)

```
## Next
now that we have one average lets get all of them

```py
def calculate_total_average(students):
    assignment = get_average(assignment_grades)
    test = get_average(test_grades)
    return 0.1 * assignment + 0.7 * test + 0.2
```
## Next on our list

Now we have to get the letter grade
```py
def assign_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"
```
## Finaly
Now we are done with the moudle!