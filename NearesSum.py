import sys
def closest_substring(intList,n):
    outlist=[]
    for i in range(0,len(intList)):
        sum=0
        count=0
        j=i
        print "Start",i
        for j in range(i,len(intList)):
            print j
            sum=sum+intList[j]
            if sum>=n:
                print("Here")
                if j!=0:
                    if abs(sum-n)>=abs(sum-n-intList[j]):
                        temp=[i,j-1]
                        outlist.append([temp,abs(sum-n-intList[j])])
                        break
                    else:
                        temp = [i, j]
                        outlist.append([temp,abs( sum - n)])
                        break
                else:
                    temp=[i,j]
                    outlist.append([temp,abs(sum-n)])
                    break
            if j==len(intList)-1:
                temp = [i, j]
                outlist.append([temp, abs(sum - n)])
                break
    print outlist
    min=sys.maxint
    ans=[]
    for i in range(0,len(outlist)):
        if outlist[i][1]==min:
            ans.append(outlist[i])
        if outlist[i][1]<min:
            min=outlist[i][1]
            ans=[]
            ans.append(outlist[i])
    print ans[0][0]
    tup=(ans[0][0][0],ans[0][0][1])
    print tup
    return tup
closest_substring([1,2,4,5,7,8],10)
