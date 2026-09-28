# Clean a messy transaction dataset
from enum import unique

transactions = [
    {"id": "T101", "amount": " 1200 ", "status": "SUCCESS"},
    {"id": "T102", "amount": "-500", "status": "FAILED"},
    {"id": "T103", "amount": "850", "status": "SUCCESS"},
    {"id": "T104", "amount": "invalid", "status": "SUCCESS"},
    {"id": "T105", "amount": "2500", "status": "SUCCESS"},
]
#
# Create a dictionary:
#
# {
#     "T101": 1200,
#     "T103": 850,
#     "T105": 2500
# }
#
# Include a transaction only when:
#
# its status is "SUCCESS"
# amount contains a valid integer
# the amount is positive
#
# Do not modify the original data.



# succeeded_transactions = {}
#
# for data in transactions:
#     # print(data)
#     if data['status'] != 'SUCCESS':
#         continue
#     try:
#         amount = int(data['amount'].strip())
#     except ValueError:
#         continue
#
#     if amount > 0:
#         succeeded_transactions[data['id']] = amount
#
#
# print(succeeded_transactions)

# succeeded_transactions = {data['id']: int(data['amount'].strip()) for data in transactions if data['status'] == 'SUCCESS' and data['amount'].strip().lstrip('-').isdigit() and int(data['amount'].strip()) > 0}
#
# print(succeeded_transactions)





# Find employees with unusual salary differences
employees = {
    "Aman": [50000, 52000, 54000],
    "Sara": [70000, 70000, 71000],
    "John": [45000, 50000, 62000],
    "Mira": [90000, 93000, 95000],
}
#
# For every employee, calculate the difference between their highest and lowest recorded salary.
#
# Create a dictionary containing only employees whose difference is greater than 5000.
#
# Expected structure:
#
# {
#     "John": 17000
# }


# greater_than_5000 = {}
#
# for employee in employees:
#     salary = employees[employee]
#     if max(salary) - min(salary) > 5000:
#         salary_diff = max(salary) - min(salary)
#         greater_than_5000[employee] = salary_diff
#
# print(greater_than_5000)

# greater_than_5000 = {employee: max(employees[employee]) - min(employees[employee]) for employee in employees if max(employees[employee]) - min(employees[employee]) > 5000}
# print(greater_than_5000)



"""START HERE"""


# Extract words using multiple rules
sentences = [
    "Python makes data processing easier",
    "Data engineers use Python extensively",
    "Processing large datasets requires memory",
]

# Produce a collection of unique lowercase words that:
#
# have at least 6 characters
# appear in exactly one sentence
# do not start with a vowel
#
# Do not manually create a list of words beforehand.

# print(sentences)



word_count = {}

vowels = 'aeiou'

unique_words = []

for sentence in sentences:
    words = sentence.lower().split()
    # print(words)
    seen_in_sentence = set()

    for word in words:
        if word not in seen_in_sentence:
            seen_in_sentence.add(word)
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1

# print(word_count)

for word in word_count:
    count = word_count[word]
    if len(word) >= 6 and count == 1 and word[0] not in vowels:
        unique_words.append(word)

# print(unique_words)



# Compare two inventories
warehouse_a = {
    "laptop": 10,
    "mouse": 30,
    "keyboard": 15,
    "monitor": 8,
}

warehouse_b = {
    "laptop": 4,
    "mouse": 35,
    "monitor": 12,
    "webcam": 20,
}
#
# Create a dictionary containing products present in both warehouses.
#
# The value should be the total available quantity.
#
# However, include only products whose combined quantity is at least 20.
#
# Expected result:
#
# {
#     "mouse": 65,
#     "monitor": 20
# }

both_warehouses = {}


for item in warehouse_a:
    if item in warehouse_b:
        total = warehouse_a[item] + warehouse_b[item]
        if total >= 20:
            both_warehouses[item] = total

# for k, v in warehouse_a.items():
#     # print(item)
#     if k in warehouse_b:
#         total = v + warehouse_b[k]
#         if total >= 20:
#             both_warehouses[k] = total


# both_warehouses = {item: total for item in warehouse_a if item in warehouse_b and (total:= warehouse_a[item] + warehouse_b[item]) >= 20}


print(both_warehouses)







