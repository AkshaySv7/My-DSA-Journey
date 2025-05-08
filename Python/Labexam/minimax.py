MAX,MIN=1000,-1000
def minimax(depth,nodeindex,ismax,values,alpha,beta,maxdepth):
    if depth==maxdepth:
        return values[nodeindex]
    if ismax:
        best=MIN
        for i in range(2):
            val=minimax(depth+1,nodeindex*2+i,False,values,alpha,beta,maxdepth)
            best=max(best,val)
            alpha=max(alpha,best)
            if alpha>=beta:
                break
        return best
    else:
        best=MAX
        for i in range(2):
            val=minimax(depth+1,nodeindex*2+i,True,values,alpha,beta,maxdepth)
            best=min(best,val)
            beta=min(beta,best)
            if alpha>=beta:
                break
        return best 
maxdepth=int(input("enter the depth of the tree"))
num_leaves=2**maxdepth
values=list(map(int,input()))
optimal=minimax(0,0,True,values,MIN,MAX,maxdepth)
print(optimal)
