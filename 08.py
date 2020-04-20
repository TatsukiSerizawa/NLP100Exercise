# coding: utf-8

def cipher(sentence):
    new = []
    for s in sentence:
        if 97 <= ord(s) <= 122:  # 英小文字なら
            s = chr(219 - ord(s))  # (219-文字コード)に変換
        new.append(s)
    return ''.join(new)

test = 'I am an NLPer'

new = cipher(test)  # 暗号化
print(new)
old = cipher(new)  # 復号化
print(old)