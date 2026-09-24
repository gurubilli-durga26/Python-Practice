'''
OOP--> Object Oriented Programming -->Objects(class,objects)
POP-->Procedure Oriented Programming -->Functions
#Chair(Object)-->wood(materials),Design(Dimensions),Person

A class is a blueprint of a object

A object is a real world entity which contains -->Attributes(variables)
                                               -->Methods(Functions)

class keyword
Flipkart-->Products-->Laptop,Mobiles,Gadgets....
Features-->Encapsulation,Inheritance,Polymorphism.

class ClassName:
      """docstring"""
      #attributes(define the data)
      ....
      ....
      def fname(self):#behaviour
      def __init__(self):
          statement(s)...
          ...........
obj=ClassName()

#Students-->name,age
class Students:
    """Students details"""
    name="Durga"
    age=21
    place="Vizag"

    def details(self):
        print(f'{self.name} is in {self.place} and age of {self.age} years')
#Creation of Objects
st1=Students()
print(st1)
print(dir(st1))
print(st1.name)
print(st1.age,st1.place)
#print(st1.details())#it returns TypeError
#print(st1.details())#NameError as we have thrown self but no reference.
st1.details()
st2=Students()
st2.detais()

#In above case how many objects u create the result will be same.

class Students:
    """Student details for multiple students"""
    def details(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    #now to access those details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students()
st1.details("durga",21,"vizag")
print(st1.name,st1.place)
st1.display()
print(st1.__class__)
print(st1.__doc__)
print(st1.__dict__)

st2=Students()
st2.details("meghana",20,"vizag")
st2.display()

#In this case we want object to be initialized-->__init__():it automatically intialize the class
class Students:
    """Student details for multiple students"""
    def __init__(self,name,age,place):
        self.name=name#instance method
        self.age=age
        self.place=place
    #now to access those details
    def display(self):#instance variable
        print(f'Student name is {self.name}')
        print(f'Student age is {self.age} and lives in {self.place}')
st1=Students("Yamini",22,"Hyd")
st1.display()
st2=Students("Lalli",23,"bangalore")
st2.display()
print(st2.__dict__)

#Create a Cars class with attributes as brand,name,price
#Create multiple objects
class Cars:
    """Cars details multiple cars brand"""
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    def cars_details(self):
        print(f'Car brand and name is {self.brand},{self.name} and its price is {self.price}')
c1=Cars("audi","audi car",450000)
c1.cars_details()


#Encapsulation-->How the methods and attributes are binded to single
#class in similar way How we can access the data-->public,protected,private

#Public Attributes-->can be created and modified even outside the class

class Users:
    """usage of public attributes"""
    def __init__(self,username):
        self.user=username#Public attribute
    def display(self):
        print(f'Username is {self.user}')
u1=Users("Raghu")
print(u1.user)
u1.user="sam"#we can modify the public attribute
print(u1.user)
u1.display()

#Protected Attribute-->These can also be modified outside the class,its mainly useful as a hint/coding convention for other users/developers
#to create a protected attribute we use underscore-->_otp

class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp):
        self.user=username#Public attribute
        self._otp=_otp#Protected Attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1=Users("durga",3456)
u1.display()
u1._otp=5678
u1.display()

#Private Attribute-->restrict the usage and cannot be directly accessed
#We have the usage or notation as double leading underscore-->__password

class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user=username#Public attribute
        self._otp=_otp#Protected Attribute
        self.__password=__password#Private attribute
    def display(self):
        print(f'Username is {self.user}')
        print(f'OTP is {self._otp}')
u1=Users("mahesh",3456,"admin1234")
print(u1.user,u1._otp)
print(u1.__dict__)
#print(u1.__password)-->In above case password can't be accessed directly-->NameMangling
print(u1._Users__password)
'''
#Usage of getter(),setter() methods

class Users:
    """usage of public attributes"""
    def __init__(self,username,_otp,__password):
        self.user=username#Public attribute
        self._otp=_otp#Protected Attribute
        self.__password=__password#Private attribute

    #Usage of getter() or get() method for password
    def get_password(self):
        """Getter method for password"""
        #return "******"
        return self.__password
    #Usage of setter() to modify the data
    def set_password(self,new_password):
        if len(new_password)<6:
            return 'password length is not matching'
        else:
            self.__password=new_password
            return 'Updated password'
u1=Users("Admin",1234,"admin123")
print(u1.get_password())
print(u1.set_password("durga"))#not satisify the requirements less than 6
print(u1.set_password("durga12"))#case satisfied
print(u1.get_password())
print(u1.__dict__)






















































      



