import pandas as pd

emp = { 'Employee': ['Nilay','Mehul','Devam','Merchant','Ledger'],
        'Age' : [19,30,24,26,24],
        'Position' : ['Employee','HR','IT Developer','Employee','IT Developer'],
        'Salary' :[10000,6000,15000,4000,400]        
        }

srn = [1,2,3,4,5]
df1 = pd.DataFrame(emp,index=srn)    
df1.to_csv('Test1.csv')
