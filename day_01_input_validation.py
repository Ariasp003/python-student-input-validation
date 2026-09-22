import pandas as pd
from pathlib import Path

CSV_FILE = Path("students_scores.csv")

def get_fname():
    """Task1"""
    fname = input("Please enter student first name: ").strip().title()

    if not fname:
        print("Name can't be empty.")
        return None
    parts = fname.split()
    if len(parts) > 1:
        print("Please enter only the first name.")
        return None
    if not fname.isalpha():
        print("The name contains non-alphabetic characters.")
        return None
    return fname

def get_lname():
    """Task2"""
    lname = input("Please enter student last name: ").strip().title()

    if not lname:
        print("Name can't be empty.")
        return

    parts = lname.split()

    if len(parts) > 1:
        print("Please enter only the last name.")
        return

    if not lname.isalpha():
        print("The name contains non-alphabetic characters.")
        return

    return lname

def get_student_id():
    """Task3"""
    try:
        std_id = int(input("please enter your student ID :").strip())
        if std_id <= 0:
            print("Student ID must be a positive eight-digit number.")
            return
        elif len(str(std_id)) != 8 :
            print("Student ID should be a valid number with length of 8.")
            return
        else:
            return std_id
    except ValueError:
        print("Invalid Input, try again")
        return
def get_age():
    """Task4"""
    try:
        age = int(input("please enter your student age :").strip())
    except ValueError:
        print("Invalid Input, try again")
        return
    if age not in range(5,101):
        print("Age not in acceptable range.")
        return
    return age

def get_grade(subject):
    try:
        grade = float(
            input(f"Please enter the student's {subject} grade: ").strip()
        )
    except ValueError:
        print(f"{subject} grade must be a number.")
        return

    if grade < 0 or grade > 100:
        print(f"{subject} grade must be between 0 and 100.")
        return

    return grade


def get_letter_grade(grade):
    """Extra 5"""
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"
    
def get_gender():
    """Task 6"""

    gender = input(
        "Enter student gender (M/F): "
    ).strip().upper()

    if gender not in ("M", "F"):
        print("Please enter M or F.")
        return

    return gender   
    
def create_student():
    """Task 7"""
    fname = get_fname()
    if fname is None:
        return
    lname = get_lname()
    if lname is None:
        return
    std_id = get_student_id()
    if std_id is None:
        return
    age = get_age()
    if age is None:
        return
    gender = get_gender()
    if gender is None:
        return
   
    math_grade = get_grade("Math")
    if math_grade is None:
        return

    physics_grade = get_grade("Physics")
    if physics_grade is None:
        return

    chemistry_grade = get_grade("Chemistry")
    if chemistry_grade is None:
        return
    try:
        attendance = float(input("please enter your student attendance :").strip())
        print("\n\n")
        if attendance < 0 or attendance > 100:
            print("attendance must be between 0 and 100.")
            return
    except ValueError:
        print("Invalid Input, try again")
        return
    
    student_dict = {
        "student_ID" : std_id,
        "first_name" : fname,
        "last_name" : lname,
        "age" : age,
        "gender" : gender,
        "math_grade" : math_grade,
        "physics_grade" : physics_grade,
        "chemistry_grade" : chemistry_grade,
        "attendance" : attendance
    }
    return student_dict

def printer():
    student_dict = create_student()
    if student_dict is None:
        print("Student was not created because one input was invalid.")
        return

    grade = (student_dict["math_grade"] + student_dict["physics_grade"] + student_dict["chemistry_grade"]) / 3
    letter_grade = get_letter_grade(grade)
    if not save_student(student_dict):
        return
    print(
    f"\n\n\nYour name is {student_dict["first_name"]} {student_dict["last_name"]}, "
    f"Gender: {'Male' if student_dict['gender'] == 'M' else 'Female'}. "
    f"You are {student_dict["age"]} years old. "
    f"Student ID: {student_dict["student_ID"]}.\n"
    f"Grades: Math : {student_dict["math_grade"]} , physics : {student_dict["physics_grade"]} , "
    f"chemistry : {student_dict["chemistry_grade"]} , attendance : {"Pass" if student_dict["attendance"] >= 60 else "Fail" }. "
    f"Letter grade: {letter_grade}. \n"
    f"Your grade : {grade}. \n"
    f"Nice to meet you!\n\n"
    )

def save_student(student_dict):
    """Save one student to the CSV file."""

    new_row = pd.DataFrame([student_dict])

    if CSV_FILE.exists():
        current_df = pd.read_csv(CSV_FILE)

        if student_dict["student_ID"] in current_df["student_ID"].values:
            print("A student with this ID already exists.")
            return False

        updated_df = pd.concat(
            [current_df, new_row],
            ignore_index=True
        )
    else:
        updated_df = new_row

    updated_df.to_csv(CSV_FILE, index=False)

    print("Student saved successfully.")
    return True

