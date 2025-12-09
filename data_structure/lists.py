# Define list
list = ["full", "stack", "web"]
print(list)

# Access a specific element
first_element = list[0]
print(first_element)

# Access the last element
last_element = list[-1]
print(last_element)

# Modify list
list[2] = "ai"
print(list)

# Add an element to the end
list.append("fazt")
print(list)

# Remove element 
list.remove("fazt")
print(list)

# Sroll list
for list in list:
    print(list)

# Practical exercise
heroes = ["Spider-Man", "Iron man", "Thor", "Wolverine"]
heroes[1] = "Capitán América"
heroes.append("Hulk")
print(heroes)