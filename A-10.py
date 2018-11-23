import random


# A-10: サイコロ
# 1から6の整数をランダムに出力する dice() 関数を実装してください
def dice():
    print(random.choice([1, 2, 3, 4, 5, 6]))


dice()
