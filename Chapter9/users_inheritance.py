#Hands On 1
#Exercise 9-7 & 9-8

print("------Exercise 9-7 & 9-8-----\n")

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

user1 = User("Admin","Admin","Admin","Admin","Admin")

class Admin(User):
    def __init__(self,first_name,last_name,age,home_city,home_state,privileges):
        super().__init__(first_name,last_name,age,home_city,home_state)
        self.privileges = Privileges()
    
    # def display_privileges(self):
    #     print(f"{self.first_name} privileges: ")
    #     for privilege in self.privileges:
    #         print(privilege)

class Privileges:
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def display_privileges(self):
        print("Admin has the following privileges: ")
        for privilege in self.privileges:
            print(privilege)    

user1 = Privileges()
user1.display_privileges()

