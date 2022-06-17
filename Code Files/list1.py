import pandas as pd
lst = []

emp1 = { 'Employee': ['Nilay','Mehul','Devam','Merchant','Ledger'],
        'Age' : [19,30,24,26,24],
        'Position' : ['Employee','HR','IT Developer','Employee','IT Developer'],
        'Salary' :[10000,6000,15000,4000,400]        
        }
df2 = pd.DataFrame(emp1)
 

for i in range(1,5):
    ele = input()
    lst.append(ele)
print(lst)

df2.loc[len(df2)] = lst
print(df2)