rev=0
def rev_in(num):
    global rev
    if(num>0):
        rem=num%10
        rev=(rev*10)+rem
        rev_in(num//10)
    return rev
num = int(input("Enter the number: "))
rev = rev_in(num)
print("Reversed Number: ",rev)