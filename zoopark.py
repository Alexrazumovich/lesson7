class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        pass
    def eat(self, food):
        print(f"{self.name} eats {food}")

    def __str__(self):
        return f"Animal,{self.name},{self.age}"


class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def make_sound(self):
        print(f"{self.name} sings")
    def __str__(self):
        return f"Bird,{self.name},{self.age},{self.color}"

class Mammal(Animal):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height
    def make_sound(self):
        print(f"{self.name} growls")
    def __str__(self):
        return f"Mammal,{self.name},{self.age},{self.height}"
class Reptile(Animal):
    def __init__(self, name, age, exist_shell):
        super().__init__(name, age)
        self.exist_shell = exist_shell
    def make_sound(self):
        print(f"{self.name} is silent")
    def __str__(self):
        return f"Reptile,{self.name},{self.age},{self.exist_shell}"
    # def eat(self,food):
    #      print(f"{self.name} eats {food}")
class People():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"People,{self.name}"
class ZooKeeper(People):
    def __init__(self, name, profession):
        super().__init__(name)
        self.profession = profession
    def __str__(self):
        return f"ZooKeeper,{self.name},{self.profession}"


class Veterinarian(People):
    def __init__(self, name, specialization):
        super().__init__(name)
        self.specialization = specialization
    def heal_animal(self):
        print(f"{self.name} heals animals")
    def __str__(self):
        return f"Veterinarian,{self.name},{self.specialization}"

class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []
    def add_animal(self,animal):
        if isinstance(animal,Animal):
            self.animals.append(animal)
    def add_employee(self,employee):
        if isinstance(employee,People):
            self.employees.append(employee)
    def print_all(self):
        print("All animals:")
        for animal in self.animals:
            print(f"{animal.name} ")
        print("All employees:")
        for employee in self.employees:
            print(f"{employee.name}")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
def save_zoo(zoo):
    with open("zoo.txt", "w") as file:

        for animal in zoo.animals:
            file.write(str(animal)+"\n")

        for employee in zoo.employees:
            file.write(str(employee)+"\n")




def open_zoo(file):
     zoo=Zoo()
     with open(file, "r") as file:
         for line in file:
             type,name,age,details=line.strip().split(",")
             if type=="Bird":
                 zoo.add_animal(Bird(name,int(age),details))
             elif type=="Mammal":
                 zoo.add_animal(Mammal(name,int(age),int(details)))
             elif type=="Reptile":
                 zoo.add_animal(Reptile(name,int(age),bool(int(details))))
             elif type=="ZooKeeper":
                 zoo.add_employee(ZooKeeper(name,details))
             else:
                 zoo.add_employee(Veterinarian(name,details))
     return zoo

open("zoo.txt");
i=0;
zoo=Zoo()
for animal in zoo.animals:
    i=i+1;
for person in zoo.employees:
    i=i+1;
if i==0:
    flamingo=Bird("flamingo",1,"pink")
    elephant=Mammal("elephant",5,500)
    Turtle=Reptile("Tortilla",50,True)
    animal_list=[flamingo,elephant,Turtle]
    animal_sound(animal_list)
    man1=ZooKeeper("ivan","director")
    man2=Veterinarian("peter","surgeon")

# print("ZOO")
# print("============")
    for animal in animal_list:
        zoo.add_animal(animal)
    # print(str(animal))


    zoo.add_employee(man1)
    zoo.add_employee(man2)
    save_zoo(zoo)
