# coding: utf-8

def ngram(targets, n):  #targetsの文章からn-gram作成
    results = []
    for i in range(len(targets)-n+1):
        results.append(targets[i:i+n])
    return results


sentence = "I am an NLPer"
words = sentence.split()

# 単語bi-gram
print(ngram(words, 2))

# 文字bi-gram
moji = ''
for i in words:
    moji += i
print(ngram(moji, 2))