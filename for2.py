#入力時に謎の改行が入る
print("数列のn番目までの和")
print("nは？：")
n=int(input())
a=0
#a1=0
#an=a(n-1)*n+5
for i in range(1,n+1):
    print(str(i)+"番目までの和："+str(a))
    a=a+a*i+5
