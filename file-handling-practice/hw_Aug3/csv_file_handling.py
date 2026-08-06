import csv

# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     print(type(reader))
#     for row in reader:
#         print(type(row))

# with open('data.csv', 'a') as f:
#     writer = csv.writer(f)
#     writer.writerow([])
#     writer.writerow(['Dita', 12, 'Sweden'])

# with open('data.csv', 'a', newline="\n") as f:
#     writer = csv.writer(f)
#     writer.writerows([['Dita', 12, 'Sweden'], ['Dita', 12, 'Sweden']])

# fieldnames = ['Name', 'Age', 'City']
# with open('data.csv', 'a') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writerow({'Name': 'Urvashi', 'Age': 24, 'City': 'Delhi'})

# fieldnames = ['Name', 'Age', 'City']
# with open('data.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'Name': 'Urvashi', 'Age': 24, 'City': 'Delhi'})


# fieldnames = ['Name', 'Age', 'City']
# with open('data.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows([{'Name': 'Urvashi', 'Age': 24, 'City': 'Delhi'}, {'Name': 'Urvashi', 'Age': 24, 'City': 'Delhi'}])

# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['Name'])


# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row[0][-1])

# with open('data.csv', 'r') as f:
#     reader = csv.reader(f)
#     total = 0
#     for row in reader:
#         total += 1
#     print(total)

# with open('data.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     count = 0
#     for row in reader:
#         if row['City'] != '':
#             count += 1
#     print(count)

