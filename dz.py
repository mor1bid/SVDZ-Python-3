# 2. Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

mylist = input("2. Здравствуйте. Введите желаемый текст/число\n: ")
warehouse = list(mylist)
market = list()
ware = ''
list(set(warehouse))
for i in range(0, len(warehouse)):
    n = 0
    for j in range(0, len(warehouse)):
        if warehouse[i] == warehouse[j] and warehouse[j] != ware:
            n += 1
            if n > 1 and warehouse[i] != '':
                market.insert(j, warehouse[i])
                ware = warehouse[i]

if len(market) == 0:
    market.insert(0, 'empty')
# else:
#     i = len(market) - 1
#     while 1 <= len(market):
#         n = 0
#         for j in range(0, len(market)):
#             if market[len(market)] == market[j]:
#                 n += 1
#                 if n > 1:
#                     market.pop(j)
#                     print("Лист повторяющихся элементов\n: ", market)

print("Лист повторяющихся элементов\n: ", market)