#matplotlib w3 theory understanding

import matplotlib

print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.subplot(1,2,1)

plt.plot(xpoints,ypoints, marker='o', ms=20, mfc='red', mec='b' , linestyle='dotted', color='green')
# plt.show()

# Line chart

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.title('Sports watch data')
plt.xlabel('avg pulse')
plt.ylabel('calories')

plt.grid()
plt.show()

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y)
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y, color='green')
plt.show()

x = np.random.normal(180,10,250)
plt.hist(x)
plt.show()


y = np.array([35,25,25, 15])
mylabels = ['A','B','C','D']
explodes = [0.2,0,0,0]
plt.pie(y, labels=mylabels, explode=explodes)
plt.legend(title = "Fruits 4 types")
plt.show()