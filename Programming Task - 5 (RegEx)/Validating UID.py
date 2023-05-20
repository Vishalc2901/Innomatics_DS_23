x=int(input())
upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
digits=['0','1','2','3','4','5','6','7','8','9']
list=[]
for i in range(x):
    num=input()
    if len(num)==10 and num.isalnum() is True:
        for i in range(10):
                list.append(num[i])
    l=0
    m=0
    for j in range(len(list)):
       for k in range(len(upper)):
         if list[j]==upper[k]:
            l+=1
    for q in range(len(list)):
       for r in range(len(digits)):
          if list[q]==digits[r]:
            m+=1
    seen=[]
    for n in range(len(list)):
        if list.count(list[n])>1:
            seen.append(list[n])
    if l>=2 and m>=3 and len(seen)==0:
        print("Valid")
    else:
        print("Invalid")
    list=[]
