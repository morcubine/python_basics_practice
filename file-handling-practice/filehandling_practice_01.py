# PYTHON FILE HANDLING - HOMEWORK QUESTIONS

# LEVEL 1: BASIC FILE OPERATIONS

# 1. Create a file named notes.txt and write:
# Python is easy.
# I am learning file handling.
# Practice makes programming better.

"""with open('notes.txt', 'w') as f:
    f.writelines('Python is easy.\nI am learning file handling.\nPractice makes programming better.\n')"""

# Then read and print the complete file.

"""with open('notes.txt', 'r') as f:
    content = f.read()
    print(content)"""

# 2. Create a file named languages.txt and write:
# Python
# Java
# C++
# JavaScript

"""with open('languages.txt', 'w') as f:
    lines = ['Python\n', 'Java\n', 'C++\n', 'JavaScript\n']
    f.writelines(lines)"""

# Read the file one line at a time using readline().

"""with open('languages.txt', 'r') as f:
    content = f.readlines()
    print(content)"""

# 3. Read languages.txt using readlines() and print each language without extra blank lines.

"""with open('languages.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        print(line)"""

"""with open('languages.txt', 'r') as f:
    content = f.readlines()
    for lines in content:
        line = lines.strip()    
        print(line)"""

# 4. Create a file named numbers.txt and write numbers from 1 to 10, with each number on a new line.

"""with open('numbers.txt', 'w') as f:
    numbers = ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n', '7\n', '8\n', '9\n', '10\n']
    f.writelines(numbers)"""

# 5. Read numbers.txt and calculate the sum of all numbers.

"""with open('numbers.txt', 'r') as f:
    content = f.read()
    total = 0
    lines = content.splitlines()
    for line in lines:
        total += int(line)
    print(total)"""

# LEVEL 2: WRITING AND APPENDING

# 6. Create a file named students.txt and write:
# Rahul
# Anjali
# Sameer
# Riya

"""with open('students.txt', 'w') as f:
    students = ['Rahul\n', 'Anjali\n', 'Sameer\n', 'Riya\n']
    f.writelines(students)"""

# Then append two more names without deleting the existing names.

"""with open('students.txt', 'a') as f:
    add_students = ['Aniket\n', 'Neha\n']
    f.writelines(add_students)"""

# 7. Write three lines to a file using writelines().

"""with open('notes.txt', 'a') as f:
    add_lines = ['Errors help you learn faster\n'
'Debugging is a skill worth learning\n'
'Consistency beats intensity\n']
    f.writelines(add_lines)"""

# LEVEL 3: COUNTING AND SEARCHING

# 8. Create a file named paragraph.txt. Read it and count:
# - Total characters

"""with open('paragraph.txt', 'w') as f:
    f.write('Python is a versatile programming language used in web development, data science, automation, and more. It has a simple and readable syntax, which makes it a great choice for beginners. Learning file handling, loops, and functions will help you build a strong foundation for more advanced projects.')"""

"""with open('paragraph.txt', 'r') as f:
    content = f.read()
    # print(f'{content!r}')
    raw = content.replace(' ', '')
    print(len(raw))"""


# 9. Count how many times the word "Python" occurs in a file. Make the search case-insensitive.

"""with open('python_count.txt', 'w') as f:
    f.write("Python is a popular programming language. python is known for its readability. Many beginners choose PYTHON as their first language. Once you learn python, you can build web apps, automate tasks, and analyze data. Python's simplicity is one of the reasons for its popularity.")"""

"""with open('python_count.txt', 'r') as f:             # Do THIS ONE AGAIN
    content = f.read()
    words = content.lower().split()
    total = 0
    punctuation = ".,'\""
    for word in words:
        cleaned = word
        for p in punctuation:
            cleaned = cleaned.replace(p, '')
        if cleaned == 'python' or cleaned.startswith('python'):
            total += 1
    print(total)"""


# 10. Ask the user for a word. Check whether that word exists in paragraph.txt.

"""with open('paragraph.txt', 'r') as f:
    content = f.read()
    words = content.lower().split()

    entry = input('Enter word: ').lower()

    for word in words:
        if entry == word:
            print('Word found.')
            break
    else:
        print('Word not found')"""
    

# 11. Read a file and print only the lines containing the word "Python".

"""with open('lines_w_python.txt', 'w') as f:
    lines = ["Python is a popular programming language.\n",
        "It is widely used in web development.\n",
        "Many beginners start their coding journey with python.\n",
        "JavaScript is mainly used for front-end development.\n",
        "PYTHON is also great for data science and automation.\n",
        "C++ is known for its performance and speed.\n",
        "Learning to code takes practice and patience.\n"]
    f.writelines(lines)"""

