'''
Inheritance-->It is one of the key properties of OOP.
we can acquire properties(features)from one class to another class.
Types
-----
1.Single Inheritence  --> Finger Print --> One child class inheriting properties from one parent
2.Multiple Inheritence --> Parents ,kids--> One child class take properties from parents
3.Multilevel Inheritence --> level by level -->Family Tree
4.Hierarchical inheritence --> Multiple child classes inherit from singlle parent
5.Hybrid Inheritence --> Combination of diff types of inheritence

1.Single Inheritence :

class Baseclass: #Parent class
        statements....
        ............
class Derivedclass(Baseclass): #Childclass
        statement(S).....
        ......
        ...

#Updating user names in a profile page
class Users:
    """Users class with basic details"""
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def fullname(self):
        return f'{self.fname+self.lname}'
#u1=Users('Durga','Gurubilli')
#print(u1.fullname())
#Now we want to extend by updating user name
class Update_Users(Users):
    #pass
    def Update(self):
        return f'{self.fname.title()+" "+self.lname.title().strip()}'#strip will remove leading spaces 
u1=Update_Users('durga','  gurubilli')
print(dir(u1))
print(u1.fullname())
print(u1.Update())

#Usage of class attribute and classmethod in Inheritance
#class attributes-->They can be accessed directly with class name
#class method-->@classmethod

#banking scenario-->RBI Bank(Base class)-->SBI,HDFC
class RBI:
    """Base class with amount"""
    cash=10000000#class attribute
    @classmethod
    def rbi_cash(cls):
        return f'Available cash with RBI is {RBI.cash}'
#b1=RBI()
#print(b1.cash)
#print(b1.rbi_cash())
#print(RBI.cash)#we can also access directly using classname.
#print(RBI.rbi_cash())
class SBI(RBI):
    pass

#b1=SBI()
#print(b1.rbi_cash())
class HDFC(RBI):
    cash=5000000#class attribute
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total Accessible cash is {cls.cash+cls.cash}')
b1=HDFC()
print(b1.cash)#In this case as cash attribute is same
print(b1.rbi_cash())
b1.hdfc_cash()

#the same cash we will access with classnames
class HDFC(RBI):
    cash=5000000#class attribute
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total Accessible cash is {cls.cash+RBI.cash}')
b1=HDFC()
print(b1.cash)
b1.hdfc_cash()
print(b1.rbi_cash())

#takeaway->if same classes is having same names as class attributes
#to access then we will directly use class names as RBI.cash,HDFC.cash


#In the same way what if we have different class attributes
class RBI:
    """Base class with amount"""
    cash=10000000#class attribute
    @classmethod
    def rbi_cash(cls):
        return f'Available cash with RBI is {cls.cash}'
class HDFC(RBI):
    amount=5000000#class attribute
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.amount}')
        print(f'Total Accessible cash is {cls.amount+cls.cash}')
b1=HDFC()
print(b1.cash)
print(b1.amount)
b1.hdfc_cash()
print(b1.rbi_cash())
'''
#Single Inheritance usage-->Base class and dervied class with constructors
#kid,father-->property scenario

class Father:
    """Father class with base property amount"""
    def __init__(self):
        self.fproperty=2500000
    def father_property(self):
        print(f'Father Property is {self.fproperty}')
#u1=Father()
#u1.father_property()
'''
class Kid(Father):
    pass
u1=Kid()
print(u1.property)
u1.father_property()

#In above case its as it is not change in method and attribute usage
class Kid(Father):
    """kid started earning"""
    def __init__(self):
        self.property=500000
    def kid_property(self):
        print(f'Kid property is {self.property}')
        print(f'kid and father combined property is {self.property+self.property}')
u1=Kid()
u1.father_property()
u1.kid_property()
#In this case -->constructor overriding as parent and child classes is having
#constructor child class constructor will override parent class constructor

we have the usage of super()-->derived classes
-->Super class constructor-->super().__init__()
-->Super class constructor with args-->super().__init__(args)
-->Superclass method (Method overriding)-->super().method()
'''
class Kid(Father):
    """kid started earning"""
    def __init__(self):
        super().__init__()
        self.kproperty=500000
        #super().__init__()#calling superclass constructor
    def kid_property(self):
        print(f'Kid property is {self.kproperty}')
        print(f'kid and father combined property is {self.kproperty+self.fproperty}')
u1=Kid()
u1.kid_property()
u1.father_property()







