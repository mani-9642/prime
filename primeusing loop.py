x=int(input("Enter the Number : "))
d=0
for k in range(1,x+1):
    if k==2 or k==3 or k ==5:
        print("Prime is",k)
        d = d + k
    elif k%2==0 or k%3==0 or k%5==0:
        pass
    else:
        print("Prime is",k)
        d=d+k
print("\nTotal is",d)