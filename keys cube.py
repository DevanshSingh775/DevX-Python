''' WAP to create a user define dict object further that each pair's data value is a cube of key value''' 
d1={}
x=int(input("Enter the no. of elements"))
i=1
while (i<=x):
    key1=int(input("Enter the KEY:"))
    data1=key1*key1*key1
    d1[key1]=data1
    i+=1
print(d1)
