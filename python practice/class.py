class Wizard:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def shout(self):
        print("I am a Magician")

    @classmethod
    def add(cls,num1,num2):
        return cls("Tiger",num1 + num2)

    @staticmethod
    def add2(num1,num2):
        return num1 + num2


Wizard1 = Wizard("Brian",31)
Wizard2 = Wizard.add(5,10)
print(Wizard2.age)