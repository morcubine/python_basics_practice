# Clean a messy transaction dataset
# transactions = [
#     {"id": "T101", "amount": " 1200 ", "status": "SUCCESS"},
#     {"id": "T102", "amount": "-500", "status": "FAILED"},
#     {"id": "T103", "amount": "850", "status": "SUCCESS"},
#     {"id": "T104", "amount": "invalid", "status": "SUCCESS"},
#     {"id": "T105", "amount": "2500", "status": "SUCCESS"},
# ]
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




#
#
# Find employees with unusual salary differences
# employees = {
#     "Aman": [50000, 52000, 54000],
#     "Sara": [70000, 70000, 71000],
#     "John": [45000, 50000, 62000],
#     "Mira": [90000, 93000, 95000],
# }
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




#
# Extract words using multiple rules
# sentences = [
#     "Python makes data processing easier",
#     "Data engineers use Python extensively",
#     "Processing large datasets requires memory",
# ]
#
# Produce a collection of unique lowercase words that:
#
# have at least 6 characters
# appear in exactly one sentence
# do not start with a vowel
#
# Do not manually create a list of words beforehand.





# Compare two inventories
# warehouse_a = {
#     "laptop": 10,
#     "mouse": 30,
#     "keyboard": 15,
#     "monitor": 8,
# }
#
# warehouse_b = {
#     "laptop": 4,
#     "mouse": 35,
#     "monitor": 12,
#     "webcam": 20,
# }
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