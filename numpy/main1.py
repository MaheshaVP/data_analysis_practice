#numpy topics

import numpy as np

a = np.array([1,2,3,4,5,6])

print(a.dtype)

b = np.array([[1,2,3],
             [4,5,6]])

print(b[0,1])
print(b[1,2])

print(a[1:3])

c = np.array([5,10,20,30,40,50,60])

print(c[c>25])
print(c[(c>25) & (c<45)])

result = np.where(c>15,"High","Low")
print(result)


sales = np.array([100,200,50,300,80])
high_sales = sales[sales >= 100]
print(high_sales)

data = np.array([10,-5,-8,0,20,15,-20])
clean_data = data[data>0]
print(clean_data)

marks = np.array([20,30,45,85,48,56,39,10,32])
passed = marks[marks>35]
pass_text = np.where(marks>35,"pass","fail")
print(passed)
print(pass_text)

a = np.array([1,2,3,4,5,6])
print(a+1)
print(a-2)
print(a*3)
print(a/4)
print(a**5)

print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))

b = np.array([[1,2,3,4],
              [5,6,7,8]])

print(np.sum(b, axis=0))
print(np.sum(b, axis=1))

print(a + 25)


a1 = np.array([[1,2,3,4],
              [5,6,7,8]])
b1 = np.array([10,20,30,40])
print(a1 + b1)
print(a1 + 20)

sales = np.array([100,200,300])
sales = sales * 1.2
print(sales)

print(a.reshape(2,3))

d = np.array([1.3 , 2.4, 5.8])

print(np.round(d))
print(np.floor(d))
print(np.ceil(d))
print(np.sqrt(d))

print(np.pi)

e = np.array([20,50,30,10,80,60,90])

print(np.sort(e)[::-1])
e = np.sort(e)
print(e)

print(np.where(e == 80))

import random

randii = np.random.randint(1000,10000)
print(randii)


