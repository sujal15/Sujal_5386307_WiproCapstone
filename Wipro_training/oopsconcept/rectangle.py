from oopsconcept.formulamethods import FM


class rectangle(FM):
        def __init__(self, l, b):
            self.length = l
            self.breath = b


        def calculate_area(self):
            return self.length * self.breath

        def calculate_perimeter(self):
            return 2 * (self.length + self.breath)
