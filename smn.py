# 1

print("1.\n")
nums = [8, 800, 5, 5, 5, 3, 5, 3, 5]
nums = list(input("1. Здравствуйте, введите желаемые числа\n: "))
# a)
print("Результат А\n:", set(nums))
# б)
numb = list()
numa = list()
dig1 = ''
dig2 = ''
for i in range(0, len(nums)):
    co = 0
    for j in range(0, len(nums)):
        if nums[i] == nums[j] and nums[i] != dig1 and nums[i] != dig2:
            co += 1
            if co == 2:
                dig1 = nums[i]
                numb.append(nums[j])
                numa.append(nums[j])
    if co == 1:
        numb.append(nums[i])
        numa.append(nums[i])
    dig2 = nums[i - 1]
for i in range(0, len(numb)):
    co = 0
    for j in range(0, len(numa)):
        if numb[i] == numb[j]:
            co += 1
            if co == 2:
                numa[j] = ''
print("Результат Б\n:", numa)

# 2

data = input("\n2. Введите пожалуйста данные\n: ")
if data.lstrip("-").isdigit():
    data = int(data)
    if data % 1 == 0:
        data = abs(data)
    else:
        data = float(data)
        if data > 0:
            data *= -1
        else:
            data = abs(data)
else:
    if data.isupper():
        data = data.lower()
    else:
        data = data.upper()
print("Результат:", data)

# 3

blockade = (451, 36.6, 'Normal', None, False, True, 'Psycho', 43.3, 0)
leningrad = dict()
for t in range(len(blockade)):
    dig1 = blockade[t - 1]
    dig2 = blockade[t - 2]
    leningrad[type(blockade[t]), t] = blockade[t]
print(leningrad)

# 4

print("\n4.")
nums = [8, 800, 5, 5, 5, 3, 5, 3, 5]
# nums = list(input("\n4. Введите желаемые числа\n: "))
numb = list()
for i in range(0, len(nums)):
    co = 0
    for j in range(0, len(nums)):
        if nums[i] == nums[j]:
            co += 1
    if co != 2:
        numb.append(nums[i])
print("Результат\n:", numb)

# 5

print("\n5.")
nums = [8, 800, 5, 5, 5, 3, 5, 3, 5]
smun = list()
co = 1
for i in range(len(nums)):
    if nums[i] % 2 != 0:
        smun.insert(co, i)
        co += 1
print("Результат\n:", smun)

# 6

message = input("\n6. Введите желаемый текст через пробел\n: ")
co = 1
for line in message.split():
    print(co, ". ", line)
    co += 1
# 7

message = input("\n7. Введите желаемый текст\n: ")
tower = dict()
for line in list(message):
    tower[line] = tower.get(line, 0) + 1
print(str(tower))

# 8
team = {
    "Дюк": ("Дробовик", "Пистолет", "Голо-копия"),
    "Флинн": ("Пистолет", "Дробовик", "Плазмаган", "Пулемёт", "BFG9000"),
    "Калеб": ("Дробовик", "Плазмаган", "Динамит"),
    "Гордон": ("Очки", "Лом", "Пистолет"),
    "Сэм": ("Дробовик", "Пулемёт", "Плазмаган")
}
