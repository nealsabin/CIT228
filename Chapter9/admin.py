from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self,first_name,last_name,age,home_city,home_state,privileges):
        super().__init__(first_name,last_name,age,home_city,home_state)
        self.privileges = Privileges()