import sys
import datetime

# 各月の日数（0はインデックス調整用）
LAST_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 現在の年を取得
today = datetime.date.today()
year = today.year

# コマンドライン引数の処理
if len(sys.argv) == 3 and sys.argv[1] == "-m":
    # -mオプションで月を指定した場合
    try:
        month = int(sys.argv[2])
    except ValueError:
        # 数値でない場合のエラー処理
        print(f"{sys.argv[2]} is neither a month number (1..12) nor a name")
        sys.exit()
    if not (1 <= month <= 12):
        # 月の範囲外の場合のエラー処理
        print(f"{sys.argv[2]} is neither a month number (1..12) nor a name")
        sys.exit()
else:
    # 引数がない場合は今月を使用
    month = int(today.month)

# タイトルの表示（中央揃え）
title = f"{month}月 {year}"
print(title.center(20))

# 月初日の曜日を取得(0=月曜日, 6=日曜日)
first_date = datetime.date(year, month, 1)
weekday = first_date.weekday()
end_day = LAST_DAYS[month]

# カレンダーの初週の空白の計算処理（48-49行目）に使う変数
count = 0
count += weekday

# 曜日のヘッダーを表示（月曜始まり）
weekdays = ["月", "火", "水", "木", "金", "土", "日"]
for i in weekdays:
    print(f"{i:1} ", end="")
print()

# カレンダー初週の行において空白を作る処理
for i in range(count):
    print(f"{'  '}", end=" ")

# 日付を表示（週が7日になったら改行）
for i in range(1, end_day + 1):
    print(f"{i:2}", end=" ")
    count += 1
    if count == 7:
        print()
        count = 0
print()

