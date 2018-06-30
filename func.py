# Function


def sayHello(name = 'Sam'):
    print('Hello', name)

sayHello()
sayHello('John')

def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1,2)
print(numSum)

def addOneToNum(num):
    num = num + 1
    print('Value inside function: ', num)
    return

num = 5
addOneToNum(num)
# print(addOneToNum())

def addOneToList(myList):
    myList.append(4)
    print('fjdlsajfsd :', myList)
    return

myList = [1, 2, 3]
addOneToList(myList)
print('fjdlsajfsdfdsfasdfasd :', myList)















