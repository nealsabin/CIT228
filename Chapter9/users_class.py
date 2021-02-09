#Hands On 1
#Exercise 9-3

print("------Exercise 9-3-----\n")

class User:
    def __init__(self,first_name,last_name,age,home_city,home_state):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.home_city = home_city
        self.home_state = home_state
        self.login_attempts = 0

    def describe_user(self):
        print(f"Name: {self.first_name} | Last Name: {self.last_name} | Age: {self.age} | Home City: {self.home_city} | Home State: {self.home_state}")
        

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}")

    # def set_login_attempts(self, attempts):
    #     self.login_attempts = attempts
    
    def increment_login_attempts(self, attempts):
        self.login_attempts = attempts + 1
        print(f"{self.first_name} {self.last_name} has tried to logon {self.login_attempts} times.")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Number of attempts has been set to: {self.login_attempts}.")
    

user = User("Joe","Smoe","44","Traverse City","Michigan")
user2 = User("Willam","Foe","66","Albany","New York")
user3 = User("Peter","Parker","16","New York","New York")

user.greet_user()
user.describe_user()
print("\n")
user2.greet_user()
user2.describe_user()
print("\n")
user3.greet_user()
user3.describe_user()
print("\n")
user.increment_login_attempts(0)
user.increment_login_attempts(1)
user.increment_login_attempts(2)
user.reset_login_attempts()
