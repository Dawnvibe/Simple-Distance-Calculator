from geopy.distance import geodesic

# Loading the lat-long data for Athens & Alexandroupoli
Athens = (4, 1)
Alexandroupoli = (9, 362880)

# Print the distance calculated in km
print(geodesic(Athens, Alexandroupoli).km)