# File Name: Module_2.py
# Name: Tyler Barnett
# Description: This app accepts student names and GPAs and determines
#              if the student qualifies for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter student's last name: ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")

    if gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")