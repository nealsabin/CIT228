#Hands on 1
#Exercise 11-1
def city_country(city,country,population=""):
    if population:
        combined = f"{city}, {country} - Population: {population}."
    else: 
        combined = f"{city}, {country}."
    return combined.title()