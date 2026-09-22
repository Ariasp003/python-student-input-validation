# Student Management System

A command-line Student Management System built with Python and Pandas.

This project allows users to create, view, search, update, remove, sort, and analyze student records. Student information is stored in a CSV file so that records can be maintained between program runs.

## Features

- Create new student records
- Validate student input
- Store student records in a CSV file
- Display all students
- Search students by ID
- Search students by full name
- Update existing student records
- Remove student records
- Calculate student averages
- Assign letter grades
- Find the student with the highest average
- Find the student with the lowest average
- Sort students by different fields

## Student Information

The application manages the following information:

- Student ID
- First Name
- Last Name
- Age
- Gender
- Math Grade
- Physics Grade
- Chemistry Grade
- Attendance

The application can also calculate and store:

- Average Grade
- Letter Grade

## Grade System

| Average | Letter Grade |
|---------|--------------|
| 90-100  | A            |
| 80-89   | B            |
| 70-79   | C            |
| 60-69   | D            |
| 0-59    | F            |

## Input Validation

The application validates user input before saving student information.

### First Name

- Cannot be empty
- Must contain alphabetic characters
- Must contain only the first name

### Last Name

- Cannot be empty
- Must contain alphabetic characters
- Must contain only the last name

### Student ID

- Must be a positive number
- Must contain exactly 8 digits
- Duplicate student IDs are rejected

### Age

- Must be a valid integer
- Must be within the accepted range

### Grades

- Must be numeric
- Must be between 0 and 100

### Gender

- Accepts M or F

### Attendance

- Must be between 0 and 100

## Main Menu

1. Create student
2. Show all students
3. Find student by ID
4. Find student by Full name
5. Remove student
6. Update student
7. Calculate student averages
8. Show best student
9. Show worst student
10. Sort students
0. Exit

## Project Structure

Day1/
├── day_01_input_validation.py

├── students_scores.csv

├── pyproject.toml

├── LICENSE

├── README.md

└── .gitignore

## Technologies Used

- Python
- Pandas
- Pathlib
- CSV
- Git
- GitHub

## Python Concepts Practiced

- Functions
- Parameters and return values
- Conditional statements
- Loops
- User input
- Input validation
- String manipulation
- Lists
- Dictionaries
- Type conversion
- Exception handling
- File handling
- Pandas DataFrames
- DataFrame filtering
- DataFrame sorting
- DataFrame updates
- CSV reading and writing
- CRUD operations
- Menu-driven application design

## Application Flow

User Input
    ↓
Input Validation
    ↓
Student Dictionary
    ↓
Pandas DataFrame
    ↓
CSV Storage
    ↓
Search / Update / Delete / Sort / Analysis

## Data Storage

Student records are stored in:

students_scores.csv

The application reads existing records from the CSV file and writes new or updated records back to the same file.

## Running the Project

### Clone the Repository

git clone <YOUR-REPOSITORY-URL>
cd Day1

### Install Dependencies

pip install pandas

### Run the Application

python day_01_input_validation.py

## Future Improvements

- Improve input re-prompting
- Add automated tests
- Add more student statistics
- Add additional search options
- Add student ranking
- Add data visualization
- Replace CSV storage with SQLite or PostgreSQL
- Build a graphical user interface
- Build a web-based version
- Add a REST API
- Add authentication and user accounts

## Author

Aria Safaeipour

## Project Status

Completed - Day 01 Python Project
