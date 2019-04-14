month_range=[31,28,31,30,31,30,31,31,30,31,30,31]
caly=[[[0 for k in range(7)] for j in range(6)] for i in range(12)]
print("X年のカレンダー\n",end="")
print("X=",end="")
X=int(input())
Y=1
Z=1
W=0
for i in range(0,Y-1,1):
    W=W+month_range[i]

W=W+(X-1)*365+Z+(X-1)//4-(X-1)//100+(X-1)//400
if (((X%4==0) and (X%100!=0)) or (X%400==0)):
    month_range[1]=29
    if Y>2:
        W=W+1
C=W%7
for i in range(0,12,1):
    l=1
    for j in range(0,6,1):
        for k in range(0,7,1):
            if (j==0 and k>=C):
                caly[i][j][k]=l
                l=l+1            
            elif (j>0 and l<=month_range[i]):
                caly[i][j][k]=l

                if l==month_range[i]:
                    C=(k+1)%7
                l=l+1
print(caly)
for i in range(0,12,1):
    print(str(i+1)+"月\n",end="")
    print("日　月　火　水　木　金　土\n",end="")
    for j in range(0,6,1):
        for k in range(0,7,1):
            if caly[i][j][k]==0:
                print("   ",end="")
            elif caly[i][j][k]>=1 and caly[i][j][k]<=9:
                print(" "+str(caly[i][j][k])+" ",end="")
            else:
                print(str(caly[i][j][k])+" ",end="")
        print("\n")
    print("\n")
