import matplotlib.pyplot as plt
import numpy as np
# x, y = [1,2,3], [10,20,30]

# plt.plot(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title("Matplotlib")
# plt.show()



# data = {"python":45, "C":30, "C#":20, "java":40}

# labels = list(data.keys())
# values = list(data.values())

# print(labels, values)

# fig = plt.figure(figsize=(10,5))

# plt.bar(labels, values, color="red", width=0.5)
# plt.xlabel('Language')
# plt.ylabel('Popularity')
# plt.title("Matplotlib")
# plt.show()

# values = np.array([12,43,65,23,87])
# mylabels = ["Apple", "Banana", "Mango", "Orange", "Chocolate"]

# plt.pie(values, labels=mylabels)
# plt.show()


x = np.linspace(0,10,30)
y = np.sin(x)

plt.scatter(x,y)
plt.show()









