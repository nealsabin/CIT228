#Hands on 2
#Exercise 9-2
print("\n----------------------------------------------------------")
print("-----Exercise 9-4-----\n")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")
        print(f"Occupent Limit: {self.number_served}")

    def set_number_served(self,served):
        self.number_served = served

    def increment_served(self, served):
        self.number_served += served

business = Restaurant("Taco Bell","Mexican")
business.describe_restaurant()
print("\n")
business.number_served = 55
business.describe_restaurant()
print("\n")
business.set_number_served(155)
business.describe_restaurant()
print("\n")
business.increment_served(100)
business.describe_restaurant()