'''
matplotlib
----------
-->This is an python library used to create graphs and chats.
plot
----
-->the function can create a line graphs with given data.
xlabel
------
-->used to represent the x-axis values.
ylabel
------
-->used to represent the y-axis values.

title
-----
-->To define the title of the graph.'''
#line graph
import matplotlib.pyplot as plt
marks=[45,89,90]
stu_=['Teja','sony','sai']
plt.plot(stu_,marks,color='red')
plt.title('Student_marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

#bar graph
import matplotlib.pyplot as plt
marks=[45,89,90]
stu_=['Teja','sony','sai']
plt.bar(stu_,marks,color='pink')
plt.title('Student_marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

#horizontal bar graph
import matplotlib.pyplot as plt
sales=[890,150,800,1200]
cars=['BMW','NANO','SWIPF','TOYATO']
plt.barh(cars,sales,color='red')
plt.title('cars sales')
plt.ylabel('company name')
plt.xlabel('number of sales')
plt.show()

#piechart
import matplotlib.pyplot as plt
subjects=['python','java','c']
students=[45,25,35]
plt.pie(students,labels=subjects)
plt.title('total students')
plt.legend(subjects)
plt.show()

#scatter graph
import matplotlib.pyplot as plt
marks=[45,89,90]
stu_=['Teja','sony','sai']
plt.scatter(stu_,marks,color='red')
plt.title('Student_marks')
plt.xlabel('students')
plt.ylabel('marks')
plt.show()

#histrography 
import matplotlib.pyplot as plt
sales=[890,150,800,1200]
plt.hist(sales)
plt.title('sales_hist')
plt.xlabel('sales')
plt.ylabel('frequency')
plt.show()

#boxplot
import matplotlib.pyplot as plt
marks=[40,50,60,70,80,90]
plt.boxplot(marks)
plt.show()
