def load_students():
    """Load student records from the CSV file."""

    if not CSV_FILE.exists():
        print("Student file does not exist. An empty table was created.")
        return pd.DataFrame()

    try:
        students_df = pd.read_csv(CSV_FILE)

        if students_df.empty:
            print("The student file exists, but it contains no students.")

        return students_df

    except pd.errors.EmptyDataError:
        print("The student file is completely empty.")
        return pd.DataFrame()

    except pd.errors.ParserError:
        print("The student file is damaged or has an invalid CSV format.")
        return pd.DataFrame()

    except PermissionError:
        print("The student file cannot be opened. It may be open in another program.")
        return pd.DataFrame()

    except Exception as error:
        print(f"An unexpected error occurred while loading the file: {error}")
        return pd.DataFrame()

def show_students():
    """Display all students stored in the CSV file."""

    students_df = load_students()

    if students_df.empty:
        print("No students found.")
        return

    print("\nAll Students:")
    print(students_df.to_string(index=False))

def find_student_by_id():
    students_df = load_students()

    if students_df.empty:
        print("No students found.")
        return
    
    std_id = get_student_id()
    if std_id is None:
        print("Student does not exist.")
        return
    student = students_df[students_df["student_ID"] == std_id]
    if student.empty:
        print("Student not found.")
        return

    print("\nStudent found:")
    print(student.to_string(index=False))


def find_student_by_name():
    students_df = load_students()

    if students_df.empty:
        print("No students found.")
        return
    fname = get_fname()
    if fname is None:
        return

    lname = get_lname()
    if lname is None:
        return
    student = students_df[
        (students_df["first_name"] == fname)
        & (students_df["last_name"] == lname)
    ]
    if student.empty:
        print("Student does not exist.")
        return
    else:
        print("Student Found :")
        print(student.to_string(index=False))

def remove_student():
    std_id = get_student_id()

    if std_id is None:
        return

    students_df = load_students()

    if students_df.empty:
        print("No students found.")
        return

    student = students_df[
        students_df["student_ID"] == std_id
    ]

    if student.empty:
        print("Student not found.")
        return

    print("\nThe student you want to remove:")
    print(student.to_string(index=False))

    first_name = student.iloc[0]["first_name"]
    last_name = student.iloc[0]["last_name"]

    answer = input(
        "Please confirm your choice (Y/N): "
    ).strip().upper()

    if answer != "Y":
        print("Removal cancelled.")
        return

    updated_df = students_df[
        students_df["student_ID"] != std_id
    ].reset_index(drop=True)

    updated_df.to_csv(CSV_FILE, index=False)

    print(
        f"{first_name} {last_name} "
        f"was successfully removed."
    )

def update_student():
    std_id = get_student_id()

    if std_id is None:
        return

    students_df = load_students()

    if students_df.empty:
        print("No students found.")
        return

    student = students_df[
        students_df["student_ID"] == std_id
    ]
    if student.empty:
        print("Student not found.")
        return
    print("The student found:\n"
          f"{student.to_string(index=False)}"
          )
    while True:
        print("Update menu:\n"
            "1. First name\n"
            "2. Last name\n"
            "3. Age\n"
            "4. Gender\n"
            "5. Math grade\n"
            "6. Physics grade\n"
            "7. Chemistry grade\n"
            "8. Attendance\n"
            "0. Cancel\n"
        )
        option = input("Please enter your choice :").strip()
        if option == "1":
            student_fname = students_df.loc[
                students_df["student_ID"] == std_id,
                    "first_name"].iloc[0]
            print(f"Current name : {student_fname}")
            new_fname = get_fname()
            if new_fname is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"first_name"] = new_fname
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"First name updated from "
            f"{student_fname} to {new_fname}."
        )
        elif option == "2":
            student_lname = students_df.loc[
                students_df["student_ID"] == std_id,
                    "last_name"].iloc[0]
            print(f"Current name : {student_lname}")
            new_lname = get_lname()
            if new_lname is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"last_name"] = new_lname
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Last name updated from "
            f"{student_lname} to {new_lname}."
        )
        elif option == "3":
            student_age = students_df.loc[
                students_df["student_ID"] == std_id,
                "age"].iloc[0]
            print(f"Current Age : {student_age}")
            new_age = get_age()
            if new_age is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"age"] = new_age
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Age updated from "
            f"{student_age} to {new_age}."
        )
        elif option == "4":
            student_gender = students_df.loc[
                students_df["student_ID"] == std_id,
                "gender"].iloc[0]
            print(f"Current Gender : {student_gender}")
            new_gender = get_gender()
            if new_gender is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"gender"] = new_gender
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Gender updated from "
            f"{student_gender} to {new_gender}."
        )
        elif option == "5":
            student_math_grade = students_df.loc[
                students_df["student_ID"] == std_id,
                "math_grade"].iloc[0]
            print(f"Current math grade : {student_math_grade}")
            new_math_grade = get_grade("math")
            if new_math_grade is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"math_grade"] = new_math_grade
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Math grade updated from "
            f"{student_math_grade} to {new_math_grade}."
        )
        elif option == "6":
            student_physics_grade = students_df.loc[
                students_df["student_ID"] == std_id,
                "physics_grade"].iloc[0]
            print(f"Current physics grade : {student_physics_grade}")
            new_physics_grade = get_grade("physics")
            if new_physics_grade is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"physics_grade"] = new_physics_grade
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Physics grade updated from "
            f"{student_physics_grade} to {new_physics_grade}."
        )
        elif option == "7":
            student_chemistry_grade = students_df.loc[
                students_df["student_ID"] == std_id,
                "chemistry_grade"].iloc[0]
            print(f"Current Chemistry grade : {student_chemistry_grade}")
            new_chemistry_grade = get_grade("chemistry")
            if new_chemistry_grade is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"chemistry_grade"] = new_chemistry_grade
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Chemistry grade updated from "
            f"{student_chemistry_grade} to {new_chemistry_grade}."
        )
        elif option == "8":
            student_attendance = students_df.loc[
                students_df["student_ID"] == std_id,
                "attendance"].iloc[0]
            print(f"Current attendance : {student_attendance}")
            new_attendance = get_grade("attendance")
            if new_attendance is None:
                return
            students_df.loc[students_df["student_ID"] == std_id,"attendance"] = new_attendance
            students_df.to_csv(CSV_FILE, index=False)
            print(
            f"Attendance updated from "
            f"{student_attendance} to {new_attendance}."
        )
        elif option == "0":
            print("back to main menu .")
            return
        else:
            print("Invalid option.")

