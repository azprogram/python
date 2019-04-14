#コンソールでそのままできる
print("繰り返し計算器")
print("数字（スペース）演算子（スペース）数字の形式で入力してください")
keisan=input()
s=keisan.split()
s[0]=int(s[0])
s[2]=int(s[2])
if s[1]=="+":
    result=s[0]+s[2]
    print(result)
elif s[1]=="-":
    result=s[0]-s[2]
    print(result)
elif s[1]=="*":
    result=s[0]*s[2]
    print(result)
elif s[1]=="/":
    result=s[0]/s[2]
    print(result)
else:
    print("入力形式が違います")

#while文
print("続けますか？[y/n]")
answer=input()
while answer=="y":
    print("演算子（スペース）数字の形式で入力してください")
    keisan=input()
    t=keisan.split()
    t[1]=int(t[1])
    if t[0]=="+":
        result=result+t[1]
        print(result)
    if t[0]=="-":
        result=result-t[1]
        print(result)
    if t[0]=="*":
        result=result*t[1]
        print(result)
    if t[0]=="/":
        result=result/t[1]
        print(result)
    print("続けますか？[y/n]")
    answer=input()

else:
    print("最終計算結果："+str(result))
    print("お疲れさまでした！")
    