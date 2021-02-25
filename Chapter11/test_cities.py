import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city = city_country("Santiago","Chile")
        self.assertEqual(formatted_city,'Santiago, Chile.')

    def test_city_countyV2(self):
        formatted_city = city_country("Santiago","Chile","300,000,000")
        self.assertEqual(formatted_city,'Santiago, Chile - Population: 300,000,000.')

if __name__ == '__main__':
    unittest.main()