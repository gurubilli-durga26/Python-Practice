'''
Scenario to understand(*args and **kwargs)
Modules-->some interesting cases -->Projects(Virtual Assistant,Email Automation)
00p-->Github(branch)

#Employee Details
def employees(*names,**settings):
    """Employee Details along with their settings"""
    print("Employees Names")
    for employee in names:
        print('-------------')
        print('-',employee)
    for key,value in settings.items():
        print("key is",key)
        print("value is",value)
employees("Rahul","Durga","Meghana",department="operations",experience_letters=True,salary=True)

def customer(*products,**category):
    """customer products details along with their category"""
    print("product name")
    for product in products:
        print(product)
    for key,value in category.items():
        print(f'{key} is {value}')
customer('laptop',model='i5',color='silver',ram=520,product='power bank')


Module-->Module is simple python block of code(reusable,organized code)
import keyword
#employee details,performance metrics(employee.py)
-->employees function
-->performance function
-->increment/leadership/learning function


'''
def employees(*names,**settings):
    """Employee Details along with their settings"""
    print("Employees Names")
    for employee in names:
        print('-------------')
        print('-',employee)
    for key,value in settings.items():
        print("key is",key)
        print("value is",value)
#employees("Rahul","Durga","Meghana",department="operations",experience_letters=True,salary=True)
#if __name__=="__main__":
details={'organization':'codegnan','year':2018,'branches':['vijayawada','hyderabad','vizag']}
print(__name__)#Dunder methods-->Magic methods


