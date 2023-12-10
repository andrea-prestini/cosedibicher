class Stock:  # Parent
    category = "Groceries"

    def __init__(self, stock_code, description, buy_price, mark_up):
        self.code = stock_code
        self.desc = description
        self.buy = buy_price
        self.margin = mark_up

    def sell_price(self):
        print("Retail price = $", round(self.buy * ((1+(self.margin/100))), 2))

    def sale(self, discount):
        print("The discounted price of {} is $".format(self.desc),
              round(self.buy * self.margin * (1-discount), 2))


class Canned(Stock):  # Child
    category = "Cans"

    def __init__(self, stock_code, description, buy_price, mark_up, volume, manuf):
        super().__init__(stock_code, description, buy_price, mark_up)
        self.volume = volume
        self.manuf = manuf

    def label(self):
        print(self.desc, "\nVolume: ", self.volume)
        self.sell_price()


C298 = Canned("C298", "Chicken Soup", 1500, 10, "400 mls", "Campbells")
C300 = Canned("C300", "Chicken Soup", 1000, 20, "400 mls", "Campbells")
C400 = Canned("C400", "Chicken Soup", 100, 50, "400 mls", "Campbells")

print("C298")
C298.label()
print()
print("C300")
C300.label()
print()
print("C400")
C400.label()