class Person:
    def __init__(self, name, age):
        print('객체 생성중')
        self.name = name
        self.age = age

    def add(self):
        print('1년이 지나 {}살이 되었습니다.'.format(self.age+1))

    

alice = Person('ALICE', 19)
alice.add()
