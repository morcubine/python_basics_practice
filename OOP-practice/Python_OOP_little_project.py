import csv

# Project: Student Record Manager
# Step 0: Think Before Coding

# Before opening your editor, answer these questions:

# What is a Student?
# What information should a Student store?
# What should a Student be able to do?

# You'll realize:

# Data (Attributes)
# Roll Number
# Name
# Age
# Marks
# Behaviors (Methods)
# Get details
# Update age
# Update marks
# Check pass/fail
# Calculate grade

# Function(s) to create:
# ❌ None (Planning step)




# Step 1: Create the Class

# Create a class named Student.

# Don't write any methods yet.

# Just create the empty class.

# Function(s) to create:

# class Student

class Student:


# Step 2: Write the Constructor

# Now think:

# Whenever someone creates a Student object, what information is required?

# The constructor should receive:

# roll
# name
# age
# marks

# Store them as private attributes.

# Function(s) to create:

# __init__(self, roll, name, age, marks)


    def __init__(self, roll, name, age, marks):
        self._roll = roll
        self._name = name
        self._age = age
        self._marks = marks


# Step 3: Validate Constructor Inputs

# Before storing anything:

# Ask yourself:

# Is roll an integer?
# Is name a string?
# Is age an integer?
# Is marks an integer?

# If not:

# Raise appropriate errors.


        if not isinstance(roll, int):
            raise TypeError(f'roll should be an integer, got {roll!r}')
        
        if not isinstance(name, str):
            raise TypeError(f'name should be a string, got {name!r}')

        if not isinstance(age, int):
            raise TypeError(f'age should be an integer, got {age!r}')

        if not isinstance(marks, int):
            raise TypeError(f'marks should be an integer, got {marks!r}')


# Then check values:

# Can age be negative?
# Can marks be below 0?
# Can marks be above 100?

# Raise errors where necessary.

        if age < 0:
            raise ValueError(f'age cannot be a negative value, got {age!r}')

        if marks < 0:
            raise ValueError(f'marks cannot be below 0, got {marks!r}')
        elif marks > 100:
            raise ValueError(f'marks cannot be over 100, got {marks!r}')
            

# Only after every validation passes should you store the attributes.

# Function(s) to modify:

# __init__()

# (No new function—add validation inside the constructor.)
        



# Step 4: Create Getter Methods

# Never access attributes directly.

# Create methods to return:

# roll
# name
# age
# marks

# Test them before moving ahead.

# Function(s) to create:

# get_roll()
# get_name()
# get_age()
# get_marks()

    def get_roll(self):
        return self._roll

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_marks(self):
        return self._marks


# Step 5: Print a Student

# If someone writes

# print(student)

# What should they see?

# Implement a readable string representation.

# Don't worry about formatting too much.

# Just make it informative.

# Function(s) to create:

# __str__()

    def __str__(self):
        return f'Roll: {self._roll}, Name: {self._name}, Age: {self._age}, Marks: {self._marks}' 


# Step 6: Update Methods

# Suppose a student's marks change.

# Should someone write

# student._marks = 90

# No.

# Instead create:

# update_marks()
# update_age()

# These methods should:

# validate input
# update attribute

# Nothing else.

# Function(s) to create:

# update_marks(new_marks)
# update_age(new_age)


    def update_marks(self, new_marks):

        if not isinstance(new_marks, int):
            raise TypeError(f'marks should be an integer, got {new_marks!r}')

        if new_marks < 0:
            raise ValueError(f'marks cannot be below 0, got {new_marks!r}')
        elif new_marks > 100:
            raise ValueError(f'marks cannot be over 100, got {new_marks!r}')
        
        self._marks = new_marks


    def update_age(self, new_age):

        if not isinstance(new_age, int):
            raise TypeError(f'age should be an integer, got {new_age!r}')

        if new_age < 0:
            raise ValueError(f'age cannot be a negative value, got {new_age!r}')

        self._age = new_age


# Step 7: Add a Pass/Fail Method

# Ask:

# Can this student pass?

# Return:

# True
# False

# Don't print anything.

# Just return.

# Function(s) to create:

# is_pass()

    def is_pass(self):

        if self._marks >= 40:
            return True
        return False


# Step 8: Add Grade Calculation

# Create another method.

# It should decide the student's grade based on marks.

# Return the grade.

# Don't print it.

# Function(s) to create:

# get_grade()


    def get_grade(self):

        if self._marks >= 90:
            return 'A'
        elif self._marks >= 75:
            return 'B'
        elif self._marks >= 60:
            return 'C'
        elif self._marks >= 40:
            return 'D'
        else:
            return 'F'


# Step 9: Create the CSV File

# Now create a file.

# Think about:

# What should the first row contain?

# (Header)

# Then add around 5–10 students.

# Function(s) to create:
# ❌ None

# Create:

# students.csv

# roll,name,age,marks
# 1,Alice,20,85
# 2,Bob,22,45
# 3,Charlie,19,92
# 4,Diana,21,38
# 5,Ethan,23,67
# 6,Fiona,20,74
# 7,George,24,55
# 8,Hannah,22,99
# 9,Ian,19,30
# 10,Julia,21,80

# students = [{'Roll': 1, 'Name': 'Alice', 'Age': 20, 'Marks': 85}, {'Roll': 2, 'Name': 'Bob', 'Age': 22, 'Marks': 45}, {'Roll': 3, 'Name': 'Charlie', 'Age': 19, 'Marks': 92}, {'Roll': 4, 'Name': 'Diana', 'Age': 21, 'Marks': 38}, {'Roll': 5, 'Name': 'Ethan', 'Age': 23, 'Marks': 67}, {'Roll': 6, 'Name': 'Fiona', 'Age': 20, 'Marks': 74}, {'Roll': 7, 'Name': 'George', 'Age': 24, 'Marks': 55}, {'Roll': 8, 'Name': 'Hannah', 'Age': 22, 'Marks': 99}, {'Roll': 9, 'Name': 'Ian', 'Age': 19, 'Marks': 30}, {'Roll': 10, 'Name': 'Julia', 'Age': 21, 'Marks': 80}]

# fieldnames = ['Roll', 'Name', 'Age', 'Marks']
# with open('students.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(students)



# Step 10: Read the File



# Create a separate function.

# Its job:

# open file
# skip header
# read each line
# split values
# convert numeric values
# create Student objects
# store them in a list

# Return the list.

# Function(s) to create:

# load_students(filename)


def load_students(filename):

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        student_list = []

        for row in reader:
            roll = int(row['Roll'])
            name = row['Name']
            age = int(row['Age'])
            marks = int(row['Marks'])
            student = Student(roll, name, age, marks)

            student_list.append(student)

    return student_list




# s1 = Student(1, 'Alice', 22, 67)

# print(s1.get_roll())
# print(s1.get_name())
# print(s1.get_age())
# print(s1.get_marks())

students = load_students('students.csv')

for s in students:
    print(s)


#   Claude check:

# print(students[0].is_pass())
# print(students[0].get_grade())
# students[0].update_marks(95)
# print(students[0])




