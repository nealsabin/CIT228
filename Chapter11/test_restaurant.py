import unittest
from restaurant import Restaurant

class TestRestuarant(unittest.TestCase):
    def setUp(self):
        restaurant_name = "Bobby's Bodega"
        cuisine_type = "Korean"
        number_served = 30
        self.restaurant=Restaurant(restaurant_name,cuisine_type,number_served)

    def test_number_served_int(self):
        served=30
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,30)

    def test_number_served_string(self):
        served="30"
        self.restaurant.set_number_served(served)
        self.assertEqual(self.restaurant.number_served,30)

    def test_increment_served_int(self):
        served=3
        self.restaurant.increment_served(served)
        self.assertEqual(self.restaurant.number_served,33)

    def test_increment_served_string(self):
        served="10"
        self.restaurant.increment_served(served)
        self.assertEqual(self.restaurant.number_served,40)


if __name__ == '__main__':
    unittest.main()
