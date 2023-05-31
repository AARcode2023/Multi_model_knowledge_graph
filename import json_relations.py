import json

# Load query results from JSON file
with open('query.json', 'r', encoding='utf-8') as query_file:
    query_results = json.load(query_file)

# Create sets to store the added names in each file
added_countries = set()
added_capitals = set()
added_celebrities = set()

# Create a list to store the country-capital relations
country_capital_relations = []

# Create a list to store the capital-celebrity relations
capital_celebrity_relations = []

# Initialize counters for unique numerical keys
capital_of_key_counter = 1
celebrity_of_key_counter = 1

# Iterate through the query results
for result in query_results:
    country = result["countryLabel"]
    capital = result["capitalLabel"]
    celebrity = result["celebrityLabel"]

    # Add country and capital relation if not already added
    country_key = f"Country/{country}"
    capital_key = f"Capital/{capital}"
    if country_key not in added_countries and capital_key not in added_capitals:
        country_capital_relation_key = f"capital_of_{capital_of_key_counter}"
        country_capital_relation = {
            "_from": country_key,
            "_to": capital_key,
            "_key": country_capital_relation_key,
        }
        country_capital_relations.append(country_capital_relation)
        added_countries.add(country_key)
        added_capitals.add(capital_key)
        capital_of_key_counter += 1

    # Add capital and celebrity relation if not already added
    celebrity_key = f"Celebrity/{celebrity}"
    if capital_key in added_capitals and celebrity_key not in added_celebrities:
        capital_celebrity_relation_key = f"celebrity_of_{celebrity_of_key_counter}"
        capital_celebrity_relation = {
            "_from": capital_key,
            "_to": celebrity_key,
            "_key": capital_celebrity_relation_key,
        }
        capital_celebrity_relations.append(capital_celebrity_relation)
        added_celebrities.add(celebrity_key)
        celebrity_of_key_counter += 1

# Save the country-capital relations JSON file with UTF-8 encoding
with open("country_capital_relations.json", "w", encoding="utf-8") as file:
    json.dump(country_capital_relations, file, ensure_ascii=False, indent=2)

# Save the capital-celebrity relations JSON file with UTF-8 encoding
with open("capital_celebrity_relations.json", "w", encoding="utf-8") as file:
    json.dump(capital_celebrity_relations, file, ensure_ascii=False, indent=2)