"""with open('lines_w_python.txt', 'r') as f:
    content = f.readlines()
    # print(content)
    for line in content:
        if 'python' in line.lower():
            print(line.strip())"""


# 12. Read numbers.txt and find:
# - Largest number
# - Smallest number
# - Sum of all numbers
# - Average of all numbers

"""with open('numbers.txt', 'r') as f:                  # Do THIS ONE AGAIN
    content = f.read()
    lines = content.splitlines()

    biggest = float('-inf')
    smallest = float('inf')
    total = 0
    avg = 0

    for line in lines:
        num = int(line)
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
        total += num

    avg = total / len(lines)

    print(f'Largest: {biggest}\nSmallest: {smallest}\nSum: {total}\nAverage: {avg}\n')"""


# 13. Count how many uppercase letters, lowercase letters, digits, and spaces are present in a file.

"""with open('char_types.txt', 'w') as f:
    f.write('Python 3 is FUN to learn in 2026! I practice coding 5 days a week, and my SCORE keeps improving. Debugging can be Tricky, but it teaches me A LOT.')"""

"""with open('char_types.txt', 'r') as f:               # Do THIS ONE AGAIN
    content = f.read()

    upper = 0
    lower = 0
    digit = 0
    space = 0

    for char in content:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        elif char == ' ':
            space += 1

    print(f'Uppercase: {upper}\nLowercase: {lower}\nDigits: {digit}\nSpaces: {space}\n')"""

# LEVEL 4: FILE MODIFICATION

# 14. Read input.txt and copy all its contents into output.txt.

"""with open('input.txt', 'w') as f:
    text = ["Hello, this is a sample text file.\nIt has multiple lines of content.\nThis line has some numbers: 12345\nAnd this line has punctuation! Does it work? Yes, it should.\nThis is after a blank line, to test that empty lines are copied too.\nLast line of the file."]
    f.writelines(text)"""

"""with open('input.txt', 'r') as infile:               # Do THIS ONE AGAIN
    content = infile.read()

with open('output.txt', 'w') as outfile:
    outfile.write(content)"""


# 15. Copy only the lines containing more than 10 characters from input.txt to output.txt.

"""with open('input2.txt', 'w') as f:
    text = ["Short\nHi there\nThis line definitely has more than ten characters.\nNo\n1234567890\n12345678901\nCat\nA longer sentence goes here for testing purposes.\nOK\nTinyThis is another line that is long enough to pass.\nX\nYes\nPython is fun and this line is long enough too.\n"]
    f.writelines(text)"""

"""with open('input2.txt', 'r') as infile:              # Do THIS ONE AGAIN               
    lines = infile.readlines()


with open('output2.txt', 'w') as outfile:
    for line in lines:
            if len(line.strip()) > 10:
                outfile.write(line)"""

# 16. Read a file and create another file containing the same text in uppercase.

"""with open('input.txt', 'r') as infile:               
    content = infile.read()
    lines = content.splitlines()

    upper = ''
    
    for line in lines:
        upper += line.upper() + '\n'

with open('output3.txt', 'w') as outfile:
    outfile.write(upper)"""

"""with open('output3.txt', 'r') as f:
    content = f.read()
    print(f'{content!r}')"""

# 17. Replace every occurrence of "Java" with "Python" in a file.
# Hint: Read -> modify data -> write updated data.

"""with open('text_w_python.txt', 'w') as f:
    text = ["Java is a popular programming language.\n",
    "Many enterprise systems are built with Java.\n",
    "Learning Java can help you understand OOP concepts.\n"]
    f.writelines(text)"""

"""with open('text_w_python.txt', 'r') as f:                # Do THIS ONE AGAIN
    content = f.read()

    content = content.replace('Java', 'Python')
    
with open('replaced.txt', 'w') as f: 
    f.writelines(content)"""


# 18. Remove all blank lines from a file and save the cleaned content in another file.

"""with open('text_w_blanks.txt', 'w') as f:
    lines = ["Python is a popular programming language.\n",
    "\n",
    "It is widely used in web development.\n",
    "\n",
    "\n",
    "Many beginners start their coding journey with Python.\n",
    "   \n",
    "JavaScript is mainly used for front-end development.\n",
    "\n",
    "Learning to code takes practice and patience.\n"]
    f.writelines(lines)"""

"""with open('text_w_blanks.txt', 'r') as f:                # Do THIS ONE AGAIN
    content = f.readlines()
    # print(content)
    new_content = ''

    for line in content:
        if line.strip() != '':
            new_content += line
    # print(new_content)

with open('removed_blanks.txt', 'w') as f:
    f.write(new_content)"""

# 19. Reverse the order of lines in a file.

"""with open('removed_blanks.txt', 'r') as f:
    content = f.readlines()
    content = content[::-1]
    # print(content)

with open('reversed.txt', 'w') as f:
    f.writelines(content)"""


