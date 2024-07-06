

t=(10,20,30,40,50,60)

print(t[0:3])  #1.Basic Slicing

print(t[3:])   #2. slicing with omitted start or stop

print(t[-3:])   #3.Slicing usng negative indices


t2=(1,2,3,4,5,6,7,8,9)


print(t2[::2])   #4. using step parameter

print(t2[::-1])   #5. reverse using negative step

print(t2[1:7:2])   #6. combining start,stop and step


#7.practice problem 

x=(2,6,3,7,5,4,7,6,8,7)

print(x[0:5])  #the 1st five elements

print(x[-5:])   #the last five elements

print(x[::3])    #every third element

print(x[1:-1])    #all except the 1st and last elements

y=tuple(reversed(x))   #the tuple reversed
print(y)