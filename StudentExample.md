# Student Example.py 

## First things first
first we need to import our other file so lets go ahead and do that:

```py
import StudentEx

```
## Next

we now need a print function to get all of our data from the other file 

```py
print(f'Name: {StudentEx.student_name}  \n Class: {StudentEx.student_class} \n Assignments: {StudentEx.assignment_grades} \n Tests: {StudentEx.test_grades} \n')

print(f"{StudentEx.student_name}'s averages in every type of class is ",round(StudentEx.calculate_total_average(StudentEx.student)),"\n",)

print(f"{StudentEx.student_name}'s letter grade is ",StudentEx.assign_letter_grade((StudentEx.calculate_total_average(StudentEx.student))),"\n",)

print(f"Now that you know {StudentEx.student_name}'s grade you can now leave. \nHave a great day! :)")
```

## We are now done