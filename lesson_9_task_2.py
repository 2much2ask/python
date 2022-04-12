class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def counting_asphalt(self, thickness, weight_asphalt_1cm):
        weight_asphalt_total = self._length * self._width * weight_asphalt_1cm * thickness
        return weight_asphalt_total


a = Road(20, 5000)
print(a.counting_asphalt(thickness=5, weight_asphalt_1cm=25))
