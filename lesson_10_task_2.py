from abc import ABC, abstractmethod


class Clothes(ABC):
    total_fabric = 0

    def __init__(self, name):
        self.name = name
        self.fabric = 0

    @abstractmethod
    def counting_fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, size, name):
        super().__init__(name)
        self.size = size
        Clothes.total_fabric += self.counting_fabric

    @property
    def counting_fabric(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height, name):
        super().__init__(name)
        self.height = height
        Clothes.total_fabric += self.counting_fabric

    @property
    def counting_fabric(self):
        return self.height * 2 + 0.3


coat_1 = Coat(10, 'row')
suit_1 = Suit(170, 'gucci')
suit_2 = Suit(150, 'zara')
print(f'всего ткани нужно: {Clothes.total_fabric:0.2f}')
