class Stationary:
    def __init__(self, title="This utensil"):
        self.title = title

    def draw(self):
        print(f'{self.title} draws a bunny')


class Pencil(Stationary):
    def draw(self):
        print(f"you can erase what you've drawn by {self.title}")


class Pen(Stationary):
    def draw(self):
        print(f'with {self.title} you give an autograph')


class Handle(Stationary):
    def draw(self):
        print(f'use {self.title} to highlight important text')


if __name__ == '__main__':
    pen = Pen("pen")
    pen.draw()
    pencil = Pencil('pencil')
    pencil.draw()
    red_marker = Handle('red_marker')
    red_marker.draw()