def add_average_column():
    students_df = load_students()

    if students_df.empty:
        print("No students found.")
        return

    students_df["average"] = (
        students_df["math_grade"]
        + students_df["physics_grade"]
        + students_df["chemistry_grade"]
    ) / 3

    students_df["average"] = students_df["average"].round(2)

    students_df["letter_grade"] = students_df["average"].apply(
        get_letter_grade
    )

    students_df.to_csv(CSV_FILE, index=False)

    print("Average and letter grade columns added successfully.")



def show_best_student():
    students_df = load_students()
    if students_df.empty:
        print("No students found.")
        return
    
    if "average" not in students_df.columns:
        print("Average column does not exist. Calculate averages first.")
        return
    
    highest_average = students_df["average"].max()
    
    best_student = students_df[
        students_df["average"] == highest_average
    ]
    print("Best Student is:\n"
    f"{best_student.to_string(index=False)}"
    )

def show_worst_student():
    students_df = load_students()
    if students_df.empty:
        print("No students found.")
        return
    if "average" not in students_df.columns:
        print("Average column does not exist. Calculate averages first.")
        return
        
    lowest_average = students_df["average"].min()
    
    worst_student = students_df[
        students_df["average"] == lowest_average
    ]
    print("Worst student is:\n"
    f"{worst_student.to_string(index=False)}"
    )

def sort_students():
    students_df = load_students()
    if students_df.empty:
        print("No students found.")
        return
    while True:
        option = input("\n\nBased on which title you want to sort:\n"
                    "1. Sort by first name\n"
                    "2. Sort by age\n"
                    "3. Sort by average grade, highest first\n"
                    "4. Sort by average grade, lowest first\n"
                    "5. Sort by attendance, highest first\n"
                    "6. Sort by attendance, lowest first\n"
                    "0. Exit\n\n"
                    "Your choice: "
                    ).strip()
        if option == "1":
            new_df = students_df.sort_values(by=["first_name"],)
            print(new_df.to_string(index=False))
        elif option == "2":
            new_df = students_df.sort_values(by=["age"])
            print(new_df.to_string(index=False))
        elif option == "3":
            if "average" not in students_df.columns:
                print("Average column does not exist.")
                continue
            new_df = students_df.sort_values(
                by="average",
                ascending=False
            )
            print(new_df.to_string(index=False))
        elif option == "4":
                    if "average" not in students_df.columns:
                        print("Average column does not exist.")
                        continue
                    new_df = students_df.sort_values(
                        by="average",
                        ascending=True
                    )
                    print(new_df.to_string(index=False))
        elif option == "5":
            new_df = students_df.sort_values(by=["attendance"],ascending=False)
            print(new_df.to_string(index=False))
        elif option == "6":
                    new_df = students_df.sort_values(by=["attendance"],ascending=True)
                    print(new_df.to_string(index=False))
        elif option == "0":
            print("Back to main menu")
            return
        else:
            print("invalid option")


def main():
    while True:
        option = input(
            "\nPlease choose from the menu below:\n"
            "1. Create student\n"
            "2. Show all students\n"
            "3. Find student by ID\n"
            "4. Find student by Full name\n"
            "5. Remove student\n"
            "6. Update student\n"
            "7. Calculate student averages\n"
            "8. Show best student\n"
            "9. Show worst student\n"
            "10. Sort students\n"
            "0. Exit\n"
            "Your choice: "
        ).strip()

        if option == "1":
            printer()
        elif option == "2":
            show_students()
        elif option == "3":
            find_student_by_id()
        elif option == "4":
            find_student_by_name()
        elif option == "5":
            remove_student()
        elif option == "6":
            update_student()
        elif option == "7":
            add_average_column()
        elif option == "8":
            show_best_student()
        elif option == "9":
            show_worst_student()
        elif option == "10":
            sort_students()
        elif option == "0":
            print("Bye")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()