class engine():
    def __init__(self,holes=4):
        self.holes=holes
        self.bores=4

class v8engine(engine):
    def __init__(self):
        super().__init__()
        self.bores=8
        
class v6engine(engine):
    def __init__(self):
        engine.__init__(self,holes=6)
        self.bores=6

class v2engine(engine):
    def __init__(self,soles=2):
        self.soles=soles
        super().__init__()
        self.bores=2
        



class car(type):
    @staticmethod
    def drive(type):
        print ("Driving with {}".format(type.bores+5))
        
    
a=v8engine()
b=v6engine()
c=v2engine()
print(a.bores)
print(a.holes)
car.drive(a)
print(b.holes)
print(b.bores)
print(c.soles)
print(c.bores)
print(c.holes)



class Person():     

        # __init__ is known as the constructor          
    def __init__(self, name, idnumber):    
            self.name = name 
            self.idnumber = idnumber 
    def display(self): 
            print(self.name) 
            print(self.idnumber) 
  
# child class 
class Employee( Person ):            
    def __init__(self, name, idnumber, salary, post): 
            self.salary = salary 
            self.post = post 
  
                # invoking the __init__ of the parent class  
            Person.__init__(self, name, idnumber)  
  
                  
# creation of an object variable or an instance 
a = Person('Rahul', 886012)     
  
# calling a function of the class Person using its instance 
a.display()  