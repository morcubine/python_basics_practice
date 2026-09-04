import re
from unittest import result

# Write a regex to find all numbers that contain exactly 6 digits

# text = 'Order 12345 shipped. Tracking: 987654. Invoice #4567890 pending. Zip code 08540 or 908540? Product SKU: 123456789. Reference number 555555 confirmed. Old code: 4444.'

# pattern = r'\d{6}'
# result = re.findall(pattern, text)
# print(result)

# Write a regex to find numbers that contain at least 4 digits.

# pattern = r"\d{4}"
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)

# Find all whitespace characters from a string containing spaces, tabs, and newlines

# text = "Hello\tWorld\nThis is   a test.\n\tGoodbye"
#
# pattern = r'\s'
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)

# Extract all product codes that follow this format:
# ABC-1234
# XYZ-5678
#
# Rules:
#
# exactly 3 uppercase letters
# one -
# exactly 4 digits

# text = "Items: ABC-1234, xyz-5678, AB-1234, ABCD-1234, ABC-123, ABC-12345, XYZ-5678 confirmed."
#
# pattern = r'\b[A-Z]{3}-\d{4}\b'
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)



# From the text below, extract only valid email addresses:
# text = """
# sales@company.com
# hello@gmail.com
# wrong@email
# @test.com
# admin123@shop.in
# """

# pattern = r'\w+[@]\w+[.]\w+'
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)


# Find all dates written in either of these formats:
# 12-09-2026
# 12/09/2026
#
# from:
#
# text = "Orders were placed on 12-09-2026, 15/08/2026 and 2026-09-12"
#
# pattern = r"\d{2}[/-]\d{2}[-/]\d{4}"
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)



# Find all invoice IDs that start with INV followed by exactly 6 digits.
#
# Example:
#
# INV123456
# INV987654

# text = "Invoices: INV123456, INV98765, INV1234567, inv123456, INV987654 processed."
#
# pattern = r'\b[A-Z]{3}\d{6}\b'
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)

# Find all filenames ending in:
# .pdf
# .csv
# .txt
#
# from:
#
# text = "report.pdf data.csv image.jpg notes.txt backup.exe"
#
# pattern = r'\w+\.(?:pdf|csv|txt)\b'
# # noinspection redeclaration
# result = re.findall(pattern, text)
# print(result)

# Find all lines starting with ERROR.

# text = """
# INFO System started
# ERROR Motor failure
# WARNING Temperature high
# ERROR Voltage too low
# INFO System stopped
# """
#
# pattern = r'^ERROR.*'
# # noinspection redeclaration
# result = re.findall(pattern, text, re.MULTILINE)
# print(result)

