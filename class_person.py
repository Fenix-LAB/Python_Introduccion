
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Se a construido el objeto")

    def myName(self):
        print("Hola, minombre es: ", self.name)

    def myAge(self):
        print("Mi edad es: ", self.age)



print("se va a crear un objeto")
P1 = person("Chris", 22)
P1.myName()
P1.myAge()

class student(person):
    def __init__(self, name, age, lvl):
        super().__init__(name, age)
        self.lvl = lvl

    def myLvl(self):
        print("Mi nivel escolar es: ", self.lvl)


S1 = student("Chris", 22, "Universidad")
S1.myAge()
S1.myLvl()