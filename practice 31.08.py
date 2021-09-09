"""
from simp import y
from simple import x

print(x + y)
"""
# import f13.f13

'''
import pickle

new_file = open("students", "a")
x = {'Avramenko': 3, 'Adamovich': 5,  'Babych': 2}
with open('students', 'wb') as f:
    pickle.dump(x, f)
with open('students', 'rb') as f:
    y = pickle.load(f)
    print(y)
for a in y:
    if y[a] > 3:
        print(a)

'''
'''
import random
a = True
while a == True:
    if int(input("guess")) != random.randint(1, 5):
        print(random.randint(1, 5))
        continue
    elif int(input("guess")) == random.randint(1, 5):\
    print("you win")
    a = False
'''

'''
def print_half_piramid(x):
    q = 1
    i = x
    while i > 0:
        print("*" * q)
        q = q + 1
        i = i - 1
    return


print_half_piramid(7)
'''

'''
def fun_list(x):
    x = input("enter your set of numbers"))
    print(max(x), min(x))
    if sorted(x) == x:
        print(True)
    else:
        print(False)
    return

fun_list(1)
'''
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
'''
"""
def func(ticket, monthly):
    return print(monthly / ticket)
func(8,240)
"""
"""
def search(x, y):
    x = str(x)
    y = str(y)
    s = y.split(x)
    q = x.swapcase()
    p = y.split(q)
    print(s)
    print(p)
    print(len(s) + len(p) - 2)
    return
search("w", "elwwwwwwwcoe o te junle")
"""
'''
'''
# import random
#
# def rock_paper_scissors(x):
#     rand = random.randint(1, 3)
#     print(rand)
#     x = input("enter rock paper or scissors")
#     if x.lower() == "rock":
#         if rand == 1:
#             res = "tie"
#         elif rand == 2:
#             res =  "lose"
#         elif rand == 3:
#             res = "win"
#     elif  x.lower() == "paper":
#         if rand == 1:
#             res = "win"
#         elif rand == 2:
#             res = "tie"
#         elif rand == 3:
#             res = "lose"
#     elif  x.lower() == "scissors":
#         if rand == 1:
#             res = "lose"
#         elif rand == 2:
#             res = "win"
#         elif rand == 3:
#             res = "tie"
#     print(res)
# return
# ffff
'''


# x = 99
# def f1():
#     x = 88
#     def f2():
#         print(x)
#
#     f2()
# f1

# def maker(n):
#     def action(x):
#         return x ** n
#     return action()

# def maker(N):
#     def action(X):
#         return print(X+N)
#     return action
#
# f = maker("1")
# f("44")
# .
# x = "093"
# print(len(x))
'''
# def countrycode(X):
#     def number(N):
#         if len(N) == 10:
#             return print(X+N)
#         else:
#             return print("false")
#     return number
# countrycode("38")("0674843434")
#
# import dir11.f1
# print(dir11.f1.x)
#
# '''

# def returner(N):
#     tupl = N
#     tup = ()
#     tup = tupl[-5], tupl[-3], tupl[-1]
#     return print(tup)
# returner((1, 3, 4, 5, 6))

# def solver():
#     a = input('heh')
#     q = 1
#     for el in a:
#         if int(el) != 0:
#             q = int(el) * q
#     return print(q)
# solver()
# import string
#
# def cypher():
#     a = input("hehe")
#     b = ""
#     for el in a:
#         if el in string.ascii_uppercase:
#             b = b + el
#     return print(b)
# cypher()

# def larger(a):
#     new = []
#     last = sorted(a)[-1]
#     for el in a:
#         if int(el) < int(last):
#             new.append(int(el))
#         elif int(el) >= int(last):
#             break
#     return print(new)
#
# larger([1, 4, 3, 5, 6, 20, 1, 1])
'''
# def cleaner():
a = {"432": ["A", "A", "B", "D"],  "53": ["L", "G", "B", "C"],  "236": ["L", "A", "X", "G", "H", "X"],  "11": ["P", "R", "S", "D"],}
# # a.values()
 g = list(a.values())
# print(g)
# # print(str(g))
# print(list(dict.fromkeys(list(a.values())[1])))
# # for v in a.values():
# #     print(v)
# print(list(a.values()))
general = []
new_list
for el in list(a.values()):
    general = general + el
print(general)
generalone = (list(dict.fromkeys(general)))
 for el in g:
     for elem in el:
         if elem in generalo
'''

max_let:
