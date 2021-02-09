from restaurant import Restaurant
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["vanilla","chocolate","strawberry"]

    def display_flavors(self):
        print(f"{self.restaurant_name} serves: ")
        for flavor in self.flavors:
            print(flavor)