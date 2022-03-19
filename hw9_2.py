class Road:
    def __init__(self, length: int, width: int):

        self._lenght = length
        self._width = width

    def calculate(self, height: int = 5, mass_m_2: int = 25) -> int:

        mass = height * mass_m_2 * self._lenght * self._width // 1000
        '''делю на 1000, тк значение нужно вывести в тоннах'''
        return mass  


if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')