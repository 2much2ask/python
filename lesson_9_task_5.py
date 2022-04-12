class Stationery:
    def __init__(self, title='Bic'):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'рисуем ручкой {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'рисуем карандашом {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'рисуем маркером {self.title}')


felttippen = Pencil('Centropen')
a = Stationery()
Stationery.draw(a)
