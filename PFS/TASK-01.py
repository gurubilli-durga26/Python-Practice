'''
#***STUDENT MARKS MANAGER***

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



#***NUMBER List Analyser***
numbers = [20, 10, 30, 20, 40, 20]
print("Original list:", numbers)
# Req 1: Sort ascending
numbers.sort()
print("After sort() ascending:", numbers)
# Req 2: Reverse to descending
numbers.reverse()
print("After reverse() descending:", numbers)
# Req 3,4,5: Search
search_num = int(input("Enter a number to search: "))
if search_num in numbers:
    print(f"{search_num} found in list")
    print(f"Count: {numbers.count(search_num)}")
    print(f"First Index: {numbers.index(search_num)}")
else:
    print(f"{search_num} not found in list")
# Req 6: min, max, sum
print(f"Smallest: {min(numbers)}, Largest: {max(numbers)}, Total: {sum(numbers)}")



#***even and odd number***
numbers = [10, 15, 20, 25, 30, 35]
even = []
odd = []
# Req 2,3,4: loop + condition + append
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even list:", even)
print("Odd list:", odd)
# Req 5: slicing
print("First three of original:", numbers[:3])
print("Last three of original:", numbers[-3:])
# Req 6 & 7: copy and clear
backup = numbers.copy()
print("Backup list:", backup)

numbers.clear()
print("After clear() original:", numbers)
print("Backup remains:", backup)


#***Unique Name Manager***
names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
print("Original list:", names)
# Req 1: Convert to set
unique_names = set(names)
print("After set() conversion:", unique_names)
# Req 2: Add Meera
unique_names.add("Meera")
print("After add('Meera'):", unique_names)
# Req 3: Add Arun and Priya using update()
unique_names.update(["Arun", "Priya"])
print("After update(['Arun','Priya']):", unique_names)
# Req 4: Check John exists then remove
if "John" in unique_names:
    unique_names.remove("John")
    print("John removed")
# Req 5: discard David without error
unique_names.discard("David")
print("After discard('David'):", unique_names)
# Req 6: loop to display
print("Final unique names:")
for name in unique_names:
    print(name)






