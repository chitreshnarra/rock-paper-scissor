num_matcher={'rock':1,'paper':2,'scissor':3}
while True:
    num1=num_matcher[input('what do u choose')]
    num2=num_matcher[input('what do u choose')]
    if num1-num2==1:
        print('1st member wins')
    elif num2-num1==1:
        print('2nd member wins')
    elif num2-num1==2:
        print('1st member wins')
    elif num1-num2==2:
        print('2nd member wins')
    inp=input('do u want to play another game?\n')
    if inp=='yes':continue
    else:break
