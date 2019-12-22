# Введення користувачем списку довільної довжини, виведення на екран кількості порожніх елементів списку

length = int(input('Введіть кількість елементів списку: '))
newlist = []
count = 0
for i in range(length):
    newlist.append(input('Введіть ' + str(i+1) + ' елемент списку: ').split(' '))
    if not newlist[i]:
        count =+ 1
print('Кількість порожніх списків дорівнює: '+str(count))
exit = input()


