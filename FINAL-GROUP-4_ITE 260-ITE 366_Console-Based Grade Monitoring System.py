students = {}
subjects = {}

TEACHER_USERNAME = "teacher"
TEACHER_PASSWORD = "teacher123"

def convert_to_college_grade(percentage, subject_type):

    if subject_type == "Minor":

        if percentage >= 94.8:
            return 1.00
        elif percentage >= 89.2:
            return 1.25
        elif percentage >= 83.6:
            return 1.50
        elif percentage >= 78.0:
            return 1.75
        elif percentage >= 72.4:
            return 2.00
        elif percentage >= 66.8:
            return 2.25
        elif percentage >= 61.2:
            return 2.50
        elif percentage >= 55.6:
            return 2.75
        elif percentage >= 50.0:
            return 3.00
        else:
            return 4.00

    elif subject_type == "Major":

        if percentage >= 96.0:
            return 1.00
        elif percentage >= 91.5:
            return 1.25
        elif percentage >= 87.0:
            return 1.50
        elif percentage >= 82.5:
            return 1.75
        elif percentage >= 78.0:
            return 2.00
        elif percentage >= 73.5:
            return 2.25
        elif percentage >= 69.0:
            return 2.50
        elif percentage >= 64.5:
            return 2.75
        elif percentage >= 60.0:
            return 3.00
        else:
            return 5.00

def get_grade_description(grade):

    if grade == 1.00:
        return "Excellent"
    elif grade <= 1.75:
        return "Very Good"
    elif grade <= 2.50:
        return "Good"
    elif grade <= 3.00:
        return "Passing"
    else:
        return "Failed"

def get_score(prompt):

    while True:

        try:
            score = float(input(prompt))

            if score < 0 or score > 100:
                print("Please enter a grade from 0 to 100.")

            else:
                return score

        except ValueError:
            print("Please enter a valid number.")

