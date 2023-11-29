class Human:
    default_name = 'Mike'
    default_age = 20

    def __init__(self, money, house):
        self.name = self.default_name
        self.age = self.default_age

        self._money = money
        self._house = house

    def info(self):
        print(f'name - {self.name},\nage - {self.age},\n'
              f'house - {self._house},\nmoney - {self._money}', end='\n\n')

    def default_info(self):
        print(self.default_name, self.default_age)

    def _make_deal(self, house, price):
        self._money -= price
        self._house.append(house)

    def earn_money(self, temp):
        self._money += temp

    def buy_house(self, house, discount):
        price_with_disc = house.final_price(discount)
        if price_with_disc <= self._money:
            self._make_deal(house, price_with_disc)
        else:
            print('У вас недостаточно денег\n')


class House():
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (100 - discount) / 100


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)



hum = Human(6000, [])
hum.default_info()
hum.info()
small_house = SmallHouse(60000)
hum.buy_house(small_house, 10)
hum.earn_money(500000)
hum.buy_house(small_house, 10)
hum.info()

