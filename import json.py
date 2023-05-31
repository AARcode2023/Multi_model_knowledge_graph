import json

# Load entities from the JSON file in UTF-8 encoding
with open('entities.json', 'r', encoding='utf-8') as file:
    entities = json.load(file)

# Separate entities into countries, cities, and celebrities
countries = []
cities = []
celebrities = []

for entity in entities:
    if entity['type'] == 'country':
        countries.append(entity)
    elif entity['type'] == 'capital':
        cities.append(entity)
    elif entity['type'] == 'celebrity':
        celebrities.append(entity)

# Save countries to a separate JSON file in UTF-8 encoding
with open('countries.json', 'w', encoding='utf-8') as file:
    json.dump(countries, file, ensure_ascii=False, indent=4)

# Save cities to a separate JSON file in UTF-8 encoding
with open('capitals.json', 'w', encoding='utf-8') as file:
    json.dump(cities, file, ensure_ascii=False, indent=4)

# Save celebrities to a separate JSON file in UTF-8 encoding
with open('celebrities.json', 'w', encoding='utf-8') as file:
    json.dump(celebrities, file, ensure_ascii=False, indent=4)
