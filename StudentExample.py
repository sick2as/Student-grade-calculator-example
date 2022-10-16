import StudentEx
print("Thank you for using my coding By: sick2as")

print(
    f'Name: {StudentEx.student_name}  \n Class: {StudentEx.student_class} \n Assignments: {StudentEx.assignment_grades} \n Tests: {StudentEx.test_grades} \n'
)
print(
    f"{StudentEx.student_name}'s averages in every type of class is ",
    round(StudentEx.calculate_total_average(StudentEx.student)),
    "\n",
)
print(
    f"{StudentEx.student_name}'s letter grade is ",
    StudentEx.assign_letter_grade(
        (StudentEx.calculate_total_average(StudentEx.student))),
    "\n",
)
print(
    f"Now that you know {StudentEx.student_name}'s grade you can now leave. \nHave a great day! :)"
)
