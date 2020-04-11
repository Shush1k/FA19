import classBody
class Pyramid(classBody.Body):
    def __init__(self, S_footprint, S_lateral, h):
        # S_footprint - площадь основания
        # S_lateral - площадь боковой поверхности
        self.S_footprint = S_footprint
        self.S_lateral = S_lateral
        self.h = h

        self.get_volume()
        self.get_surface()

    def get_surface(self):
        self.surface_square = self.S_footprint + 4 * self.S_lateral

    def get_volume(self):
        self.volume = (1 / 3) * self.S_footprint * self.h