class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f'this is a {self.title}.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f'this is a {self.title}.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f'this is a {self.title}.')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()