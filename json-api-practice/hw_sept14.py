import json


import requests
from pprint import pprint

# API URL
#
# URL = 'https://jsonplaceholder.typicode.com/todos'
# Question
#
# Ask:
#
# Enter user id:
#
# Print only the todos belonging to that user.
#
# Also count how many are completed and incomplete.
#
# Expected:
#
# User ID: 4
#
# Completed: 7  -->  6
# Incomplete: 13  -->  14

# parameters = {'results': 100}

# response = requests.get(URL)
# print(response)

# content = response.json()
# print(content)
#
# compl_todos = 0
# incompl_todos = 0
#
# for entry in content:
#     if entry['userId'] == 4:
#         if entry['completed']:
#             compl_todos += 1
#         else:
#             incompl_todos += 1
#
# print(f"Completed: {compl_todos}\nIncomplete: {incompl_todos}")



##########




# API URL
#
# https://randomuser.me/api/
# Question
#
# Fetch 20 random users.
#
# Print:
#
# Name
# Age
# Country
#
# Then find the oldest person.


# parameters_20 = {'results': 20}
# URL_random = 'https://randomuser.me/api/'
# #
# # response = requests.get(URL_random, parameters_20).json()
# # pprint(response)

# oldest = 0
# person = {}

# for entry in response['results']:
    # pprint(f"Name: {entry['name']['title']} {entry['name']['first']} {entry['name']['last']}, Age: {entry['dob']['age']}, Country: {entry['location']['country']}")

#     age = entry['dob']['age']
#
#     if age > oldest:
#         oldest = age
#         person = {'title': entry['name']['title'], 'first': entry['name']['first'], 'last': entry['name']['last']}
#
#
# print(f"Highest Age: {oldest}, Name: {person['title']} {person['first']} {person['last']}")


# Question
#
# Fetch 100 users.
#
# Create a dictionary:
#
# {
# "Australia": 8,
# "Germany": 5,
# "France": 9
# }
#
# The country should be the key and number of users should be the value.

# parameters_100 = {'results': 100}
# response2 = requests.get(URL_random, parameters_100).json()
#
# country_users = {}
#
# for entry in response2['results']:
#     country = entry['location']['country']
#     if country not in country_users:
#         country_users[country] = 0
#     country_users[country] += 1
#
# pprint(country_users)



#########



# Question
#
# Fetch 25 users.
#
# The API gives lots of unnecessary information.
#
# Create your own cleaned structure:
#
# {
# "name": "John Smith",
# "age": 32,
# "email": "...",
# "country": "..."
# }
#
# Save all users into:
#
# people.json


# parameters_25 = {'results': 25}
# URL_random = 'https://randomuser.me/api/'
#
# response = requests.get(URL_random, parameters_25).json()
#
# people = []
#
# for entry in response['results']:
#     # print(entry)
#     person = {'name': f"{entry['name']['first']} {entry['name']['last']}", 'age': entry['dob']['age'], 'email': entry['email'], 'country': entry['location']['country']}
#     # print(person)
#
#     people.append(person)
#
# pprint(people)

# with open('people.json', 'w') as f:
#     json.dump(people, f)


#########


# Question
#
# Do not call the API.
#
# Read:
#
# people.json
#
# Print only users older than 50.

# with open('people.json', 'r') as f:
#     data = json.load(f)
#
# older_50 = []
#
# for entry in data:
#     if entry['age'] > 50:
#         older_50.append(entry)
#
#
# pprint(older_50)