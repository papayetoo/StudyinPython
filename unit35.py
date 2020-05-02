
class Person:
    count = 0

    def __init__(self):
        self.bag = []
        Person.count += 1

    def put_bag(self, stuff):
        self.bag.append(stuff)

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))
class Student(Person):
    def study(self):
        print('공부하기')

class Knight:
    __item_limit = 10

    def print_item_limit(self):
        print(Knight.__item_limit)

class Calc:
    @staticmethod
    def add(a,b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

james = Student()
james.put_bag('책')
james.study()

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

x = Knight()
x.print_item_limit()

Calc.add(1,2)
Calc.mul(2,2)

Person.print_count()