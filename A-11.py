# A-11: BMIアプリ
# 身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリを実装してください
#
# 参考となるWebアプリ
# https://keisan.casio.jp/exec/system/1161228732​
#
# 小数点第2位まで表示すること
#
# # 例
# $ python bmi.py
# Height(m)? > 170
# Weight(kg)? > 60
# Your BMI is 20.76

# BMI＝ 体重kg ÷ (身長m)2

input_height = input("身長を入力してください(m): ")
input_weight = input("体重を入力してください(kg): ")

height = float(input_height)
weight = int(input_weight)

bmi = weight / height ** 2
print(round(bmi, 2))
