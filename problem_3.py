'''
3. Создать класс Point, который представляет собой точку в двумерном пространстве. 
Класс должен иметь методы для инициализации координат точки, 
вычисления расстояния до другой точки, а также для получения и изменения координат.
'''

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x: int, y: int) -> None:
        Point.__validate(x, y)
        self.x = x
        self.y = y
    

    def __str__(self) -> str:
        return f'Point< x = {self.x}, y = {self.y} >'
    

    def get(self) -> str:
        return self.__str__()


    @staticmethod
    def __validate(*args) -> None:
        for arg in args:
            if not isinstance(arg, (int, float, complex)):
                raise ValueError('Значения x и y должны быть числовыми')


    def change_coordinate(self, x=None, y=None) -> None:
        if x is not None:
            Point.__validate(x)
            self.x = x
        if y is not None:
            Point.__validate(y)
            self.y = y
    

    def distance(self, other) -> float:
        if not isinstance(other, type(self)):
            raise ValueError('Вторая точка должна быть представлена экземпляром класса Point')
        return (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2) ** .5
