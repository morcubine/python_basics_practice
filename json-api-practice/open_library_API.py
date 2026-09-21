import requests
from pprint import pprint


# API URL
#
# URL = 'https://openlibrary.org/search.json'
# Question
#
# Ask:
#
# Search book:
#
# Display the first five results:
#
# Title:
# Author:
# First Published:



# # print(response)
# book_title = input('Enter book title: ')
# pages = int(input('Enter number of pages: '))
#
# params = {'q': book_title, 'limit': pages}
#
# response = requests.get(URL, params=params).json()
# # pprint(response)
#
# total_books = 0
#
# for data in response['docs']:
#     total_books += 1
#     if 'author_name' in data:
#         print(data['author_name'], data.get('first_publish_year', 1990), data['title'])
#
#     else:
#         print('Book does not exist')
#
# print(total_books)


"""Homework TODO"""


# Question
#
# Search for a topic.
#
# Among the first 50 results, find the book with the earliest first_publish_year.




# API URL

URL = 'https://api.open-meteo.com/v1/forecast'

# Question
#
# Get:
#
# temperature
# humidity
# wind speed

params = {'latitude': 19.2, 'longitude': 109.7, 'current': ['temperature_2m', 'wind_speed_10m', 'relative_humidity_2m']}

response = requests.get(URL, params=params).json()
# pprint(response)

current = response['current']

humidity = current['relative_humidity_2m']
temp = current['temperature_2m']
wind = current['wind_speed_10m']

print(f'Temperature: {temp}\nHumidity: {humidity}\nWind: {wind}')


"""Homework TODO"""


# Question
#
# Get hourly temperature data.
#
# Find:
#
# Highest temperature
# Lowest temperature
# Average temperature


"""Homewrk TODO"""


# Question
#
# Ask:
#
# Topic: Python
# Minimum Year: 2015
#
# Print only books first published in or after that year.












