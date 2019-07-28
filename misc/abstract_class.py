from abc import ABCMeta, abstractmethod, ABC


class abstract(metaclass=ABCMeta):

    @abstractmethod
    def method_name(self):
        pass


class abstract_2(ABC):

    @abstractmethod
    def method_name(self):
        pass


class inherit_abstract(abstract):

    def method_name(self):
        pass


class inherit_abstract_fail(abstract):

    def method_incorrect_name(self):
        pass


if __name__ == "__main__":
    print("main")
    x = inherit_abstract()
    y = inherit_abstract_fail()
    print(x)
    # y=Test2()
    # print(y)
