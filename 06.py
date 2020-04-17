# coding: utf-8

def ngram(targets, n):  #targetsの文章からn-gram作成
    results = []
    for i in range(len(targets)-n+1):
        results.append(targets[i:i+n])
    return results

paradaice = "paraparaparadise"
paragraph = "paragraph"

X = set(ngram(paradaice, 2))
Y = set(ngram(paragraph, 2))

print('X:' + str(X))
print('Y:' + str(Y))

print('X|Y:' + str(X|Y))
print('X&Y:' + str(X&Y))
print('X-Y:' + str(X-Y))

print("'se'という文字がXに含まれる:" + str('se' in X))
print("'se'という文字がXに含まれる:" + str('se' in Y))