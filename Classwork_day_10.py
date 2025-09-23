from abc import ABC, abstractmethod
class general_user(ABC):
    def __init__ (self,name:str,joining_year:int):
        self.name = name
        self.jyear = joining_year
    
    def calculate (self):
        return f"Number of years the user has been on the platform: {2025 - self.jyear}"

class Customer(general_user):
    def __init__ (self,name:str,joining_year:int,role:str):
        super().__init__(name,joining_year)
        self.role = role
class Vendor(general_user):
    def __init__ (self,name:str,joining_year:int,role:str):
        super().__init__(name,joining_year)
        self.role = role
obj1 = Customer("Akshai", 2020, "Buyer")
obj2 = Vendor("Hassan", 2018, "Seller")

print(f"""Customer Name: {obj1.name}
Role: {obj1.role}
{obj1.calculate()}
------------------""")
print(f"""Vendor Name: {obj2.name}
Role: {obj2.role}
{obj2.calculate()}
------------------""")




        

        
    
        
    
    
    
    