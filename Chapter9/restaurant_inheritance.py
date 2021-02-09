#Hands on 2
#Exercise 9-2
print("\n----------------------------------------------------------")
print("-----Exercise 9-6-----\n")

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

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["vanilla","chocolate","strawberry"]

    def display_flavors(self):
        print(f"{self.restaurant_name} serves: ")
        for flavor in self.flavors:
            print(flavor)

stand=IceCreamStand("DQ","Ice Cream")
stand.display_flavors()