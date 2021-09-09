# inp = input('enter values here')
# a = inp.split(" ")
# print(a)
# b = []
# for el in a:
#     b.append(int(el))
# if b == sorted(b):
#     print("True")
# # 1 2 4 6 8 10 12 14 16 17


# inp = input('enter values here')
# a = inp.split(" ")
# print(a)
# b = 1
# for el in a:
#     if int(el) > 0:
#         b = b * int(el)
# print(b)
#
#
# a = ['Red', 'Green', 'Blue', 'White', 'Black']
# b = []
# for el in a:
#     el = el[::-1]
#     print(el)
#     b.append(el)
# print(b)

# a = {'salt':2, 'meat': 25, 'apples': 6, 'banana':3, 'milk': 4.5, 'bread': 2.5}
# sort = sorted(list(a.values()))
# b = sort[-3::]
# for k, v in a.items():
#      if v in b:
#          print(k)

#
# inp = input("enter number of stars")
# base = {"Continental Hotel" : "****","Big Street Hotel" : "**", "Corner Hotel" : "**", "Trashviews Hotel" : "*", "Hazbins" : "****", "Hazbins Deluxe" : "*****"}
#
# for k, v in base.items():
#     if len(v) == int(inp):
#         print(k)