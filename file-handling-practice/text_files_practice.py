# Write only reviews containing the word "bad" into negative_reviews.txt.
#
# Example input:
#
text = """The product is good
Delivery was bad
Very useful product
Bad packaging"""
#
# Expected output:
#
# Delivery was bad
# Bad packaging
#
# Use case-insensitive matching.

# with open('negative_reviews.txt', 'w') as f:
#     f.write(text)

# with open('negative_reviews.txt', 'r') as f:
#     # content = f.read()
#
#     review = []
#
#     for line in f:
#         if 'bad' in line.lower():
#             review.append(line)
#     str_review = ''.join(review)
#
#     print(str_review)
#
# with open('negative_reviews.txt', 'w') as f:
#     f.write(str_review)






# Find failed students
#
# marks.txt:
#
# students = """Aman,78
# Riya,32
# Karan,65
# Neha,29
# Sam,90"""
#
# Read the file and write students having marks below 40 into failed_students.txt.
#
# Expected:
#
# Riya,32
# Neha,29



# with open('marks.txt', 'w') as f:
#     f.write(students)

# with open('marks.txt', 'r') as f:
#     content = f.readlines()
#
#     failed = []
#
#     for student in content:
#         s = student.strip().split(',')
#         # print(student)
#         marks = int(s[1])
#         if marks < 40:
#             failed.append(student)
#
#     print(failed)
#
#
# with open('failed_students.txt', 'w') as f:
#     f.writelines(failed)





# Find low-stock products
#
# inventory.txt:
#
# Laptop,15
# Mouse,3
# Keyboard,8
# Monitor,2
# Webcam,0
#
# Write products having stock below 5 into low_stock.txt.
#
# Expected:
#
# Mouse: 3
# Monitor: 2
# Webcam: 0



# Extract hashtags
#
# posts.txt:
#
# text = """Learning #Python today
# Working on #MachineLearning
# Beautiful weather today
# Practicing #DSA and #Coding"""
#
# Read the file and write only the lines containing at least one # into hashtag_posts.txt.


# with open('posts.txt', 'w') as f:
#     f.write(text)

# with open('posts.txt', 'r') as f:
#
#     hashes = []
#
#     for line in f:
#         words = line.strip().split()
#         for word in words:
#             if word.startswith('#'):
#                 w = word[1:]
#                 hashes.append(f'{w}\n')
#
# with open('hashtag_posts.txt', 'w') as f:
#     f.writelines(hashes)






# Remove duplicate lines
#
# customers.txt:

# customers = ['Aman\n'
# 'Riya\n'
# 'Aman\n'
# 'Sam\n'
# 'Riya\n'
# 'Neha\n']

# Create unique_customers.txt:
#
# Aman
# Riya
# Sam
# Neha
#
# Try to preserve the original order


# with open('customers.txt', 'w') as f:
#     f.writelines(customers)

# with open('customers.txt', 'r') as f:
#     content = f.readlines()
#
#     unique = set(content)
#
#     # unique = []
#     #
#     # for name in content:
#     #     # name = name.strip()
#     #     if name not in unique:
#     #         unique.append(name)
#
#     print(unique)
#
# # with open('unique_customers.txt', 'w') as f:
# #     f.writelines(unique)




# Find
# invalid
# emails
#
# emails.txt:
#
# emails = ['aman @ gmail.com\n'
# 'riya.gmail.com\n'
# 'sam @ yahoo.com\n'
# 'karan @ company\n'
# 'neha @ hotmail.com\n']
#
# Write
# emails
# that
# do
# not contain
# both @ and.into
# invalid_emails.txt.


# with open('emails.txt', 'w') as f:
#     f.writelines(emails)

# with open('text_files/text_files_practice/emails.txt', 'r') as f:
#     content = f.readlines()
#     invalid = []
#
#     for entry in content:
#         e = entry.split()
#         # print(e)
#         if '@' not in e and '.' not in e:
#             invalid.append(entry)
#
#     # print(invalid)
#
# with open('text_files/text_files_practice/invalid_emails.txt', 'w') as f:
#     f.writelines(invalid)



# Missing Invoice Numbers
# invoice_sequence.txt
# INV1001
# INV1002
# INV1003
# INV1005
# INV1006
# INV1008
# INV1009
# Question: Invoice numbers should be sequential. Find the missing invoice numbers.
# Expected:
# INV1004
# INV1007
