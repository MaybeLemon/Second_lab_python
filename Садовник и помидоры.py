from random import randint


class Tomato:

    def __init__(self, index):
        self.states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный']
        self._index = index
        self._state = self.states[index]

    def grow(self):
        if self._index != 3:

            self._index += 1
            self._state = self.states[self._index]


    def is_ripe(self):
        if self._index == 3:
            return True
        return False


class TomatoBush:
    def __init__(self, kolvo):
        self.kolvo = kolvo
        self.tomatoes = [Tomato(randint(0, 3)) for i in range(self.kolvo)]

    def grow_all(self):
        for i in range(len(self.tomatoes)):
            self.tomatoes[i].grow()

    def all_are_ripe(self):
        for i in range(self.kolvo):
            if not self.tomatoes[i].is_ripe():
                return False
        return True

    def give_away_all(self):
        self.tomatoes = []


def knowledge_base():
    print("У вас есть помидоры.\nВы должны за ними ухаживать, чтобы они выросли."
          "\nКогда они вырастут, можете собирать урожай\n")


class Gardener():
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            return True
        else:
            print("Плоды ещё не созрели")
            return False


knowledge_base()
toma = TomatoBush(1)
gard = Gardener('Tayler', toma)
gard.work()
while not gard.harvest():
    gard.work()

print('Урожай собран')
