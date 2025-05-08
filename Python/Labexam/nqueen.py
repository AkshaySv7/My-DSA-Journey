def algonqueen(k,n,x):
    for i in range(1,n+1):
        if place(k,i,x):
            x[k]=i
            if k==n:
                printNqueen(n,x)
            else:
                algonqueen(k+1,n,x)

def place(k,i,x):
    for j in range(1,k):
        if x[j]==i:
            return False
        elif abs(x[j]-i)==abs(j-k):
            return False
    return True

def printNqueen(n,x):
    print("sol:")
    for i in range(1,n+1):
        for j in range(1,n+1):
            if x[i]==j:
                print("q",end="")
            else:
                print("_",end="")
        print()
    print()   
           
def main():
    n=int(input("enter the number of rows"))
    if n<=0:
        print("invlaid input")
    else:
        x=[0]*(n+1)
        algonqueen(1,n,x)

if __name__=="__main__":
    main()



