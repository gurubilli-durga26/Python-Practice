'''
Polymorphism --> Method Overloading,Method overriding,Operator Overiridng
poly=many
morph=forms
Method Overloading-->Default arguments,Variable length arguments,Type of arguments.


#Hotstar --> FreeUsers,Premium Users,VIP users

class Hotstar:
    """Understanding Polymorphism"""
    def watch(self):
        print("User logged in and seeing basic content")
    def watch(self,movie):
        self.movie=movie
        print(f'User Watching {self.movie}')
u1=Hotstar()
u1.watch("Leo")
#In the above scenario only the updated content is seen

#Method Overloading-->Default arguments,Variable length arguments,Type of arguments.
##Method Overloading(Compile time polymorphism)-->Default arguments

class Hotstar:
    """default args usage"""
    def watch(self,movie=None):
        self.movie=movie
        if self.movie==None:
            print(f'Welcome to Hotstar')
        elif self.movie==movie:
            print(f'User watching {self.movie}')
u1=Hotstar()
u1.watch()
u1.watch("Happy Days")

#multiple  args
class Hotstar:
    """*args args usage"""
    def watch(self,*movie):
        self.movie=movie
        if self.movie==None:
            print(f'Welcome to Hotstar')
        elif self.movie==movie:
            for i in range(len(movie)):
                print(f'User watching {self.movie[i]}')
u1=Hotstar()
u1.watch("Happy Days","leo","VARSHAM")

#scenario of adding movies to watchlist
class Hotstar:
    """*args args usage"""
    def watch(self,movie=None):
        print(f'Welcome to Hotstar')
    def add_tolist(self,*movies):
        for movie in movies:
            print(movie)
u1=Hotstar()
u1.watch()
u1.add_tolist("Happy Days","leo","VARSHAM")
           
#Method Overloading with type of arguments(isinstance())
#Hotstar-->one movie,multiple movie

class Hotstar:
    """Usage of type args"""
    def watch(self,movie=None):
        print(f'Welcome to Hotstar')
    def movie_list(self,content):
        self.content=content
        if isinstance(content,str):
            print(f'User watching {self.content}')
        elif isinstance(content,tuple):
            print(content)
            for movie in content:
                print(movie)
        elif isinstance(content,list):
            print(content)
            for movie in content:
                print(movie)
u1=Hotstar()
u1.watch()
u2=Hotstar()
u2.movie_list("vikram")
u2.movie_list(("Happy Days","leo","VARSHAM"))
u2.movie_list(["Happy Days","leo","VARSHAM"])


#Method Overriding-->Inheritance usage
#when the same method name is used in base class and also in dervied class
#super()
#free user-->[can watch free content with advertisements]
#premium user-->[can watch premium content without advertisements]
#VIP User-->[can watch premium content along with devices count,streaming]


class Hotstar:
    """Base class with welcome"""
    def watch(self):
        print(f'welcome to hotstar')
class Free_user(Hotstar):
    """Free users class with advertisements"""
    def watch(self):
        super().watch()
        print(f'Free movie with advertisements')
class Premium_users(Free_user):
    """premium content"""
    def watch(self):
        super().watch()
        print('premium content')
class VIP_user(Premium_users):
    """LIVE content"""
    def watch(self):
        super().watch()
        print('LIVE content with best streaming')
u1=VIP_user()
u1.watch()
u2=Premium_users()
u2.watch()
        

#Operating Overloading-->(Magic methods/dunder methods)__init__
a=13;b=24
print(a+b)
print(a.__add__(b))#self.value+other.value
print('codegnan'.__add__('python'))#concatenation
print([1,3,].__add__([2,34,9]))#Merging

#in above case same __add__() is performing different cases(Addition,concatenation,merging)

a=[1,2,3,4,5]
print(a.__len__())#len(a)
'''
class WatchHistory:
    """Duration of watching content"""
    def duration(self,hours):
        self.hours=hours
u1=WatchHistory()
u1.duration(25)
u2=WatchHistory()
u2.duration(35)
print(u1.hours+u2.hours)

class WatchHistory:
    """Duration of watching content"""
    def duration(self,hours):
        self.hours=hours
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
        print(f'User watching {self.hours} hours duration')
u1=WatchHistory()
u1.duration(25)
u2=WatchHistory()
u2.duration(35)
print(u1.hours+u2.hours)
print(u1+u2)#get the complete duration
u1.__str__()
u2.__str__()




















