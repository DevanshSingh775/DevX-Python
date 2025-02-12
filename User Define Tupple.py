list=[]
tuples=int(input("Enter the number of tuples you want to add:"))
for i in range(tuples):
    tuple_values=input("Enter the values for tuple:")
    tuple_values=tuple(tuple_values)
    list.append(tuple_values)
print(list)
