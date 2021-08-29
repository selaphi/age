driving = input('請問你有沒有開過車?')
age = input ('請問你的年齡是?')
age = int(age)
if driving == '有':
    if age >= 18 :
        print('你通過測驗了')
    else:
        print('奇怪，你怎麼會開過車?')
elif driving == '沒有': 
    if age >= 18 :
        print('有機會可以先去考駕照')
    else:
        print('等你18歲以後，考過駕照就能開車')
else:
    print('只能回答 有/沒有')

