class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
# Cat 객체의 문자열 표현방식
    def __str__(self):
        return 'Cat(name='+self.__name+', age='+str(self.__age)+')'
    # self.__age를 외부에서 자유롭게 접근하는 것을 제한하고 음수가 되지 않도록 함
    def set_age(self, age):
        if age > 0:
            self.__age = age
    def get_age(self):
        return self.__name
nabi = Cat('나비', 3) # nabi 인스턴스 생성
print(nabi)
nabi.set_age(4) # set_age() 메소드를 통해서 age에 접근
nabi.set_age(-5) # set_age() 메소드를 통해서 age가 음수가 되지 않도록 함
print(nabi)

b = nabi.get_age()
print(b)
