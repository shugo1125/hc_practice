import random
import json

items = ["A", "B", "C", "D", "E", "F"]

# まず全体をランダムでシャッフルする
random.shuffle(items)

# 3:3で分けるか2:4で分けるかランダムで判断する
if random.randint(0, 1) == 0:
    # 3:3に分割してさらにそれぞれのリストをアルファベット順にソートする
    first_half = sorted(items[:3])
    second_half = sorted(items[3:])
    print(json.dumps(first_half))
    print(json.dumps(second_half))
else:
    # 2:4に分割してさらにそれぞれのリストをアルファベット順にソートする
    first_two = sorted(items[:2])
    first_four = sorted(items[2:])
    print(json.dumps(first_two))
    print(json.dumps(first_four))