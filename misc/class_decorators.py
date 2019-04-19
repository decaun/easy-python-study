class Geek: 
    def __init__(self): 
         self.age = None 

    # getter method 
    def get_age(self): 
        return self.age 
      
    # setter method 
    def set_age(self, x): 
        self.age = x 
  
raj = Geek() 

print(raj.age) 
# setting the age using setter 
raj.set_age(21) 
  
# retrieving age using getter 
  
print(raj.age) 