def add_student():

    print("\n==============================")
    print("         ADD STUDENT")
    print("==============================")

    student_id = input("Enter Student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    valid_id = True

    for character in student_id:
        if character < "0" or character > "9":
            if character != "-":
                valid_id = False
                break

    if not valid_id:
        print("Invalid Student ID. Use numbers only, with optional hyphens.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter student's full name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    students[student_id] = {"name": name, "grades": {}}

    for code in subjects:
        students[student_id]["grades"][code] = {"P1": None, "P2": None, "P3": None}

    print("\nStudent added successfully!")

def remove_student():

    print("\n==============================")
    print("        REMOVE STUDENT")
    print("==============================")

    if len(students) == 0:
        print("There are no students.")
        return

    list_students()

    student_id = input("\nEnter Student ID to remove: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    confirm = input("Are you sure you want to remove this student? (Y/N): ").upper()

    if confirm == "Y":
        del students[student_id]
        print("Student removed successfully!")

    else:
        print("Student was not removed.")

def list_students():

    print("\n==============================")
    print("        LIST OF STUDENTS")
    print("==============================")

    if len(students) == 0:
        print("There are no students.")
        return

    for student_id, student in students.items():
        print(student_id, "-", student["name"])

def add_subject():

    print("\n==============================")
    print("          ADD SUBJECT")
    print("==============================")

    code = input("Enter Subject Code: ").strip().upper()

    if code == "":
        print("Subject code cannot be empty.")
        return

    if code in subjects:
        print("Subject already exists.")
        return

    name = input("Enter Subject Name: ").strip()

    if name == "":
        print("Subject name cannot be empty.")
        return

    print("\nSubject Type")
    print("1. Minor")
    print("2. Major")
    print("3. PE")
    print("4. NST")

    choice = input("Choose subject type: ")

    if choice == "1":
        subject_type = "Minor"
        special = ""

    elif choice == "2":
        subject_type = "Major"
        special = ""

    elif choice == "3":
        subject_type = "Minor"
        special = "PE"

    elif choice == "4":
        subject_type = "Minor"
        special = "NST"

    else:
        print("Invalid subject type.")
        return

    subjects[code] = {"name": name, "type": subject_type, "special": special}

    for student in students.values():
        student["grades"][code] = {"P1": None, "P2": None, "P3": None}

    print("\nSubject added successfully!")

def remove_subject():

    print("\n==============================")
    print("        REMOVE SUBJECT")
    print("==============================")

    if len(subjects) == 0:
        print("There are no subjects.")
        return

    list_subjects()
    code = input("\nEnter Subject Code to remove: ").strip().upper()

    if code not in subjects:
        print("Subject not found.")
        return

    print("\nSubject:", subjects[code]["name"])

    confirm = input("Are you sure you want to remove this subject? (Y/N): ").upper()

    if confirm == "Y":

        del subjects[code]

        for student in students.values():

            if code in student["grades"]:

                del student["grades"][code]

        print("Subject removed successfully!")

    else:
        print("Subject was not removed.")

def list_subjects():

    print("\n==============================")
    print("         LIST OF SUBJECTS")
    print("==============================")

    if len(subjects) == 0:
        print("There are no subjects.")
        return

    for code, subject in subjects.items():
        print(code, "-", subject["name"], "(" + subject["type"] + ")")

def input_student_scores():

    print("\n==============================")
    print("      INPUT STUDENT GRADES")
    print("==============================")

    if len(students) == 0:
        print("There are no students.")
        return

    if len(subjects) == 0:
        print("There are no subjects.")
        return

    list_students()
    student_id = input("\nEnter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    list_subjects()
    code = input("\nEnter Subject Code: ").strip().upper()

    if code not in subjects:
        print("Subject not found.")
        return

    print("\nSelect Period")
    print("1. P1")
    print("2. P2")
    print("3. P3")

    choice = input("Choose period: ")

    if choice == "1":
        period = "P1"

    elif choice == "2":
        period = "P2"

    elif choice == "3":
        period = "P3"

    else:
        print("Invalid period.")
        return

    subject_type = subjects[code]["type"]

    print("\n==============================")
    print("STUDENT:", students[student_id]["name"])
    print("SUBJECT:", subjects[code]["name"])
    print("TYPE:", subject_type)
    print("PERIOD:", period)
    print("==============================")

    if subject_type == "Minor":
        print("\nMinor Subject Weight")
        print("CS = 60%")
        print("PE = 40%")

        cs = get_score("Enter CS grade (0-100): ")
        pe = get_score("Enter PE grade (0-100): ")
        period_grade = (cs * 0.60 + pe * 0.40)

    else:
        print("\nMajor Subject Weight")
        print("CS = 55%")
        print("PE = 45%")

        cs = get_score("Enter CS grade (0-100): ")
        pe = get_score("Enter PE grade (0-100): ")
        period_grade = (cs * 0.55 + pe * 0.45)

    students[student_id]["grades"][code][period] = {"CS": cs, "PE": pe, "percentage": period_grade}

    print("\nGrade saved successfully!")
    print("Period Percentage:", round(period_grade, 2), "%")

def calculate_period_grade(student_id, code, period):
    grade_data = (students[student_id]["grades"][code][period])

    if grade_data is None:
        return None

    return grade_data["percentage"]

def calculate_subject_grade(student_id, code):

    p1 = calculate_period_grade(student_id, code, "P1")
    p2 = calculate_period_grade(student_id, code, "P2")
    p3 = calculate_period_grade(student_id, code, "P3")

    if (p1 is None or p2 is None or p3 is None):
        return p1, p2, p3, None

    final_percentage = (p1 * 0.33 + p2 * 0.33 + p3 * 0.34)
    return (p1, p2, p3, final_percentage)

def view_student_grades():

    print("\n==============================")
    print("      VIEW STUDENT GRADES")
    print("==============================")

    if len(students) == 0:
        print("There are no students.")
        return

    list_students()

    student_id = input(
        "\nEnter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    print("\nStudent:", students[student_id]["name"])
    print("Student ID:", student_id)

    total = 0
    count = 0

    for code, subject in subjects.items():
        p1, p2, p3, final_percentage = (calculate_subject_grade(student_id, code))

        print("\n------------------------------")
        print(subject["name"])
        print("Subject Type:", subject["type"])

        if p1 is not None:
            print("P1:", round(p1, 2))
        else:
            print("P1: Not yet entered")

        if p2 is not None:
            print("P2:", round(p2, 2))
        else:
            print("P2: Not yet entered")

        if p3 is not None:
            print("P3:", round(p3, 2))
        else:
            print("P3: Not yet entered")

        if final_percentage is not None:
            college_grade = (convert_to_college_grade(final_percentage, subject["type"]))
            description = (get_grade_description(college_grade))
            print("Overall Percentage:", round(final_percentage, 2), "%")
            print("Grade:", format(college_grade, ".2f"))
            print("Description:", description)

            total += final_percentage
            count += 1

        else:
            print(
                "Overall Percentage:", "Not yet complete")
            print("Grade:", "Not yet complete")

    if count > 0:
        overall_percentage = total / count

        print("\n==============================")
        print("      OVERALL ALL SUBJECTS")
        print("==============================")

        print(
            "Overall Percentage:", round(overall_percentage, 2), "%")
        print("Complete Subjects:", count)

def is_deans_list(student_id):

    total_college_grade = 0
    count = 0

    for code, subject in subjects.items():

        if subject["special"] == "PE":
            continue

        if subject["special"] == "NST":
            continue

        _, _, _, final_percentage = calculate_subject_grade(student_id, code)

        if final_percentage is None:
            continue

        college_grade = convert_to_college_grade(final_percentage, subject["type"])

        total_college_grade += college_grade
        count += 1

    if count == 0:
        return False, 0

    average_college_grade = (total_college_grade / count)

    if average_college_grade <= 1.75:
        return True, average_college_grade

    return False, average_college_grade

def deans_list():

    print("\n==============================")
    print("      DEAN'S LIST QUALIFIERS")
    print("==============================")

    if len(students) == 0:
        print("There are no students.")
        return

    qualified = False

    for student_id, student in students.items():
        status, average = is_deans_list(student_id)

        if status:
            qualified = True
            print(student["name"], "-", student_id, "- Average Grade:", format(average, ".2f"))

    if not qualified:
        print("No students currently qualify for the Dean's List.")

    print("\nPE and NST are excluded from the Dean's List calculation.")

def student_view_grades(student_id):

    print("\n==============================")
    print("          MY GRADES")
    print("==============================")

    print("Student:", students[student_id]["name"])
    print("Student ID:", student_id)

    if len(subjects) == 0:
        print("\nNo subjects available.")
        return

    total = 0
    count = 0

    for code, subject in subjects.items():
        p1, p2, p3, final_percentage = (calculate_subject_grade(student_id, code))

        print("\n------------------------------")
        print(subject["name"])
        print("Type:", subject["type"])

        if p1 is not None:
            print("P1:", round(p1, 2))
        else:
            print("P1: Not yet entered")

        if p2 is not None:
            print("P2:", round(p2, 2))
        else:
            print("P2: Not yet entered")

        if p3 is not None:
            print("P3:", round(p3, 2))
        else:
            print("P3: Not yet entered")

        if final_percentage is not None:
            college_grade = (convert_to_college_grade(final_percentage, subject["type"]))
            description = (get_grade_description(college_grade))

            print("Overall Percentage:", round(final_percentage, 2), "%")
            print("Grade:", format(college_grade, ".2f"))
            print("Description:", description)

            total += final_percentage
            count += 1

        else:
            print("Overall Percentage:", "Not yet complete")
            print("Grade:", "Not yet complete")

    if count > 0:

        overall_percentage = total / count

        print("\n==============================")
        print("      OVERALL ALL SUBJECTS")
        print("==============================")

        print("Overall Percentage:", round(overall_percentage, 2), "%")

def student_deans_status(student_id):

    print("\n==============================")
    print("     DEAN'S LIST STATUS")
    print("==============================")

    status, average = (is_deans_list(student_id))

    print("Student:", students[student_id]["name"])
    print("Student ID:", student_id)
    print("\nDean's List Average Grade:", format(average, ".2f"))

    if status:
        print("Status: QUALIFIED")

    else:
        print("Status: NOT QUALIFIED")

def student_menu(student_id):

    while True:

        print("\n==============================")
        print("         STUDENT MENU")
        print("==============================")

        print("Welcome,", students[student_id]["name"])

        print("==============================")

        print("1. View my grades")
        print("2. Check Dean's List status")
        print("3. Logout")

        choice = input("\nChoose an option: ")

        if choice == "1":
            student_view_grades(student_id)

        elif choice == "2":
            student_deans_status(student_id)

        elif choice == "3":
            print("\nLogging out...")
            break

        else:
            print("\nInvalid choice. Please choose 1-3.")

def deans_list():

    print("\n==============================")
    print("      DEAN'S LIST QUALIFIERS")
    print("==============================")

    if len(students) == 0:

        print("There are no students.")
        return

    qualified = False

    for student_id, student in students.items():

        status, average = is_deans_list(student_id)

        if status:
            qualified = True
            print(student["name"], "-", student_id, "- Average Grade:", format(average, ".2f"))

    if not qualified:
        print("No students currently qualify for the Dean's List.")

    print("\nPE and NST are excluded from the Dean's List calculation.")

def teacher_menu():

    while True:

        print("\n==============================")
        print("        TEACHER MENU")
        print("==============================")

        print("1. Add student")
        print("2. Remove student")
        print("3. List of students")
        print("4. Add subject")
        print("5. Remove subject")
        print("6. List of subjects")
        print("7. Input student grades")
        print("8. View a student's grades")
        print("9. Dean's List qualifiers")
        print("10. Exit to login")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            remove_student()

        elif choice == "3":
            list_students()

        elif choice == "4":
            add_subject()

        elif choice == "5":
            remove_subject()

        elif choice == "6":
            list_subjects()

        elif choice == "7":
            input_student_scores()

        elif choice == "8":
            view_student_grades()

        elif choice == "9":
            deans_list()

        elif choice == "10":
            print("\nReturning to login...")
            break

        else:
            print("\nInvalid choice. Please choose 1-10.")

def teacher_login():

    print("\n==============================")
    print("        TEACHER LOGIN")
    print("==============================")

    username = input("Teacher username: ")
    password = input("Teacher password: ")

    if (username == TEACHER_USERNAME
        and password == TEACHER_PASSWORD):

        print("\nTeacher Login successful.")
        teacher_menu()

    else:
        print("\nInvalid username or password.")

def student_login():

    print("\n==============================")
    print("        STUDENT LOGIN")
    print("==============================")

    student_id = input("Enter your Student ID: ").strip()

    if student_id not in students:
        print("\nStudent ID not found.")
        return

    print("\nStudent Login successful.")
    print("Welcome,", students[student_id]["name"])
    student_menu(student_id)

while True:

    print("\n==============================")
    print("  GRADE MONITORING SYSTEM")
    print("==============================")

    print("\n1. Teacher")
    print("2. Student")
    print("3. Exit")

    choice = input("\nLogin as: ")

    if choice == "1":
        teacher_login()

    elif choice == "2":
        student_login()

    elif choice == "3":
        print("\nThank you for using the Grade Monitoring System!")
        break

    else:
        print("\nInvalid choice. Please choose 1, 2, or 3.")