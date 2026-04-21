#matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# x = [1,2,3,4]
# y = [5,6,7,8]

# plt.plot(x,y)
# plt.grid()
# plt.show()

data = {
    "Salary" : [2000,1000,3000,1500,800,500,5000,5600,2500,1100]
}

df = pd.DataFrame(data)
# read = pd.read_csv('data.csv')

# print(df)

#line chart

# plt.plot(df['Salary'],color="blue",marker = 'o',linestyle =":")
# plt.grid()
# plt.show()

#histogram

# plt.hist(df["Salary"], bins=4, color="green")
# plt.grid()
# plt.show()

#boxplot

# plt.boxplot(df['Salary'])
# plt.show()

df['Dept'] = ['Manager','IT','Sales','Developer','IT','Sales','Manager','Manager','Developer','IT']

# print(df)

count = df['Dept'].value_counts()
# print(count)

#pie

# plt.pie(count, labels=count.index, autopct="%1.1f", explode= [0, 0.1, 2])
# plt.show()

#bar

# plt.bar(count.index , count)
# plt.show()

df['Age'] = [21,23,20,21,24,25,29,22,24,21]

# print(df.head())

#scatter

# plt.scatter(df['Age'],df['Salary'],color='orange')
# plt.show()

sorted_age = df.sort_values('Age')

# plt.plot(sorted_age['Age'],df['Salary'],color='red',marker='*',linewidth="2")
# plt.grid()
# plt.show()

# plt.bar(sorted_age['Age'],df['Salary'],color = 'green')
# plt.show()

it_salary = df[df['Dept']=='IT']["Salary"]
# print(it_salary)

salary_by_dept = df.groupby('Dept')['Salary'].sum()
# print(salary_by_dept)

# plt.pie(salary_by_dept, labels=salary_by_dept.index , autopct="%1.2f", shadow= True )
# plt.axis("equal")
# plt.show()
# plt.savefig('pie_salary_by_dept.png')

df['Experience'] = [1,2,3,1,2,5,8,2,5,6]
# print(df)

# plt.scatter(sorted_age['Age'], df['Salary'], s= df["Experience"] * 20, color = "skyblue", edgecolors="black")
# plt.title("Age VS Salary")
# plt.show()


# color mapping
# color_map = {
#     "IT": "yellow",
#     "Manager": "green",
#     "Developer": "blue",
#     "Sales": "skyblue"
# }

# loop through each department
# for dept, df_dept in df.groupby('Dept'):
#     color = color_map.get(dept, "gray")  # default color
    
#     plt.scatter(
#         df_dept['Age'],
#         df_dept['Salary'],
#         c=color,
#         label=dept   # 👈 important for legend
#     )

# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.title("Employee Data")

# plt.legend()  # now it will work
# plt.show()


df.to_csv('emp.csv', index=False)
