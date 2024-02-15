# LISTE - ALGO : VALEUR LA PLUS PETITE

# V1 :
nom_chauffeur = ["Jean", "Cécile", "Pierre", "Alice", "Paul", "Marine", "Jack"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

distance_min = distance_chauffeur_km[0]
index_min = 0

for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min :
        distance_min = distance    
        index_min = i

print(f"Distance minimale : {distance_min} km")
print(f"Index de la distance minimale : {index_min}")
print(f"Nom du chauffeur : {nom_chauffeur[index_min]}")

distance_chauffeur_km.sort()
print(distance_chauffeur_km[0])
print(distance_chauffeur_km)


# V2 :
nom_et_distance = [("Jean", 1.5), ("Cécile", 2.2), ("Pierre", 0.4)]

nom_et_distance_min = nom_et_distance[0]

for nom_et_distance in nom_et_distance :
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print(f"Le chauffeur {nom_et_distance_min[0]} est le plus proche, il se situe à {nom_et_distance_min[1]} km.")

