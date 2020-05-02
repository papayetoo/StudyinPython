class Person:
    def __init__(self, name, age, address, wallet):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요.'.format(self.__wallet))

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.greeting()

print('이름 :', maria.name)
print('나이 :', maria.age)
print('주소 :', maria.address)
maria.pay(1000)

