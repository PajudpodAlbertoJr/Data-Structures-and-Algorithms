import array

x = [1,2,3,4]
print ("The new created array is : ",end=" ")
for z in range (0, 3):
    print (x[z], end=" ")
 
print("\r")
print(x[3])
x.append(7)
print(x)
x.insert(3,9)
print(x)