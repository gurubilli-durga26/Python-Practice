'''
#STUDENT MARKS MANAGER

#make sure to create marks list
marks=[]
for mark in range(3):
    mark=int(input('enter the marks:'))
    marks.append(mark)
#print(marks)
#insert 90 marks into the list
marks.insert(0,90)
#print(marks)
#add multiple marks
marks.extend([75,85])
#print(marks)
#check for 75 marks in given marks list
if 75 in marks:
    marks.remove(75)
#remove the the final mark using pop
removed_mark=marks.pop()
print(f'removed mark is {removed_mark}')
#final list of marks
print(f'final student marks list is {marks}')
print(f'count of student marks is {len(marks)}')
'''
#Number list analyser
numbers=[20,10,30,20,40,20]
numbers.sort()
numbers.reverse()
print(numbers)
