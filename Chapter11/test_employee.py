import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        first='Bobby'
        last='Len'
        salary=100000
        default_raise=5000
        self.employee=Employee(first,last,salary,default_raise)

    def test_give_default_raise(self):
        money=105000
        self.employee.give_raise(money)
        self.assertEqual(self.employee.salary,105000)

    #not sure how to go about this
    def give_custom_raise(self):
        money=110000
        default_raise=10000
        self.employee.give_raise(money)
        self.assertEqual(self.employee.salary,110000)


if __name__ == '__main__':
    unittest.main()
