#object oriented api

import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('emp.csv')
# # print(df)

# three = fig,axs = plt.subplots(1,3, figsize=(8,5))
# # print(three)

# sort_age = df.sort_values('Age')
# # print(sort_age)

# # line plot
# axs[0].plot(sort_age['Age'],df['Salary'], color='red', marker='*',linewidth='2', markersize='2')
# axs[0].grid()
# axs[0].set_title("Line plot")
# axs[0].set_xlabel('Age')
# axs[0].set_ylabel('Salary')

# #hist
# axs[1].hist(df['Salary'], bins=5, color='skyblue')
# axs[1].set_title('Histogram')
# axs[1].set_xlabel("Salary")
# axs[1].set_ylabel("Freequency")

# plt.show()
# plt.savefig("Multiple_plots.png")

data2 = {
    'year': [2020,2021,2022,2023],
    'sales':[100,150,200,250],
    'profit':[20,30,40,50],
    'expense':[80,120,160,200]
}

df2 = pd.DataFrame(data2)
# print(df2)

plt.plot(df2['year'],df2['sales'],label='Sales')
plt.plot(df2['year'],df2['profit'],label='Profit')
plt.plot(df2['year'],df2['expense'],label='Expense')

plt.title('Financial Analysis')
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.show()

#3D plot
df = pd.read_csv('emp.csv')


ax = plt.axes(projection = '3d')

ax.scatter(df['Age'],df['Salary'],df['Experience'])
ax.set_xlabel('age')
ax.set_ylabel('salary')
ax.set_zlabel('experience')
plt.show()