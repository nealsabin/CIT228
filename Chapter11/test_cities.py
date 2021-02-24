import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_country("Traverse City","United States","300,000,000")
        self.assertEqual(formatted_city,'Traverse City, United States - Population: 300,000,000')

if __name__ == '__main__':
    unittest.main()