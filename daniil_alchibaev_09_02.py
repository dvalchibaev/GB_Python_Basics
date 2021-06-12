class Road:
    CM_TO_M = 0.01
    KG_TO_T = 0.001

    def __init__(self, length: float = 0, width: float = 0):
        self.__length = length
        self.__width = width

    def calculate_mass(self, density_kg=1, height_in_cm=1) -> float:
        volume = self.__length * self.__width * height_in_cm
        density_tn = self.KG_TO_T * density_kg
        return density_tn * volume


if __name__ == '__main__':
    spb_2_msk_road = Road(7000, 4)
    print(f'Road weights {spb_2_msk_road.calculate_mass(25, 5)} T')
