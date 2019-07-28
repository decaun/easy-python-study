from abc import ABCMeta, abstractmethod, ABC


class abstract(metaclass=ABCMeta):

    @abstractmethod
    def method(self):
        pass


class abstract_i(ABC):

    @abstractmethod
    def method(self):
        pass


if __name__ == "__main__":
    print("main")
    x = Test()
    print(x)
    # y=Test2()
    # print(y)
