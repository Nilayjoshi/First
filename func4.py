def func1(*args):
        print(li)

def func2(*args):
        sum = 0
        for i in range(0,3):
            sum = sum + args[i]
        print("Total Marks:",sum)

li = ["Nilay","Amit","Abhishek","Darshan","Mohit"]
func1(li)

s1 = int(input("1st Subject Marks:"))
s2 = int(input("2nd Subject Marks:"))
s3 = int(input("3rd Subject Marks:"))
func2(s1,s2,s3)
