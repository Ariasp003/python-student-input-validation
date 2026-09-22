Overview

A Python-based command-line Student Management System for creating, storing, searching, updating, deleting, sorting, and analyzing student records.

The project uses Python, Pandas, and CSV file storage to manage student information through a simple interactive menu.

Features

Create new student records

Validate student input

Store student data in a CSV file

Display all students

Search students by ID

Search students by full name

Update existing student records

Remove student records

Calculate student averages

Assign letter grades

Find the highest and lowest average

Sort students by different fields

Student Information

Student ID

First Name

Last Name

Age

Gender

Math Grade

Physics Grade

Chemistry Grade

Attendance

Average

Letter Grade

Grade System

Average

Letter Grade

90 - 100

A

80 - 89

B

70 - 79

C

60 - 69

D

0 - 59

F

Input Validation

First Name

Cannot be empty

Must contain only alphabetic characters

Must contain only one first name

Last Name

Cannot be empty

Must contain only alphabetic characters

Must contain only one last name

Student ID

Must be a positive number

Must contain exactly 8 digits

Duplicate student IDs are rejected

Age

Must be a valid number

Must be within the accepted range

Grades

Must be numeric

Must be between 0 and 100

Gender

Accepts M or F

Attendance

Must be between 0 and 100

Main Menu

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

Project Structure

Day1/
├── day_01_input_validation.py
├── students_scores.csv
├── pyproject.toml
├── 1.txt
├── README.md
└── .gitignore

Technologies Used

Technology

Purpose

Python

Application logic

Pandas

DataFrame operations and CSV management

Pathlib

File path handling

CSV

Persistent student data storage

Git / GitHub

Version control and project sharing

Python Concepts Practiced

Functions

Parameters and return values

Conditional statements

while loops

Input handling

String manipulation

Lists

Dictionaries

Type conversion

Exception handling

File handling

Pandas DataFrames

DataFrame filtering

DataFrame sorting

DataFrame updates

CSV reading and writing

Basic CRUD operations

Menu-driven programs

How It Works

User Input  →  Input Validation  →  Create Student Record  →  Store Data  →  Save to CSV  →  Search / Update / Delete / Sort / Analyze

Running the Project

1. Clone the repository

git clone <YOUR-REPOSITORY-URL>

2. Open the project

cd Day1

3. Install Pandas

pip install pandas

4. Run the program

python day_01_input_validation.py

Data Storage

Student records are stored in students_scores.csv. The CSV file is used as persistent storage, allowing student information to remain available after the program is closed.

Future Improvements

Better input re-prompting

Automated testing

More advanced statistics

Additional search options

More subjects

Student ranking

Data visualization

SQLite database integration

Web interface

REST API

Authentication and user accounts

Author

Aria Safaeipour

Project Status

Completed — Day 01 Python Project
