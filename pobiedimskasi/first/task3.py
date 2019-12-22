# Програма рахує кількість парних і непарних елементів у списку довільної довжини

length = int(input('Введіть кількість елементів списку: '))
newlist = []
sum1 = 0
sum2 = 0
for i in range(length):
    newlist.append(input('Введіть ' + str(i+1) + ' елемент списку: '))
    newlist[i] = int(newlist[i])
    if newlist[i]%2 == 0:
        sum1 =+ newlist[i]
    else:
        sum2 += newlist[i]
print('Сумма парних: '+str(sum1))
print('Сумма непарних: '+str(sum2))
exit = input()

