class employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def display(self):
        print(f"""name: {self.name} 
role: {self.role}""")

class trainer(employee):
    def __init__(self,name,role,specialisation):
        employee.__init__(self,name,role)
        self.specialisation = specialisation
    def display(self):
        print(f"""name: {self.name} 
role: {self.role} 
specialization: {self.specialisation}
""")

class yogainstructor(employee):
    def __init__(self,name,role,yoga_style):
        employee.__init__(self,name,role)
        self.yoga_style = yoga_style
    def display(self):
        print(f"""name: {self.name} 
role: {self.role} 
yoga style: {self.yoga_style} 
""")

class multitrainer(trainer,yogainstructor):
    def __init__(self,name,role,specialisation,yoga_style):
        trainer.__init__(self,name,role,specialisation)
        yogainstructor.__init__(self,name,role,yoga_style)
    def display(self):
        print(f"""name: {self.name} 
role: {self.role} 
specialisation:{self.specialisation} 
yoga style: {self.yoga_style}
""")


multi = multitrainer("Gautham","workout trainer","cardio","Yoga")
multi.display()

yogains = yogainstructor("Justin","yoga","Yoga")
yogains.display()

trainee = trainer("Rahul","Diet trainer","Food knowledge")
trainee.display()

employ = employee("Akash","muscle trainer")
employ.display()
