class Privileges:
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def display_privileges(self):
        print("Admin has the following privileges: ")
        for privilege in self.privileges:
            print(privilege)  