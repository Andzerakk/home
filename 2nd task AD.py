n1 = input("Please enter first number")
n2 = input("Please enter second number")
if n2.isdigit() and n1.isdigit():
    n1_1 = int(n1)
    n2_2 = int(n2)
    if n1_1 > 0:
        if n2_2 > 0:
            print(n1_1 + n2_2, "\n", n1_1 - n2_2, "\n", n1_1 / n2_2,"\n", n1_1 ** n2_2)
        else:
            print('enter valid values')
    else:
        print('enter valid values')
else:
    print('enter valid values')