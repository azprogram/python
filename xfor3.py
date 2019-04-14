#ニュートン法　2の平方根の近似
#decimalモジュール
#https://docs.python.org/ja/3/library/decimal.html
import decimal

print("2の平方根の近似計算")
print("何回？：")
n=int(input())
a=2
#有効数字を拡張
decimal.getcontext().prec = 1000
for i in range(1,n+1):
    a=decimal.Decimal(a)/2+1/decimal.Decimal(a)
    print(str(i)+"回目："+str(a)) 
