# coding: utf-8

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words_len = []

sentence = sentence.split()

for word in sentence:
    words_len_tmp = len(word)
    if ',' in word or '.' in word:
        words_len_tmp += -1
    words_len.append(words_len_tmp)

print(words_len)