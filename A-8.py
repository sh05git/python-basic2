# A-8: リストを要素に持つリスト
# users_info を使って次のような出力をしてください

"Name: Kazuma, Age: 35"
"Name: Tom, Age: 57"
"Name: Bob, Age: 77"

users_info = [["Kazuma", 35], ["Tom", 57], ["Bob", 77]]
for user in users_info:
    print(f"Name: {user[0]}, Age: {user[1]}")
