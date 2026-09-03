# new_list = []
# with open('data.txt', 'r') as f:
#     content = f.readlines()
#     for line in content:
#         words = line.split()
#         for word in words:
#             if 'a' in word.lower():
#                 new_list.append(word)
# print(new_list)

# Regex

# > < == = . \ ! ' *

# print("hello" * 3)
# x = (2, 3, 4, 5, 6)
# *a, b, c = x
# print(a)

# x = [2, 3, 4]
# y = 9
# z = 8
# a = (*x, y, z)
# print(a)

# Regex -> Regular expressions
# \d -> digit (0-9)

import re
# text = "Room number is 404"
# pattern = r"\d\d"
# result = re.findall(pattern, text)
# print(result)

# \s -> spaces
# text = "Room number is 40 456 45 "
# pattern = r"\d\d\s"
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 40 456 45 "
# pattern = r"\d+" # one or more
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"\d{10}" # {3} means exactly 3
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 3425678921 342352342235553 2323513 68659"
# pattern = r"\d{10,}" # {3} means exactly 3
# result = re.findall(pattern, text)
# print(result)


# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"\d{6,15}" # range
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"\s\d+?" # range
# result = re.findall(pattern, text)
# print(result)

# one or more ----- 0 or 1

# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"\d*" # 0 or more
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"\w{5,}" # char -> [A-Za-z0-9]
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"[1-9]{5,}" # range
# result = re.findall(pattern, text)
# print(result)

# text = "Room number is 3425678921 34235 2323513 68659"
# pattern = r"[A-Za-z]{5,}" # range
# result = re.findall(pattern, text)
# print(result)

# with open('hashtags.txt', 'r') as f:
#     content = f.read()
#
# pattern = r"[#][A-Za-z]+" # range
# result = re.findall(pattern, content)
# print(result)


# . -> any character
# text = "accccat bat rat"
# pattern = r".+at" # range
# result = re.findall(pattern, text)
# print(result)


# starts with -> ^

# text = "Fridge model XO34"
# pattern = r"^Fridge"
# result = re.search(pattern, text)
# print(result)


# ends with -> $

# text = "Fridge model XO34 car"
# pattern = r"car$"
# result = re.search(pattern, text)
# print(result)

# text = "Orders were placed on 12-09-2026, 15/08/2026 and 2026-09-12"
# pattern = r"\d{2}-\d{2}-\d{4}"
# result = re.findall(pattern, text)
# print(result)


# terminal
# cd Desktop
# cd name_of_folder
# git status
# claude -> give command for git config setup in terminal
# git pull