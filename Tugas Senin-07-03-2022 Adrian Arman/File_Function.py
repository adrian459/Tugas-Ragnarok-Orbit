#Encapsulation
class Email:
    __password = None
    def __init__(self, username, password):
        self.username = username
        self.__password = password #private access modifier
    def __getPassword(self): #Accessing private modifier using __function (private function)
        print(self.__password)
    def getPassword(self):#Accesing private function using public function
        self.__getPassword()
        
class Savings:
    _Amount = None
    def __init__(self, amount):
        self._amount = amount #protected access modifier 
class Check_Balance(Savings):
    def __init__(self, amount):
        Savings.__init__(self, amount)
    def DisplayDetail(self):
        print("Balance : ", self._amount, "$")

#Inheritance 
class Mercedez_Benz:
    def __init__(self, Brand):
        self.Brand = Brand
    def display_info(self):
        print("Vehichle Brand : ", self.Brand)
        print("Brand Type     : ", "-")
        print("Max Speed      : ", "0", " km/h")
        print("Length         : ", "0", "Meter")
        print("Width          : ", "0", "Meter")

class Mercy_CLA(Mercedez_Benz):
    def __init__(self, Brand, type, max_speed, length, width):
        super().__init__(Brand)
        self.type = type
        self.max_speed = max_speed
        self.length = length
        self.width = width
    def display_info(self):
        print("Vehichle Brand : ", self.Brand)
        print("Brand Type     : ", self.type)
        print("Max Speed      : ", self.max_speed, " km/h")
        print("Length         : ", self.length, "Meter")
        print("Width          : ", self.width, "Meter")
        
class Mercy_CLS(Mercedez_Benz):
    def __init__(self, Brand, type, max_speed, length, width):
        super().__init__(Brand)
        self.type = type
        self.max_speed = max_speed
        self.length = length
        self.width = width
    def display_info(self):
        print("Vehichle Brand : ", self.Brand)
        print("Brand Type     : ", self.type)
        print("Max Speed      : ", self.max_speed, " km/h")
        print("Length         : ", self.length, "Meter")
        print("Width          : ", self.width, "Meter")
        
#Abstraction
from abc import abstractmethod, ABC

class Programmer_calculator(ABC):
    @abstractmethod
    def calculate(self):
        pass
class Dec_Bin(Programmer_calculator):
    def __init__(self, number):
        self.number = number
    def calculate(self):
        print("Dec : ", self.number, "-->", " Bin : ", bin(self.number).replace("0b", ""))
class Dec_Oct(Programmer_calculator):
    def __init__(self, number):
        self.number = number
    def calculate(self):
        print("Dec : ", self.number, "-->", " Oct : ", oct(self.number).replace("0o", ""))
class Dec_Hex(Programmer_calculator):
    def __init__(self, number):
        self.number = number
    def calculate(self):
        print("Dec : ", self.number, "-->", " Hex : ", hex(self.number))
     

 #Polymorphysm
class Aircraft:
    def __init__(self):
        self.AircraftName = "Default"
        self.TailHeight = 0
        self.WingSpan = 0
        self.MaxWeight = 0
    def display_info(self):
        print("Aircraft Name : ", self.AircraftName)
        print("Tail Height   : ", self.TailHeight, "Meter")
        print("Wing Span     : ", self.WingSpan, "Meter")
        print("Max Weight    : ", self.MaxWeight, "Ton")

class A1(Aircraft):
    def __init__(self):
        Aircraft.__init__(self)
        self.AircraftName = "Boeing-737"
        self.TailHeight = 200
        self.WingSpan = 100
        self.MaxWeight = 20
    def display_info(self):
        print("Aircraft Name : ", self.AircraftName)
        print("Tail Height   : ", self.TailHeight, "Meter")
        print("Wing Span     : ", self.WingSpan, "Meter")
        print("Max Weight    : ", self.MaxWeight, "Ton")

class A2(Aircraft):
    def __init__(self):
        Aircraft.__init__(self)
        self.AircraftName = "Sukhoi SU-57"
        self.TailHeight = 20
        self.WingSpan = 100
        self.MaxWeight = 20
    def display_info(self):
        print("Aircraft Name : ", self.AircraftName)
        print("Tail Height   : ", self.TailHeight, "Meter")
        print("Wing Span     : ", self.WingSpan, "Meter")
        print("Max Weight    : ", self.MaxWeight, "Ton")

