"""name = ["sahal","shabeeb","anas","ajnas","rashid","minhaj"]
place = ["kuttiady","malappuram","farooq","kottakkal","calicut","calicut"]
age = [21,23,20,24,23,22]"""

"""keys = ['person1', 'person2', 'person3']
ages = [25, 30, 35]
cities = ['New York', 'Los Angeles', 'Chicago']"""

# Combine into dictionary
"""dictionary = {name: {'age': age, 'place': place} for key, age, place in zip(name, age, place)}
print(dictionary)"""

keys = ['sahal', 'shabeeb', 'anas']
ages = [21, 22, 20]
cities = ['kuttiady', 'malappuram', 'farooq']

# Combine into dictionary
dictionary = {key: {'age': age, 'city': city} for key, age, city in zip(keys, ages, cities)}
print(dictionary)
