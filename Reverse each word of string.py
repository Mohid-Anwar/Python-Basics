Sentence = "My Name is Jessa"
b = Sentence.split(" ")

new_word_list = []

for word in b:
    new_word_list += [word[::-1]]

res_str = " ".join(new_word_list)
print(res_str)
