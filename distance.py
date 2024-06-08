
from functools import total_ordering
from typing import Any

@total_ordering
class Millimeter:
    label = 'мм'
    ratio = 1 # Отношение определяемой еденицы измерения к миллиметрам

    def __init__(self, value) -> None:
        try:
            if isinstance(value, (int, float)):
                self._value = float(value)
            else:
                self._value = float(value.as_millimeters() / self.ratio)
        except TypeError:
            print('Enter a valid dictionary.')




        # if type(value) == int or type(value) == float:
        #     self._value = round(value, 5)
        # else:
        #     self._value = value.as_millimeters() / self.ratio


    def as_millimeters(self) -> float:
        """Возвращает значение длины в миллиметрах.

        :rtype: float
        :return: Значение округленное до 5 знаков после запятой
        """
        return round(self._value * self.ratio, 5)
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(value={self._value})'

    def __add__(self, other)-> Any:
        return type(self)((self.as_millimeters() / self.ratio) + (other.as_millimeters() / self.ratio))
    
    def __sub__(self, other):
        return type(self)((self.as_millimeters() / self.ratio) - (other.as_millimeters() / self.ratio))

    def __mul__(self, other):
        return type(self)((self.as_millimeters() / self.ratio) * (other.as_millimeters() / self.ratio))
    
    def __truediv__(self, other):
        if other._value == 0:
            raise 'Division by zero is not possible.'
        else:
            return type(self)((self.as_millimeters() / self.ratio) / (other.as_millimeters() / self.ratio))
    
    def __hash__(self):
        return hash(self.as_millimeters())
    
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    def __lt__(self, other):
        return self.as_millimeters() < other.as_millimeters()
    
    def __int__(self):
        return int(self.as_millimeters())
        # return int(self._value * self.ratio)

    def __float__(self):
        return float(self.as_millimeters())
    




class Centimeter(Millimeter):
    label = 'см'
    ratio = 10

class Meter(Millimeter):
    label = 'метр'
    ratio = 1000


class Inch(Millimeter):
    label = 'дюйм'
    ratio = 25.4


c = Centimeter(94.95)
i = Inch(86.44)
m = Millimeter(10.8)


(c * m).as_millimeters()



