class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self):
        mass_per_metre = 25
        high = 5
        mass = self._width * self._length * high * mass_per_metre / 1000
        print(f'Необходимая масса асфальта для покрытия дороги длиной: {self._length} метров\n'
              f'и шириной: {self._width} метров составляет {mass} тонн')


if __name__ == "__main__":
    road_length_with = Road(2500, 10)
    road_length_with.asphalt_mass()

# Необходимая масса асфальта для покрытия дороги длиной: 2500 метров
# и шириной: 10 метров составляет 3125.0 тонн
