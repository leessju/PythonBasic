# create class & object
class Person(object):
    __name = ''
    __email = ''

    def __init__(self, name = 'hi', email = 'abc@abc.com'):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def toString(self):
        return '{} can be  contacted a {}'.format(self.__name, self.__email)

# james = Person()
# james.set_name('nicejames')
# james.set_email('nicejaems@gmail.com')
#
# print(james.get_name())
# print(james.get_email())
#
# someone = Person('1111', '2222')
# print(someone.get_name())
# print(someone.get_email())
#
# noone = Person()
# print(noone.get_name())
# print(noone.get_email())
# print(noone.toString())



class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def toString(self):
        return '{} can be  contacted a {} and at {}'.format(self.__name, self.__email, self.__balance)



john = Customer('John Doe', 'jdoe@gmail.com', 100)
print(john.toString())










