import smn
import re
import random

# 1. Решить задачи, которые не успели решить на семинаре.

# 2. Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

mylist = input("2. Здравствуйте. Введите желаемый текст/число\n: ")
warehouse = list(mylist)
market = list()
check = ''
list(set(warehouse))
for i in range(0, len(warehouse)):
    got = 0
    for j in range(0, len(warehouse)):
        if warehouse[i] == warehouse[j] and warehouse[j] != check:
            got += 1
            if got > 1 and warehouse[i] != ' ':
                market.insert(j, warehouse[i])
                check = warehouse[i]

if len(market) == 0:
    market.insert(0, 'empty')

print("Лист повторяющихся элементов\n: ", list(set(market)))

# 3. В большой текстовой строке подсчитать количество 
# встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

print("3.\n:")
text = 'Этот документ описывает соглашение о том, как писать код для языка python, включая стандартную библиотеку, входящую в состав python. PEP 8 создан на основе рекомендаций Гуидо ван Россума с добавлениями от Барри. Если где-то возникал конфликт, мы выбирали стиль Гуидо. И, конечно, этот PEP может быть неполным (фактически, он, наверное, никогда не будет закончен). Ключевая идея Гуидо такова: код читается намного больше раз, чем пишется. Собственно, рекомендации о стиле написания кода направлены на то, чтобы улучшить читаемость кода и сделать его согласованным между большим числом проектов. В идеале, весь код будет написан в едином стиле, и любой сможет легко его прочесть. Это руководство о согласованности и единстве. Согласованность с этим руководством очень важна. Согласованность внутри одного проекта еще важнее. А согласованность внутри модуля или функции — самое важное. Но важно помнить, что иногда это руководство неприменимо, и понимать, когда можно отойти от рекомендаций. Когда вы сомневаетесь, просто посмотрите на другие примеры и решите, какой выглядит лучше.'.lower()
# text = input("3. Введите желаемый текст, что хотите проверить на 10 самых частых слов\n:").lower()
contend = {}
cleant = re.findall(r"[\w']+", text)
for mine in text.split(): # чтобы были полные слова, не буквы
    count = 0
    for line in text.split():
        if mine == line:
            count += 1
    if count > 1:
        contend[mine] = count
contend = dict(reversed(sorted(contend.items(), key = lambda item: item[1])))
ranking = {}
i = 1
for j in contend.keys():
    if len(ranking) <= 10:
        ranking[str(i) + ' место'] = j + ' - ' + str(contend[j]) + ' шт.'
        i += 1
print(ranking)

# 4. Создайте словарь со списком вещей для похода в качестве ключа и их 
# массой в качестве значения. Определите какие вещи влезут в
# рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

inventory = {
    "Коврик": 0.8, "Одежда": 0.8, "Компас": 0.039, "Фонарик": 0.15, "Посуда": 2.0, "Аптечка": 1.3, "Термос": 1.0, "Обед": 1.0, "Палатка": 10, "Спальник": 2, "Фотоаппарат": 0.4
}
loot = list()
home = list()
backpack = float(input("Введите желаемый размер вместимости своего рюкзака (в литрах)\n: "))
if backpack > 120.0:
    print('Рюкзаков такой вместимости не бывает.')
else:
    scales = 0
    for item in inventory.keys():
        if scales + inventory[item] <= backpack:
            scales += inventory[item]
            loot.append(item)
        else:
            home.append(item)
if len(home) == 0:
    home.insert(0, "ничего!")
print("В ваш рюкзак мы смогли уместить\n:", loot,"\nОбщий вес составил: ", round(scales, 1), "/", backpack, " кг.\nОставшееся дома\n:", home)