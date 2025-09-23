from abc import ABC, abstractmethod
class general_user(ABC):
    def __init__ (self,user_name,account_year):
        self.un = user_name
        self.ay = account_year
    def account_age(self):
        return f"No of years the account have been made: {2025 - self.ay}"
    @abstractmethod
    def get_role(self):
        pass
class Admin(general_user):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return (f"""Hey Admin
Name of the user : {self.un}
Year of Account Creation: {self.ay}
{self.account_age()}
Role of user:{self.get_role()}
-----------------------------""")

class Guest(general_user):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return (f"""Hai Admin
Name of the user : {self.un}
Year of Account Creation: {self.ay}
{self.account_age()}
Role of user:{self.get_role()}
-----------------------------""")
        
admin = Admin("Mohanlal",2008)
guest = Guest("Mammooty",1999)

print(admin)
print(guest)
    
        
    
        
        