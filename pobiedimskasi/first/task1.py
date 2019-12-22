# Виведення усіх слів, що містять у собі принаймні одну велику літеру

text = input('Введіть текст: ')
text = text.split(' ')
newlist = []
for i in range(len(text)):
   if text[i].lower() != text[i]:
        newlist.append(text[i])
print(str(newlist))
exit = input()
