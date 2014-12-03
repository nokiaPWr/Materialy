class ShopInventory():
    def __init__(self):
        self.items = {}
        self.total_price = 0
        self.shop_balance = 0

    def __str__(self):
        return 'Hello! Mamy na stanie: ' +  str(self.items)

    def add_item(self, item, quantity, price):
        self.items[item] = {'quantity':quantity, 'price':price}
        self.total_price += price * quantity


    def sell_item(self, name):
        self.total_price -= self.items[name]['price']
        self.items[name]['quantity'] -= 1
        self.shop_balance += self.items[name]['price']

    def balance(self):
        print(self.shop_balance)

si = ShopInventory()
si.add_item('A', 2, 3)
si.add_item('B', 0, 0)
print si
