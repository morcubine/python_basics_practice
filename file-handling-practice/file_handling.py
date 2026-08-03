# x = 5

# read, write, append

# modes -> 'r', 'rt', 'wt', 'w', 'a', 'w+', 'r+',

# with open('hw_mixed.txt', 'r') as f:
    # content = f.read(10) # reads everything -> string
    # print(content)
    # content = f.readline()
    # next(f)
    # content1 = f.readline()
    # print(content1)
    # content = f.readlines()
    # print(content[4])
    # for line in f:
    #     print(line)

# lines = ['hello world\n', 'apple mango\n']
# with open('apples.txt', 'w') as f:
    # f.write('hello world')
    # f.write('\napple world')
    # f.writelines(lines)

# with open('apples.txt', 'a') as f:
#     f.write('grapes\n')

# count = 0
# with open('hw_mixed.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         if line != "":
#             count += 1
# print(count)

# count = 0
# with open('hw_mixed.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         words = line.split()
#         count += len(words)
# print(count)


# count = 0
# with open('hw_mixed.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         if 'appears' in line:
#             print("Found")
#             break
#     else:
#         print("couldn't find it")

# try:
#     with open('test.text', 'r') as f:
#         content = f.read()
#         print(content)
# except FileNotFoundError as e:
#     print(e)
#
# print("hello world")

# vowels
# vowels = "aeiou"
# count = 0
# with open('hw_mixed.txt', 'r') as f:
#     for line in f:
#         line = line.strip()
#         for char in line:
#             if char in vowels:
#                 count += 1
#     print(count)



#   1.
#   Create a file named notes.txt and write:
#   Python is easy.
#   I am learning file handling.
#   Practice makes programming better.


# with open('notes.txt', 'r') as f:
#     content = f.read()
#     print(content)

#   2.

# with open('languages.txt', 'r') as f:
#     content = f.readlines()
#     for line in content:
#         print(line)

#   3.

# with open('languages.txt', 'r') as f:
#     content = f.readlines()
#     for line in content:
#         line = line.strip()
#         print(line)

#   4./5.

# with open('numbers.txt', 'r') as f:
#     content = f.read()
#     print(f'{content!r}')
#     lines = content.splitlines()
#     print(lines)
#     total = 0
#     for num in lines:
#         total += int(num)
#     print(total)

#   6.

# with open('students.txt', 'a') as f:
#     f.write('\nAniket')
#     f.write('\nNeha')

#   7.

# with open('notes.txt', 'a') as f:
#     f.writelines(['\nErrors help you learn faster\n', 'Debugging is a skill worth learning\n', 'Consistency beats intensity\n'])

#   8.

# with open('paragraph.txt', 'r') as f:
#     content = f.read()
#     total = 0
#     # print(f'{content!r}')
#     for char in content:
#         if char != '\n':
#             total += 1
#     print(total)

#   9.

# with open('paragraph2.txt', 'r') as f:
#     content = f.readlines()
#     # print(content)
#     total = 0
#     for line in content:
#         words = line.lower().split()
#         # print(words)
#         for word in words:
#             if word == 'python':
#                 total += 1
#     print(total)

#   10.

# with open('paragraph.txt', 'r') as f:
#     content = f.readlines()
#     word = input('Enter word: ')
#     for line in content:
#         if word in line:
#             print('Word found')
#             break
#     else:
#         print('Word not found')

    
#   11.

# with open('paragraph2.txt', 'r') as f:
#     content = f.readlines()
#     # print(content)
#     for line in content:
#         sentences = line.split('.')
#         for sentence in sentences:
#             if 'Python' in sentence:
#                 print(sentence)

#   12.

# Find:
# - Largest number
# - Smallest number
# - Sum of all numbers
# - Average of all numbers

# with open('numbers.txt', 'r') as f:
#     content = f.read()
#     lines = content.splitlines()
#     biggest = 0
#     for num in lines:
#         if int(num) > biggest:
#             biggest = int(num)
#     print(biggest)


# with open('numbers.txt', 'r') as f:
#     content = f.read()
#     lines = content.splitlines()
#     smallest = []
#     for num in lines:
#         smallest.append(int(num))

#     print(min(smallest))


# with open('numbers.txt', 'r') as f:
#     content = f.read()
#     lines = content.splitlines()
#     total = 0
#     for num in lines:
#         total += int(num)
#     print(total)       


# with open('numbers.txt', 'r') as f:
#     content = f.read()
#     lines = content.splitlines()
#     total = 0
#     for num in lines:
#         total += int(num)

#     ave = total / len(lines)
#     print(ave)

#   13. 

#   Count how many uppercase letters, lowercase letters, digits, and spaces are present in a file.

# with open('paragraph2.txt', 'r') as f:
#     content = f.read()
#     lines = content.splitlines()
#     # print(lines)
#     uppers = 0
#     lowers = 0
#     digits = 0
#     spaces = 0

#     for line in lines:
#         for char in line:
#             if char.isupper():
#                 uppers += 1
#             if char.islower():
#                 lowers += 1
#             if char.isdigit():
#                 digits += 1
#             if char == '\n':
#                 spaces +=1

    # print(f'Uppercase:{uppers} \nLowercase: {lowers} \nDigits: {digits} \nSpaces: {spaces}')

#   14.

# with open('input.txt', 'r') as infile:
#     content = infile.read()

# with open('output.txt', 'w') as outfile:
#     outfile.write(content)
    
#   15.

# with open('input.txt', 'r') as infile:
#     lines = infile.readlines()

# with open('output2.txt', 'w') as outfile:
#     for line in lines:
#         if len(line.strip()) > 10:
#             outfile.write(line)

#   16.

# with open('input.txt', 'r') as infile:
#     content = infile.read()

# with open('output3', 'w') as outfile:
#     outfile.write(content.upper())

#   17.

#   Replace every occurrence of "Java" with "Python" in a file.
#   Hint: Read -> modify data -> write updated data.

# with open('replace.txt', 'r') as f:
#     content = f.read()

# upd_content = content.replace('Java', 'Python')

# with open('replace.txt', 'w') as f:
#     f.write(upd_content)

#   18. 
#   Remove all blank lines from a file and save the cleaned content in another file.

# with open('messy.txt', 'r') as f:
#     content = f.readlines()

# with open('clean.txt', 'w') as f:
#     for line in content:
#         if line.strip() != '':
#             f.write(line)

#   19.
#   Reverse the order of lines in a file.

# with open('clean.txt', 'r') as f:
#     content = f.read().splitlines()
#     # print(content)

# with open('reversed.txt', 'w') as f:
#     reversed_content = content[::-1]
#     for line in reversed_content:
#         f.write(line + '\n')

#   20.
#   Create a new file containing only the unique words from another file.

# with open('word_source.txt', 'r') as f:
#     content = f.readlines()

#     punctuation = '.,!?;:\'"()'

#     new_words = []
#     for line in content:
#         words = line.lower().split()
#         for word in words:
#             clean_word = word.strip(punctuation)
#             if clean_word not in new_words:
#                 new_words.append(clean_word)

# with open('unique_words.txt', 'w') as f:
#     f.write('\n'.join(new_words))




        
    









