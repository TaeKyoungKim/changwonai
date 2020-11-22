class Cat:
    def __init__(self, name , color="흰색"):
        self.name = name
        self.color=color

    def meow(self, name="태경"):
        print('My name is {}, My Color is {}, meow~ meow~ 주인은 {}'\
            .format(self.name, self.color, name))

nabi = Cat('나비', '검은색')
nero = Cat('네로', '하얀색')
raon = Cat('라온', '점박이')
nabi.meow()
nero.meow()
raon.meow()