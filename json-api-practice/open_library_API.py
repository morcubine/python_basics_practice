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



# book_title = input('Enter book title: ')
# entries = int(input('Number of entries: '))
#
# params = {'q': book_title, 'limit': entries}
# # params = {'q': book_title, 'limit': 5}
#
#
# response = requests.get(URL, params=params).json()
# # pprint(response)
#
# total_books = len(response['docs'])
#
# for data in response['docs']:
#     # total_books += 1
#     if 'title' in data:
#         print(f"{data['title']}, author: {', '.join(data['author_name'])}, published: {data.get('first_publish_year', 'unkown')}")
#     else:
#         print('Book does not exist')
#
# print(f'Number of books: {total_books}')


"""Homework TODO"""


# Question
#
# Search for a topic.
#
# Among the first 50 results, find the book with the earliest first_publish_year.



# book_topic = input('Enter topic of a book: ')
#
# params = {'q': book_topic, 'limit': 50}
#
# response = requests.get(URL, params=params).json()
# # pprint(response)
#
# earliest_publ = float('inf')
# title = ''
#
# for data in response['docs']:
#     if 'first_publish_year' in data and data['first_publish_year'] < earliest_publ:
#         earliest_publ = data['first_publish_year']
#         title = data['title']
#
#
#
# if title:
#     print(f'Book "{title.title()}", first published: {earliest_publ}')
# else:
#     print('No books with known publish year found')


"""Homewrk TODO"""


# Question
#
# Ask:
#
# Topic: Python
# Minimum Year: 2015
#
# Print only books first published in or after that year.


# book_topic = input('Enter topic of a book: ')
# publ_year = int(input('Enter publish year: '))
#
# params = {'q': book_topic, 'limit': 50}
#
# response = requests.get(URL, params=params).json()
# # pprint(response)
#
#
# for data in response['docs']:
#     title = data['title']
#     if 'first_publish_year' in data:
#         year = data['first_publish_year']
#         if data['first_publish_year'] >= publ_year:
#             print(f'Book "{title.title()}", published {year}')
#     else:
#         print('Book not found')




# API URL

URL = 'https://api.open-meteo.com/v1/forecast'

# Question
#
# Get:
#
# temperature
# humidity
# wind speed

# params = {'latitude': 19.2, 'longitude': 109.7, 'current': ['temperature_2m', 'wind_speed_10m', 'relative_humidity_2m']}
# params = {'latitude': 19.2, 'longitude': 109.7, 'daily': ['temperature_2m_max' , 'temperature_2m_mean' , 'temperature_2m_min'] }
# params = {'latitude': 19.2, 'longitude': 109.7, 'hourly': 'temperature_2m'}
# #
# response = requests.get(URL, params=params).json()
# # pprint(response)
#
# current = response['current']
#
# humidity = current['relative_humidity_2m']
# temp = current['temperature_2m']
# wind = current['wind_speed_10m']
#
# print(f'Temperature: {temp}\nHumidity: {humidity}\nWind: {wind}')


"""Homework TODO"""


# Question
#
# Get hourly temperature data.
#
# Find:
#
# Highest temperature: 31.4
# Lowest temperature: 21.2
# Average temperature: 24.83

# daily = response['daily']
#
# highest_temp = daily['temperature_2m_max']
# lowest_temp = daily['temperature_2m_min']
# avg_temp = daily['temperature_2m_mean']
#
# highest = 0
# lowest = float('inf')
# avg = 0
#
#
# for temp in range(len(highest_temp)):
#     if highest_temp[temp] > highest:
#         highest = highest_temp[temp]
#     if lowest_temp[temp] < lowest:
#         lowest = lowest_temp[temp]
#     avg = sum(avg_temp) / len(avg_temp)




# print(f'Highest temperature: {highest}\nLowest temperature: {lowest}\nAverage temperature: {round(avg, 2)}')


params = {'latitude': 19.2, 'longitude': 109.7, 'hourly': 'temperature_2m'}

response = requests.get(URL, params=params).json()


hourly = response['hourly']
#
# print(hourly)




time = hourly['time']
temperature = hourly['temperature_2m']

highest = 0
highest_hour = 0

lowest = float('inf')
lowest_hour = 0

avg = 0
avg_hour = 0

lowest_diff = float('inf')
closest_to_avg = float('inf')


avg = sum(temperature) / len(temperature)

for i in range(len(time)):
    if temperature[i] > highest:
        highest = temperature[i]
        highest_hour = time[i]
    if temperature[i] < lowest:
        lowest = temperature[i]
        lowest_hour = time[i]

    diff = abs(temperature[i] - avg)

    if diff < lowest_diff:
        lowest_diff = diff
        closest_to_avg = temperature[i]
        avg_hour = time[i]


print(f"Highest temp: {highest} at {highest_hour}, lowest temp: {lowest} at {lowest_hour}, average temp: {round(avg, 2)} at {avg_hour}")



# print(avg)
# print(temperature)










