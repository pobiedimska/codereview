
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