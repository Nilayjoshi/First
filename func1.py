def prime(n):
    flag=0
    for i in range(2,n):
        if(n%i==0):
            flag=1
            break
    
    if(flag==1):
        print(n,"is not prime number")
    else:
        print(n,"is a prime number")    

n = int(input("Enter Integer:"))
prime(n)