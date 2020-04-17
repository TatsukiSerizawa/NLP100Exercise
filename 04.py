# coding: utf-8

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num_first = (1, 5, 6, 7, 8, 9, 15, 16, 19)
results = {}

words = sentence.split()

for (num, word) in enumerate(words, 1):  # enumerateでnumは1からスタート
    if num in num_first:
        results[word[0:1]] = num  # もしnum_first内と一致すればresultに1文字目だけ格納してnumを与える
    else:
        results[word[0:2]] = num

print(results)