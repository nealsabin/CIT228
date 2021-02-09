#Hands on 1
#Exercise 9-1

print("-----Exercise 9-1-----\n")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"\t{self.restaurant_name} is currently open!")

business = Restaurant("Taco Bell","Mexican")

business.describe_restaurant()
business.open_restaurant()

#Exercise 9-2
print("\n----------------------------------------------------------")
print("-----Exercise 9-2-----\n")

class Restaurant2:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"\t{self.restaurant_name} is currently open!")

business = Restaurant("Taco Bell","Mexican")
business2 = Restaurant("Dominos","Italian")
business3 = Restaurant("Culvers","American")

business.describe_restaurant()
business2.describe_restaurant()
business3.describe_restaurant()


