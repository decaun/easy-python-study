from abc import ABCMeta, abstractmethod,ABC

class abstract(metaclass=ABCMeta):

    @abstractmethod
    def method_name(self):
        pass

class abstract_i(ABC):
    
    @abstractmethod
    def method_name(self):
        pass

if __name__=="__main__":
    print("main")
    x=abstract()
    print(x)
    #y=Test2()
    #print(y)