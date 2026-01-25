from juice import Juice

PRODUCTS = {
    "pepusi": 150,
    "monster": 230,
    "irohasu": 120,
}

class VendingMachine:
    def __init__(self):
        self.__sales = 0

        # 3種類の棚（リスト）を辞書で管理。ここが自販機の「中身」
        self.__stocks = {name: [] for name in PRODUCTS}

        # 初期在庫を各棚に5本ずつ補充する
        for name in PRODUCTS:
            for _ in range(5):
                self.__stocks[name].append(Juice(name, PRODUCTS[name]))

    def get_sales(self):
        return self.__sales

    def can_buy(self, suica, name):
        # 指定された名前の棚（リスト）を取得。なければ空のリストを返す
        target_stocks = self.__stocks.get(name, [])

        # 在庫があるか確認
        if len(target_stocks) == 0:
            raise ValueError("在庫が不足しています")

        # Suica残高が足りるか確認
        # target_stocks[-1] で棚の一番手前にあるジュースの値段を見る
        if suica.get() < target_stocks[-1].get_price():
            raise ValueError("残高が不足しています")

        return True

    def buy_juice(self, suica, name):
        # 購入判定がOKなら、実際の購入処理へ進む
        if self.can_buy(suica, name):
            # 1. 棚からジュースの実体（インスタンス）を1つ取り出す
            juice_item = self.__stocks[name].pop()

            # 2. 取り出したジュースから値段を聞いて、売上を加算する
            self.__sales += juice_item.get_price()

            # 3. お客さんのSuicaから代金を引き落とす（別のクラスに命令を送る）
            suica.pay(juice_item.get_price())
        else:
            raise Exception("購入できません")

    def get_stock(self):
        # すべての棚を回って、残っているジュースの本数を合計する
        total = 0
        for shelf in self.__stocks.values():
            total += len(shelf)
        return total

    def refill(self, name, amount):
        if name not in self.__stocks:
            raise ValueError(f"{name}という商品は存在しません")

        for _ in range(amount):
            self.__stocks[name].append(Juice(name, PRODUCTS[name]))
