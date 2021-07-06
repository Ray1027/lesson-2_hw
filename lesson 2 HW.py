x=input('數學期末考成績?')
x=int(x)
y=input('英文期末考成績?')
y=int(y)

if x>=90<=100 and y>=90<=100:
    print('恭喜獲得獎品!')
elif x<=60>=0 and y>=90<=100:
    print('下次要再加油!')
elif x>=90<=100 and y<=60>=0:
    print('下次要再加油!')
elif x<=60>=0 and y<=60>=0:
    print('你要被處罰了!')
else:
    print('一樣要加油喔!')