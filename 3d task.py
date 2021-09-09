import math
ppl = input("вкажіть кількість осіб ")

pieces = input("вкажіть кількість піц ")

if ppl.isdigit() and pieces.isdigit():
    if int(ppl) > 0 and int(pieces) > 0:
        m = math.floor(int(pieces) * 8 / int(ppl))
        z = (int(pieces) * 8) - (m * int(ppl))
        od = "шматочок"
        mn = 'шматочки'
        if m > 1 and z > 1 or m = 0 and z = 0 :
            print("кожна людина отримує", m,mn , "залишок", z, mn)
        if m > 1, z = 1:
            print("кожна людина отримує", m, mn, "залишок", z, mn)
