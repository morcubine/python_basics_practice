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

