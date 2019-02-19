class engine():
    def __init__(self):
        self.holes=8
        self.bores=8

class v8engine(engine):
    def __init__(self):
        super().__init__()
        self.bores=7

class car(type):
    @staticmethod
    def drive(type):
        print ("Driving with {}".format(type.bores+5))
    
a=v8engine()
print(a.bores)
car.drive(a)