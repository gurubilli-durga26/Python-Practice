'''
python project-->pop/oop-->DSA(logical based-->pattern based-->platform
POP(procedure oriented programming)-->Dividing the entire code into blocks-->procedure-->functions(def)
Functions-->A reusable block of code/a block of statements which performs a specific task.
syntax:
def <funcname>(parameters):
    """Doc String"""
    statement(s)...
    ..........      #body of func
    return value(s)...
fname(args)#func call
'''
#simple scenario to understand
def add(a,b):
    """Addition function"""
    c=a+b
    return c
print(add(4,6))#addition
c,d='codegnan','python'
print(add(c,d))#concatenation
e,f=map(str,input('enter the values').split(','))
print(add(e,f))
print(add([1,3,4],[4,6,7]))#merging
#print(add(1,2,3,4)) #positional arugments fail

#variable length arguments-->*args :We can pass any number of positional
#arguments-->where data will be stored in tuple.

def sample(*a):
    """Demo of variable length arguments"""
    print(a)
    print(type(a))#default it stores in tuple format.
sample()
sample(2,3,4,5)
sample('codegnan',[23,4],'poll',2+5j)
sample([1,2,3,4])#in tuple it will take singal object
sample(*[1,2,3,4])#keep star before list,tuple will take four objects.
#* is used to unpack the values into a collection
a,*b,c=12,'code','poll',23,4,9
print(a)
print(b)
print(c)
a,b,*c=12,'code','poll',23,4,9
print(a)
print(b)
print(c)

def add(*a):
    """Perform addition for numeric values"""
    print(a)
    result=0
    for i in a:
        #print(i)
        #if type(i) in [int,float]:
        if type(i)==int or type(i)==float:
            result=result+i
    return result
print(add(2,4,6))
print(add(2,'codegnan',3,4))


#keyword arguments-->we pass the name for the arguments
def batch(name,age,place):
#def batch(name='durga',age,place='hyd'):#error -->non default always follows
    """keyword arguments and default arguments usage"""
    print(f'{name} is in {place} and age is {age}years')
batch('codegnan',1,'vizag')
batch(place='vizag',name='codegnan',age=1)
#KEYWORD arguments only needs name matching not order.
batch(name='durga',age=21)
#default arguments can accept a value as default.

print(4,5)
print(4,5,sep=':')#here keyword arguments is sep and we are changing
#the default value for sep

#keyword variable length arguments(**kwargs)-->any number of
#keyword arguments ,data is stored in dictionary
def batch(**a):
    """Keyword variable length arguments usage"""
    print(a)
    print(type(a))
batch()
batch(name='durga',age=21,place='vizag',branch='ece')
data={'name':['durga','meghana'],'place':['vizag','kerala']}
batch(**data)
data.update({'batch':'PFS-VSP-007'})
batch(**data)

#Task:create a function with the usage of *args & **kwargs.
#using *args,kwargs
def order(*items, **customer):
    """Customer details using *args,**kwargs"""
    print("Items:")
    for item in items:#To access the items one by one 
        print(item)#For Accessing the items
    print("Customer Details:")
    for key, value in customer.items():#For accessing the customer details, .items():For accessing of both key,value
         print(f"{key} : {value}")
order("Laptop","Mouse","Keyboard",name="Meghana",city="Vizag")



        
        

















