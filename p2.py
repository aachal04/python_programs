a=int(input("Enter a number:"))
b = a & (a-1)
count = 1
while(b!=0):
    count +=1
    b = b & (b-1)
print("Count of 1's: ",count)

