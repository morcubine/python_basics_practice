import csv

# Students.csv 
# Name,Age,Marks
# Alice,18,92
# Bob,19,75
# Charlie,18,88
# David,20,56
# Eva,19,99
# Frank,18,43
# Grace,20,81
# Henry,19,67

# Q1: Print only the students whose marks are greater than 80.

# fieldnames = ['Name', 'Age', 'Marks']
# with open('students.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows([{'Name': 'Alice', 'Age': 18, 'Marks': 92}, {'Name': 'Bob', 'Age': 19, 'Marks': 75}, {'Name': 'Charlie', 'Age': 18, 'Marks': 88}, {'Name': 'David', 'Age': 20, 'Marks': 56}, {'Name': 'Eva', 'Age': 19, 'Marks': 99}, {'Name': 'Frank', 'Age': 18, 'Marks': 43}, {'Name': 'Grace', 'Age': 20, 'Marks': 81}, {'Name': 'Henry', 'Age': 19, 'Marks': 67}])

# with open('students.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if int(row['Marks']) > 80:
#             print(row)

# Q2: Find the highest marks.

# with open('students.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)
#     highest_marks = 0
#     top_students = ''
#     for row in reader:
#         marks = int(row['Marks'])
#         if  marks > highest_marks:
#             highest_marks = marks
#             top_students = row['Name']
#     print(f'Students: {top_students}, Score: {highest_marks}')

# Q3: Count how many students scored above the average.

# with open('students.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)

#     student_marks = []
#     above_avg = 0

#     for row in reader:
#         marks = int(row['Marks'])
#         student_marks.append(marks)
        
        
#     avg = sum(student_marks) // len(student_marks)
#     # print(avg)

#     for marks in student_marks: 
#         if marks > avg:
#             above_avg += 1

#     print(above_avg)



# Q4: Print students whose names have more than 5 letters.

# with open('students.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)

#     names = []

#     for row in reader:
#         name = row['Name']
#         if len(name) > 5:
#             names.append(name)

#     print(', '.join(names))



# Q5: Find the second-highest marks in students.csv.

# with open('students.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)

#     top_marks = []

#     for row in reader:
#         marks = int(row['Marks'])
#         top_marks.append(marks)

#     sorted_topmarks = sorted(top_marks)
#     # print(sorted_topmarks)

#     print(sorted_topmarks[-2])

# Q6: Create a new CSV file called passed_students.csv containing only students whose marks are at least 40.

# with open('students.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)

#     above_sixty = []

#     for row in reader:
#         marks  = int(row['Marks'])
#         if marks >= 60:
#             above_sixty.append(row)
        
#     print(above_sixty)

# fieldnames = ['Name', 'Age', 'Marks']
# with open('passed_students.csv', 'w', newline='') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(above_sixty)

# Dataset 2: employees.csv
# Name,Department,Salary
# John,HR,50000
# Emma,IT,72000
# Chris,Finance,65000
# Sophia,IT,82000
# Daniel,HR,45000
# Olivia,Marketing,55000
# James,Finance,90000
# Lily,IT,61000

# fieldnames = ['Name', 'Department', 'Salary']
# with open('employees.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames= fieldnames)
#     writer.writeheader()
#     writer.writerows([{'Name': 'John', 'Department': 'HR', 'Salary': 50000}, {'Name': 'Emma', 'Department': 'IT', 'Salary': 72000}, {'Name': 'Chris', 'Department': 'Finance', 'Salary': 65000}, {'Name': 'Sophia', 'Department': 'IT', 'Salary': 82000}, {'Name': 'Daniel', 'Department': 'HR', 'Salary': 45000}, {'Name': 'Olivia', 'Department': 'Marketing', 'Salary': 55000}, {'Name': 'James', 'Department': 'Finance', 'Salary': 90000}, {'Name': 'Lily', 'Department': 'IT', 'Salary': 61000}])

# Q7: Print employees whose names end with 'a'.

# with open('employees.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)

#     for row in reader:
#         if row['Name'].endswith('a'):
#             print(row['Name'])

# Q8: Print all employee names in alphabetical order.

# with open('employees.csv', 'r', newline='') as f:
#     reader = csv.DictReader(f)

#     names = []
    
#     for row in reader:
#         # print(rows)
#         names.append(row['Name'])     
#     # print(names)
#     sort_names = sorted(names)
#     print(sort_names)



    # rows = []
    # for row in reader:
        # rows.append(row)
    # sort_rows = sorted(rows, key=lambda row: row['Name'])
    # print(sort_rows)