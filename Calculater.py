print('welcome to calculate program, please input your option to do: ')
n1=" "
n2=" "
while n1 !=0 and n2!=0:
    x=input(print('for summtion (+),for sibtract(-),for power (*), for divetion(/)'))
    while x!='+' and x!='-' and x!='^' and x!='/':
         print('please return your option')
         x=input(print('for summtion (+),for sibtract(-),for power (*), for divetion(/)'))
    n1=input(print('please input the first number :'))
    n1=float(n1)
    n2=input(print('please input the second number :'))
    n2=float(n2)
    if x=="+":
     print(n1+n2)
    elif x=="-":
     print(n1-n2)
    elif x=="*":
     print(n1*n2)
    elif x=="/":
     print(n1/n2)
    