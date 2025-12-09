# Definie dictionary
my_dictionary = {
    "name": "Fazt",
    "age": 23,
    "city": "Los Angeles"
}

print(my_dictionary["name"])

# Scroll dictionary
for clave in my_dictionary:
    print(clave)


# For example
inventary = {
    "espada": 1,
    "pocion": 5,
    "escudo": 1
}

# Add
inventary["moneda"] = 100

# Update
inventary["pocion"] = 7

for clave, valor in inventary.items():
    print(f"La clave es '{clave}' y el valor es '{valor}'")
