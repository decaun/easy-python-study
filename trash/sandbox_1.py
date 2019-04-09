class house():
    door=1
    wall=4
    floor=1

    def __init__(self):
        self.cimney=1
        self.window=4
        self.toilet=1
        self.increase_cimney()
        
    @classmethod
    def increase_wall(cls):
        cls.wall+=1
        print("There are {} walls now".format(cls.wall))
        
    @property
    def be_wall(self):
        print("i dont do anything X {}".format(self.wall))
        return self.wall
    
    @staticmethod
    def flush(self):
        print("flushed {} times".format(self.toilet))

    def increase_cimney(self):
        self.cimney+=1

if __name__=="__main__":
    ben=house()
    sam=house()
    print(ben.be_wall)
    house.flush(ben)
    house.increase_wall()
    print("ben has {} walls also ".format(ben.be_wall))
    sam.cimney=1
    print(ben.cimney)
    print(sam.cimney)