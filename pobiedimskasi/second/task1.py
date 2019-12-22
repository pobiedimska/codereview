# Вхідні дані:  -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
# Результат: список слів (у нижньому регістрі), що містить кожне друге слово та кількість його повторів 
# Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

# Виклик функції: find_most_frequent('Hello, Hello, my dear Mom! I want play and play and football')
# Повертає: [ [Hello,2] , [dear,1] , [I,1] , [play,2] ,[ football,1] ]
# Вхідні дані:  -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
# Результат: список слів (у нижньому регістрі), що містить кожне друге слово та кількість його повторів 
# Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

# Виклик функції: find_most_frequent('Hello, Hello, my dear Mom! I want play and play and football')
# Повертає: [ [Hello,2] , [dear,1] , [I,1] , [play,2] ,[ football,1] ]


def count_iterations(text):
    text_list = []
    new_text = []
    for word in text:
        count = 0
        for comparison_word in text:
            if word == comparison_word:
                count += 1
        text_list.append([word, count])

    for word in text_list:
        if not new_text.contains(word):
            new_text.append(word)
    return new_text

def make_lower(text):
    for number in range(len(text)):
        text[number] = text[number].lower()
    return text

def delete_punctuation(text, punct_list):
    for punct in punct_list:
        text.replace(punct, "")
    return text

punctuation = [" ", ",", ".", ":", ";", "!", "?", "-"]
#text = input("")
text = 'Hello, Hello, my dear Mom! I want play and play and football'
text = delete_punctuation(text, punctuation)
text = text.split(" ")

text = make_lower(text)
text = count_iterations(text)

print(text[::2])




print(text)
