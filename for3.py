#ニュートン法　2の平方根の近似
print("数列のn番目までの和")
print("nは？：")
n=int(input())
a=2
#a1=2
#an=a(n-1)/2+1/a(n-1)
for i in range(1,n+1):
    print(str(i)+"番目までの和："+str(a))
    a=a/2+1/a
    
#6番目で小数第15位まで記述（カンスト）