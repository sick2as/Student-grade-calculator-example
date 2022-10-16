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
    print("Assignment Grades: " + str(obj['Assignment Grades']))
    print("Test Grades: " + str(obj['Test Grades']))
    print("Participation Grades: " + str(obj['Participation Grades']))
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
        "Assignment Grades": StudentEx.assignment_grades,
        "Test Grades": StudentEx.test_grades,
        "Participation Grades": StudentEx.participation_grade,
        
        "Class": StudentEx.student_class,
        "Letter Grade": StudentEx.assign_letter_grade(
            StudentEx.calculate_total_average(StudentEx.student)
        ),
    }
    with open("student.json", "w") as f:
        f.write(json.dumps(js))
