# 1行目: 規定打数 (X)
par_line = input().split(",")
# 2行目: プレイヤー打数 (Y)
player_line = input().split(",")

par_scores = [int(i) for i in par_line]
player_scores = [int(i) for i in player_line]
scores = []

# 辞書（マッピング）の定義
SCORE_MAPPING = {
    -3: "アルバトロス",
    -2: "イーグル",
    -1: "バーディ",
    0: "パー",
    1: "ボギー",
}

for i in range(18):
    diff = player_scores[i] - par_scores[i]
    y = player_scores[i]

    if y == 1:
        if diff == -4:
            scores.append("コンドル")
        else:
            scores.append("ホールインワン")
    elif diff >= 2:
        scores.append(f"{diff}ボギー")
    else:
        name = SCORE_MAPPING.get(diff)
        scores.append(name)

result = ",".join(scores)
print(result)
