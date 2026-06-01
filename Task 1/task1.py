'''import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,25,30,40]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()


import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [75, 85, 90, 65]

plt.bar(students, marks)
plt.title("Student Marks")
plt.show()


import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,5,4,5]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()

import matplotlib.pyplot as plt

data = [12,15,18,20,20,21,22,25,28]

plt.hist(data, bins=5)
plt.title("Histogram")
plt.show()
'''
import matplotlib.pyplot as plt

labels = ["Python", "Java", "C++"]
sizes = [50, 30, 20]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Programming Language Usage")
plt.show()



