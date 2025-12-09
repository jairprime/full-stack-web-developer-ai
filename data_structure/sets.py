# Define sets
duplicate_number = [1, 2, 3, 3, 3, 4, 5]
numbers_without_duplicates = list(set(duplicate_number))
print(numbers_without_duplicates)

# Sets challenge
asistentes = ["Ana","Luis", "Juan", "Sofia"]
invidatos = ["Ana", "Luis", "Carlos", "Juan", "Sofia"]

# Convert lists to sets
set_asistentes = set(asistentes)
set_invidatos = set(invidatos)

print("Asistentes a la fiesta:", set_asistentes)

# Invited people who did not attend
no_asistieron = set_invidatos.difference(set_asistentes)
print("Invitados que no asistieron:", no_asistieron)

# Full list of people involved
todas_las_personas = set_asistentes.union(set_invidatos)
print("Todas las personas involucradas:", todas_las_personas)