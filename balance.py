#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#自定义模块balance
d=float(input('Please input your initial balance:\n'))
p=float(input('Please input the interest rate(a number):\n'))
year=1
while year<=5:
    d=float(d+d*p/100)
    print('Your new balance after year:',year,'is',d)
    year=year+1
print('Your final balance is',d)

