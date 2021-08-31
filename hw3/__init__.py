"""c = input('enter ur string')
q = 0
for el in c:
    if el in ['a', 'u', 'i', 'o', 'y', 'e']:
        q = q + 1

print(q)"""
'''
i = input('enter string')
i1 = i.swapcase()
print(i, i1)'''

"""

my_string = input('here ')
if my_string[4] == "s":
    token = my_string.split('https://')[1].split(".com")[0]
if my_string[4] == ":":
    token = my_string.split('http://')[1].split(".com")[0]
print(token)

"""
'''
import string
input = input("here ")
q = ""
for el in input:
    if el in string.ascii_uppercase:
        q = q + el
print(q)
    '''
'''
import string

i = input('enter ur password')
q = 0
w = 0
e = 0
for el in i:
    if el in string.ascii_lowercase:
        q = q + 1
    if el in string.ascii_uppercase:
        w = w + 1
    if el.isdigit():
        e = e + 1
if q > 0 and e > 0 and w > 0 and 7 < len(i) < 17:
    print('password valid')
else:
    print("password non valid")
'''