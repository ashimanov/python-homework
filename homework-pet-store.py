# creates a Pet class, __ before each class attirbute makes them private
class Pet:
    def __init__(self, name: str, species: str, age: int, sex: str):
            self.__name = str(name) # converts name input to string if it isn't a string already
            self.__species = str(species) # converts species input to string if it isn't a string already
            if not isinstance(age, int): # checks if age input is an integer
                raise TypeError(f'Your input "{age}" is invalid. Must be an integer.') # raises an error if age input isn't an integer
            else:
                self.__age = age
            self.__sex = str(sex) # converts sex input to string if it isn't a string already

    def get_info(self):
        try:
            self.info = f'Pet name: {self.__name}\nSpecies: {self.__species}\nAge: {self.__age}\nSex: {self.__sex}' # compiles a simple Pet info block (string)
            print(self.info)
        except Exception as ex:
            return f'An exception with get_info: {ex}.'

# creates a subclass Dog (Pet is the superclass)
class Dog(Pet):
    def __init__(self, name, species, age, sex, breed: str):
        super().__init__(name, species, age, sex)
        self.__breed = str(breed) # converts breed input to string if it isn't a string already

    def bark(self):
        print('Гав!')
 
# creates a subclass Cat (Pet is the superclass)
class Cat(Pet):
    def __init__(self, name, species, age, sex,color: str):
        super().__init__(name, species, age, sex)
        self.__color = str(color) # converts color input to string if it isn't a string already

    def meow(self):
        print('Мяу!')


# Fluffy is created, an instance of the Dog subclass and its methods are called
Fluffy = Dog('Fluffy', 'dog', 3, 'male', 'Husky')
Fluffy.bark()
Fluffy.get_info()

print(' ') # just a spacer to visually enhance the output

# Furball is created, an instance of the Cat subclass and its methods are called
Furball = Cat('Furball', 'cat', 2, 'male', 'grey')
Furball.meow()
Furball.get_info()

