import requests
from pprint import pprint

# PokéAPI — Pokémon Information
#
# API pattern
#
# URL = https://pokeapi.co/api/v2/pokemon/NAME
#
# Example:

# name = input('Enter Pokemon: ')

# URL = f'https://pokeapi.co/api/v2/pokemon/{name}'
# Question
#
# Ask:
#
# Enter Pokemon:
#
# Print:
#
# Name
# Height
# Weight
# Base Experience

# response = requests.get(URL1).json()
# print(response.keys())

# print(f"Name: {response['name']}, Height: {response['height']}, Weight: {response['weight']}, Base Experience: {response['base_experience']}")


# For a Pokémon entered by the user, print:
#
# Types:
# electric
#
# Abilities:
# static
# lightning-rod
# for entry in response['abilities']:
#     print((entry['ability']['name']))
#
#
# print(response['types'][0]['type']['name'])


# Question
#
# Print all Pokémon stats:
#
# hp
# attack
# defense
# special-attack
# special-defense
# speed
#
# Then find the strongest stat.



# base_stat = 0
# highest_stat = ''
#
# for entry in response['stats']:
#     x = entry['base_stat']
#     if x > base_stat:
#         base_stat = x
#         highest_stat = entry['stat']['name']
#
# print(f"{base_stat}, {highest_stat}")


"""Start Here!!"""


# Question
#
# Ask:
#
# Pokemon 1:
# Pokemon 2:
#
# Compare their attack stats.
#
# Example:
#
# Pikachu Attack: 55
# Charizard Attack: 84
#
# Charizard has higher attack.



# p1 = input('Enter Pokemon 1: ')
# p2 = input('Enter Pokemon 2: ')
# print()
#
# URL1 = f'https://pokeapi.co/api/v2/pokemon/{p1}'
# URL2 = f'https://pokeapi.co/api/v2/pokemon/{p2}'
#
# response1 = requests.get(URL1).json()
# response2 = requests.get(URL2).json()
# # print(response1.keys())
#
# p1_attack = 0
# p2_attack = 0
#
# for entry in response1['stats']:
#     if entry['stat']['name'] == 'attack':
#         p1_attack = entry['base_stat']
#
# # print(p1_attack)
#
# for entry in response2['stats']:
#     if entry['stat']['name'] == 'attack':
#         p2_attack = entry['base_stat']
#
# # print(p2_attack)
#
# print(f'{p1.title()} Attack: {p1_attack}\n{p2.title()} Attack: {p2_attack}')
# print()
#
# if p1_attack > p2_attack:
#     print(f'{p1.title()} has higher attack')
# else:
#     print(f'{p2.title()} has higher attack')
#
# print()



#########




# API URL
#
# URL = 'https://dog.ceo/api/breeds/list/all'

# Question
#
# Find:
#
# Total number of breeds
# Breeds having sub-breeds
# Breed with most sub-breeds

# response = requests.get(URL).json()
# # print(response)
#
#
#
# total_breeds = 0
# breeds_subs = {}
#
# highest_breed = ''
# most_subs = 0
#
# breed_dict = response['message']
#
# for breed in breed_dict:
#     # print(breed)
#     total_breeds += 1
#     subs = breed_dict[breed]
#
#     if subs != []:
#         breeds_subs[breed] = len(subs)
#
#     if len(subs) > most_subs:
#         most_subs = len(subs)
#         highest_breed = breed
#
#
#
#
# print(f'Total breeds: {total_breeds}')
# print()
# pprint(f'Breeds with sub-breeds: {breeds_subs}')
# print()
# print(f'Breed: {highest_breed}, number of sub-breeds: {most_subs}')






# Question
#
# Ask:
#
# Enter breed:
#
# Check whether that breed exists.
#
# If it does, print its sub-breeds.
#
# Otherwise:
#
# Breed not found


# entry = input('Enter breed: ').lower()
#
# # print(response['message'])
#
# for breed in response['message']:
#     if entry == breed:
#         print(response['message'][breed])
#         break
# else:
#     print('Breed not found')






