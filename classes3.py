class Class1(object):
    def __init__(self):
        pass


class Class2(Class1):
    def __init__(self):
        super(Class2, self).__init__()
        super(self.__class__, self).__init__()


c = Class2()

