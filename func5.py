def palin(str1):
    i=0
    j=0
    flag=0
    rev = str1[::-1]    
    for i in str1:
        if(i==rev[j]):
            flag=0
        else:
            flag=1
            break
        j+=1

    if(flag==0):
        return "String is Palindrome"           
    else:
        return "String is not Palindrome"     

str1 = input("Enter String: ")
print(palin(str1))