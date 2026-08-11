import csv


class Student:




    def __init__(self, roll, name, age, marks):
        self._roll = roll
        self._name = name
        self._age = age
        self._marks = marks



        if not isinstance(roll, int):
            raise TypeError(f'roll should be an integer, got {roll!r}')
        
        if not isinstance(name, str):
            raise TypeError(f'name should be a string, got {name!r}')

        if not isinstance(age, int):
            raise TypeError(f'age should be an integer, got {age!r}')

        if not isinstance(marks, int):
            raise TypeError(f'marks should be an integer, got {marks!r}')



        if age < 0:
            raise ValueError(f'age cannot be a negative value, got {age!r}')

        if marks < 0:
            raise ValueError(f'marks cannot be below 0, got {marks!r}')
        elif marks > 100:
            raise ValueError(f'marks cannot be over 100, got {marks!r}')
            


    def get_roll(self):
        return self._roll

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_marks(self):
        return self._marks


    def __str__(self):
        return f'Roll: {self._roll}, Name: {self._name}, Age: {self._age}, Marks: {self._marks}' 



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


    def is_pass(self):

        if self._marks >= 40:
            return True
        return False



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



def find_student(student_list, roll_number):

    for s in student_list:
        # print(s)
        if roll_number == s.get_roll():
            return s.get_name()
    else:
        raise ValueError(f'{roll_number} does not exist')

def highest_marks(students_list):

    highest = 0

    for s in students_list:
        if s.get_marks() > highest:
            highest = s.get_marks()

    return highest
        



def main():
    print('Welcome to the Python Little Project\n')

    try:
        student_list = load_students('students.csv')
        print(f'Loaded {len(student_list)} students\n')
    except FileNotFoundError:
        student_list = []
        print(f'Could not find {student_list}. Starting with an empty list.')


    menu = ('0. Load csv file\n1. Get roll number\n2. Get name\n3. Get age\n4. Get marks\n5. Update marks\n6. Update age\n7. print object\n8. Check pass/fail\n9. Get grade\10. Find student\n11. Find top student\nQ means quit')

    menu_labels = {'0': 'Load CSV file', '1': 'Get roll number', '2': 'Get name', '3': 'Get age', '4': 'Get marks', '5': 'Update marks', '6': 'Update age', '7': 'Print objedct', '8': 'Check pass/fail', '9': 'Get grade', '10': 'Find student', '11': 'Find top student'}
     

    while True:
        print(f'Please choose one of the following:\n{menu}')
        entry = input('> ').strip()
        if entry.lower() in menu_labels:
            print(f'→ {menu_labels[entry]}')
        print()

        if not student_list and entry not in ('0', 'q', 'Q'):
            print('No students loaded - choose 0 to load the CSV first\n')
            continue

        if entry == '0':
            student_list = load_students('students.csv')

        elif entry == '1':
            print('Roll numbers:')
            for s in student_list:
                print(s.get_roll())


        elif entry == '2':
            print('Student names:')
            for s in student_list:
                print(s.get_name())


        elif entry == '3':
            print('Student age:')
            for s in student_list:
                print(s.get_age())


        elif entry == '4':
            print('Student marks:')
            for s in student_list:
                print(s.get_marks())


        elif entry == '5':
            name = input('Enter student name: ')
            marks = int(input('Enter new mark: '))
            for s in student_list:
                if name == s.get_name():
                    s.update_marks(marks)
                    break
    
        elif entry == '6':
            name = input('Enter student name: ')
            age = int(input('Enter new age: '))
            for s in student_list:
                if name == s.get_name():
                    s.update_age(age)
                    break

        elif entry == '7':
            roll_number = int(input('Enter roll number: '))
            for s in student_list:
                if roll_number == s.get_roll():
                    print(s)
                    break

        elif entry == '8':
            roll_number = int(input('Enter roll number: '))
            for s in student_list:
                if roll_number == s.get_roll():
                    print(s.is_pass())
                    break

        elif entry == '9':
            name = input('Enter name of student: ')
            for s in student_list:
                if name == s.get_name():
                    print(s.get_grade())
                    break

        elif entry == '10':
            roll_number = int(input('Enter roll number: '))
            print(find_student(student_list, roll_number))
            

        elif entry == '11':
            print(highest_marks(student_list))

        elif entry.lower() == 'q':
            print('Thank you. Bye.')
            print()
            break

        print()


main()


