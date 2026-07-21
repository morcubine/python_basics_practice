import requests

# Question 1
# URL: https://jsonplaceholder.typicode.com/users/1
# Steps:
# 1. Import requests.
# 2. Send GET request.
# 3. Check status_code==200.
# 4. If yes convert response to dict and print Name, Username, Email.
# 5. Else print 'Request Failed'.

# import requests
# URL = "https://jsonplaceholder.typicode.com/users/1"
#
# data = requests.get(URL)
# print(data)
#
# if data.status_code == 200:
#     response = data.json()
#     print(response['name'], response['username'], response['email'])
# else:
#     print("Request failed")
# Status codes -> 200.... success
# 400 -> 404 not found -> server ->




# Question 2
# URL: https://jsonplaceholder.typicode.com/users/3
# Steps:
# 1. Send GET request.
# 2. Check status code.
# 3. Access nested address dict.
# 4. Print Street, Suite, City, Zipcode.

# URL = 'https://jsonplaceholder.typicode.com/users/3'
# response = requests.get(URL)
# # print(response)
# data = response.json()
# address = data['address']

# # print(address['street'], address['suite'], address['city'], address['zipcode'])

# keys = ['street', 'suite', 'city', 'zipcode']

# for key in keys:
#     print(address[key])


# print(data['address'])




# Question 3
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Fetch all users.
# 2. Ask user for city.
# 3. Print names from that city.
# 4. If none print 'No users found'.

# import requests
# URL = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(URL)
# data = response.json()
#
# city = input("Enter city? ")
# for item in data:
#     if city == item['address']['city']:
#         print(item['name'])




# Question 4
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Fetch all users.
# 2. Print users whose email contains '.biz'.
# 3. Print Name -> Email.

# URL = 'https://jsonplaceholder.typicode.com/users'

# response = requests.get(URL)
# # print(response)
# entry = response.json()
# # print(entry)

# users = []

# for item in entry:
#     emails = item['email'].endswith('.biz')
#     if emails:
#         users.append(item)

# print(users)




# Question 5
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Find user with longest name.
# 2. Print Name, Email, Company name.


# URL = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(URL)
# data = response.json()
# longest_len = 0
# name = ""
# for item in data:
#     if len(item['name']) > longest_len:
#         longest_len = len(item['name'])
#         name = item['name']

# print(name, longest_len) 




# Question 6
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Sort users by length of name.
# 2. Print Name (Length).

# URL = 'https://jsonplaceholder.typicode.com/users'

# response = requests.get(URL)

# data = response.json()
# # print(type(data))

# names = sorted(data, key=lambda x: len(x['name']))
# # print(names)
# # names_only = []

# # for item in names:
# #     names_only.append(item['name'])


# # print(names_only)




# Question 7
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Ask username.
# 2. Print complete dictionary if found.
# 3. Else print 'Username not found'.

"""URL = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(URL)
data = response.json()
# print(data)

name = input('Enter name: ')

for item in data:
    if name.title() in item['name']:
            print(item)
            break
else:
    print('Username not found')"""




# Question 8
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Count unique company names.

'''URL = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(URL)
data = response.json()
# print(data)

companies = []
count = 0

for item in data:
    companies.append(item['company']['name'])

count = len(set(companies))


# for entry in companies:
#     count += 1

print(f'{companies}\ncompany count: {count}')'''




# Question 9
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Find user with highest ID.
# 2. Print Name and ID.

"""URL = 'https://jsonplaceholder.typicode.com/users'

respone = requests.get(URL)
data = respone.json()
# print(sorted(data, key=lambda x: x['id']))

count = 0
highest_id = 0
name = ''

for item in data:
    count = item['id']
    if count > highest_id:
        highest_id = count
        name = item['name']

print(f'{name}, {highest_id}')"""




# Question 10
# URL: https://jsonplaceholder.typicode.com/users
# Steps:
# 1. Create new list of dicts with keys: name, city, company.
# 2. Print new list.

# URL = 'https://jsonplaceholder.typicode.com/users'

# response = requests.get(URL)
# data = response.json()
# # print(data)
# new_data = []

# for item in data:
#     new_data.append({'name': item['name'], 'city': item['address']['city'], 'company': item['company']['name']})

# print(new_data)




# Question 11
# URL: https://jsonplaceholder.typicode.com/posts
# Steps:
# 1. Fetch posts.
# 2. Count posts where userId==5.

"""URL = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(URL)
data = response.json()
# print(data)

total = 0

for item in data:
    if item['userId'] == 5:
        total += 1

print(total)"""




# Question 12
# URL: https://jsonplaceholder.typicode.com/posts
# Steps:
# 1. Find post with longest title.
# 2. Print ID, Title, User ID.

"""URL = 'https://jsonplaceholder.typicode.com/posts'


longest_title = 0
post = ''

user = []

response = requests.get(URL)
data = response.json()
# print(data)

for item in data:
    len_title = len(item['title'])
    if len_title > longest_title:
        longest_title = len_title
        post = item['body']

        user = [item['id'], item['title'], item['userId']]


print(user)"""



# Question 13
# URL: https://jsonplaceholder.typicode.com/posts
# Steps:
# 1. Print posts whose title contains 'est'.
# 2. Print ID and Title.

"""URL = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(URL)

data = response.json()
# print(data)

posts = []

for item in data:
    if 'est' in item['title']:
        posts.append({item['id'], item['title'], item['body']})

print(posts)"""




# Question 14
# URL: https://jsonplaceholder.typicode.com/posts
# Steps:
# 1. Send POST with title/body/userId.
# 2. Check status_code==201.
# 3. Print status code, response JSON and returned ID.

URL = 'https://jsonplaceholder.typicode.com/posts'

# response = requests.get(URL)
# print(response)
# data = response.json()
# print(data)

# new_data = {
#     'title': 'Romeo and Juliet',
#     'body': 'where for art thou Romeo',
#     'userId': 100
# }
     

# sending = requests.post(URL, data=new_data)
# print(sending.json(), sending.status_code)



