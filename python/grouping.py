import random
import json

items = ["A", "B", "C", "D", "E", "F"]

# まず全体をランダムでシャッフルする
random.shuffle(items)

# 3:3で分けるか2:4で分けるかランダムで判断する
num = random.randint(2, 3)

first_half = sorted(items[:num])
second_half = sorted(items[num:])

print(json.dumps(first_half), json.dumps(second_half), sep='\n')