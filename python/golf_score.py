# 1行目: 規定打数 (X)
par_line = input().split(",")
# 2行目: プレイヤー打数 (Y)
player_line = input().split(",")

par_scores = [int(i) for i in par_line]
player_scores = [int(i) for i in player_line]
scores = []

# 各ホールのスコアを判定（18ホール）
for i in range(18):
    diff = player_scores[i] - par_scores[i]
    # 規定打数との差に応じてスコア名を判定
    if diff == -4:
        scores.append("コンドル")
    # ホールインワン: 1打で入れた場合（ただし、規定打数5で1打の場合はコンドル）
    elif player_scores[i] == 1:
        scores.append("ホールインワン")
    # アルバトロス: 規定打数-3打（規定打数5で2打の場合のみ）
    elif diff == -3 and par_scores[i] == 5:
        scores.append("アルバトロス")
    elif diff == -2:
        scores.append("イーグル")
    elif diff == -1:
        scores.append("バーディ")
    elif diff == 0:
        scores.append("パー")
    elif diff == 1:
        scores.append("ボギー")
    elif diff > 1:
        scores.append(f"{diff}ボギー")
result = ",".join(scores)
print(result)
