import os
import quicklayer

file = quicklayer.get(__file__,"test.txt")

print("FILE: " + file)

with open(file) as f:
    r = f.read()
    print(r)


'''
# ファイルの情報
print(__file__)

# 区切り文字の取得
print(os.sep)

# inの使い方
print("a" in "a") # True
print("aa" in "a") # False
print("a" in "aa") # True
'''
