import requests
from pprint import pprint


# https://jsonplaceholder.typicode.com/todos
# Question


# Fetch all todos.
#
# Find:
#
# Total todos
# Completed todos
# Incomplete todos
#
# Also print the titles of only the incomplete todos.

# URL = 'https://jsonplaceholder.typicode.com/todos'
# response = requests.get(URL)
#
# # print(response)
# content = response.json()
#
# todos = 0
# completed = 0
# incompleted = 0
#
# for entry in content:
#     todos += 1
#     if entry['completed']:
#         completed += 1
#     else:
#         incompleted += 1
#         print(f'Incomplete tasks: {entry["title"]}')
#
# print(f'TODO: {todos}, completed: {completed} , incompleted: {incompleted}')




# APIs
#
# https://jsonplaceholder.typicode.com/users
# https://jsonplaceholder.typicode.com/posts
# Question
#
# Fetch users and posts.
#
# For every user, calculate how many posts they have.
#
# Expected:
#
# Leanne Graham: 10 posts
# Ervin Howell: 10 posts



# URL_users = 'https://jsonplaceholder.typicode.com/users'
# URL_posts = 'https://jsonplaceholder.typicode.com/posts'
#
# response_users = requests.get(URL_users).json()
# # pprint(response_users)
#
# response_posts = requests.get(URL_posts).json()
# # pprint(response_posts)
#
# users = {}
#
#
#
# for user in response_users:
#     for entry in response_posts:
#         if entry['userId'] == user['id']:
#             name = user['name']
#             if name not in users:
#                 users[name] = 0
#             users[name] += 1
#
#
#
# print(users)


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


####




parameters = {'results': 25}

response = requests.get('https://randomuser.me/api/', parameters).json()
# pprint(response)

for entry in response['results']:
    print(entry)
