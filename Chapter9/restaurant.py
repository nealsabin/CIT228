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