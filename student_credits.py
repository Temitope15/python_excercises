#program that checks student credits to determine their status
student_credit = 85
if student_credit < 0:
    print("Student credit cannot be negative!")
elif student_credit <= 23:
    print("You are a freshman! Welcome to oau")
elif student_credit <= 53:
    print("You are a sophomore.")
elif student_credit <= 83:
    print("You are a junior.")
elif student_credit > 84:
    print("Congratulations, you have completed your degree. Keep up the good work!")