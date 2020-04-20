# coding: utf-8
import random

test = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

ans = []

text = test.split()

for word in text:
    if len(word) > 4:
        tmp = list(word[1:-1])
        random.shuffle(tmp)
        word = word[0] + ''.join(tmp) + word[-1]
        ans.append(word)
    else:
        ans.append(word)

print(' '.join(ans))