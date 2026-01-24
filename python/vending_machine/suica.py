class Suica:
    def __init__(self):
        # 内部で保持する残高
        self.__deposit = 500

    def charge(self, val):
        # 100円未満のチャージを拒否するバリデーション（入力チェック）
        if val < 100:
            raise ValueError("100円未満はチャージできません")
        self.__deposit += val

    def get(self):
        return self.__deposit

    def pay(self, amount):
        # 指定された金額を残高から引き落とす
        self.__deposit -= amount