# 20. Create a new file containing only the unique words from another file.

"""with open('multiples.txt', 'w') as f:
    lines = ["Python is a popular programming language.\n",
    "Python is widely used in web development.\n",
    "Many beginners start their coding journey with python.\n",
    "JavaScript is mainly used for front-end development.\n",
    "Python is also great for data science and automation.\n",
    "C++ is known for its performance and speed.\n",
    "Learning to code takes practice and patience.\n"]
    f.writelines(lines)"""

"""with open('multiples.txt', 'r') as f:                # Do THIS ONE AGAIN
    content = f.read()
    # print(content)
    words = content.lower().split()
    # print(words)

    unique = []

    for word in words:
        word = word.strip(',.\'?!')
        if word not in unique:
            unique.append(word)

    # print(unique)

with open('unique.txt', 'w') as f:
    f.writelines('\n'.join(unique))"""
        

# LEVEL 5: EXCEPTIONS

# 21. Write a program that asks the user for a file name and reads it.
# Handle FileNotFoundError.

"""with open('sample.txt', 'w') as f:
    lines = ["This is a sample file for testing file reading.\n",
    "If you can see this, the file was found successfully.\n",
    "Try running your program again with a made-up filename\n",
    "to make sure your FileNotFoundError handling works too.\n"]
    f.writelines(lines)"""

"""filename = input('Enter file name: ')                # Do THIS ONE AGAIN

try:
    with open(filename, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Sorry, {filename} doesn't exist")"""

# CHALLENGE QUESTIONS

# 22. Create a program that compares two text files and checks whether their contents are identical.

"""with open('file_a.txt', 'w') as f:
    lines_a = ["Python is a popular programming language.\n",
    "It is widely used in web development.\n",
    "Many beginners start their coding journey with Python.\n",
    "JavaScript is mainly used for front-end development.\n",
    "Learning to code takes practice and patience.\n"]
    f.writelines(lines_a)

with open('file_b.txt', 'w') as f:
    lines_b = ["Python is a popular programming language.\n",
    "It is widely used in web development.\n",
    "Many beginners start their coding journey with JavaScript.\n",
    "JavaScript is mainly used for front-end development.\n",
    "Learning to code takes practice and patience.\n"]
    f.writelines(lines_b)"""

"""with open('file_a.txt', 'r') as f:
    content1 = f.readlines()

with open('file_b.txt', 'r') as f:
    content2 = f.readlines()

    # if content1 == content2:
    #     print('Files are identical')
    # else:
    #     print('Files differ')

    if content1 == content2:
        print('Files are identical')
    else:
        print('Files differ')
        for i, (line1, line2) in enumerate(zip(content1, content2), start=1):
             if line1 != line2:
                  print(f"Line: {i}:")
                  print(f'  File A: {line1.strip()}')
                  print(f'  File B: {line2.strip()}')

        if len(content1) != len(content2):
            print(f"Files also differ in length: File A has {len(content1)} lines, File B has {len(content2)} lines.")        
"""

# 23. Create a program that merges the contents of file1.txt and file2.txt into merged.txt.

"""with open('file1.txt', 'w') as f:
    lines = ['Python is a popular programming language.\nIt is widely used in web development.\nMany beginners start their coding journey with Python.\n']
    f.writelines(lines)

with open('file2.txt', 'w') as f:
    lines = ['JavaScript is mainly used for front-end development.\nC++ is known for its performance and speed.\nLearning to code takes practice and patience.\n']
    f.writelines(lines)"""

"""with open('file1.txt', 'r') as f:                # Do THIS ONE AGAIN
    content1 = f.read()

with open('file2.txt', 'r') as f:
    content2 = f.read()

with open('files_merged.txt', 'w') as f:
    f.write(content1)
    f.write(content2)"""

# 24. Create a program that reads a file and prints the longest line. -->

"""with open('longest_line.txt', 'w') as f:
    lines = ['This is a short line.\nHere is a medium-length line for testing.\nThe quick brown fox jumps over the lazy dog.\nA very very very very very very long line that should definitely be the longest one in this file\nTiny.\nAnother reasonably sized line for comparison.']
    f.writelines(lines)"""

"""with open('longest_line.txt', 'r') as f:             # Do THIS ONE AGAIN
    content = f.read()

    lines = content.splitlines()

    longest_length = 0
    longest_line = ''

    for line in lines:
        if len(line) > longest_length:
            longest_length = len(line)
            longest_line = line

    print(f'Line: {longest_line}\nLength: {longest_length}')"""

# with open('longest_line.txt', 'r') as f:
#     longest_line = max(f, key=len)

#     print(longest_line)
#     print(len(longest_line))