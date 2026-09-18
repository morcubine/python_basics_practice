import requests
from pprint import pprint

# PokéAPI — Pokémon Information
#
# API pattern
#
# URL = https://pokeapi.co/api/v2/pokemon/NAME
#
# Example:

name = input('Enter Pokemon: ')

URL = f'https://pokeapi.co/api/v2/pokemon/{name}'
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

response = requests.get(URL).json()
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




#########




# API URL
#
# https://dog.ceo/api/breeds/list/all
# Question
#
# Find:
#
# Total number of breeds
# Breeds having sub-breeds
# Breed with most sub-breeds



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