"""str1 = "hello"
print(str1[::-1])"""


"""print(input("Enter your str ")[1:-1])"""

'''a = input("Enter your str ")
mid = a[1:-1]
print(a[-1] + mid + a[0])'''

'''a = "HeLLo My NamE is Jack"
b = a.casefold()
c = a.capitalize()
print(c[:-4] + a[-4:].capitalize()  )'''

'''ch = "who lives in the pineapple under the sea"
print("".join(ch.split(" ")))'''

""""str1 = "HelloWorlD"

print(str1.replace("W", " W").casefold().capitalize())"""

'''s1 = "amazing"
print(s1.replace('a', '').replace('i', ''))'''

import string

a = input('enter your password')
if len(a) < 4 or len(a) > 16:
 print('no')
else:
 for el in a:
     if el in string.digits or el in string.punctuation:
         break

