__author__ = 'shaloba'


class Shape(object):
    def draw(self):
        print self.__class__.__name__ + ' shape.'


class Rectangle(Shape):
    def draw(self):
        super(Rectangle, self).draw()


class Square(Shape):
    def draw(self):
        super(Square, self).draw()


class Circle(Shape):
    def draw(self):
        super(Circle, self).draw()


class ShapeFactory():
    @staticmethod
    def get_shape(shape_type):
        if shape_type is None:
            return None

        elif shape_type == 'Rectangle':
            return Rectangle()

        elif shape_type == 'Square':
            return Square()

        elif shape_type == 'Circle':
            return Circle()


if __name__ == '__main__':
    rectangle_obj = ShapeFactory.get_shape('Rectangle')
    square_obj = ShapeFactory.get_shape('Square')
    circle_obj = ShapeFactory.get_shape('Circle')
    rectangle_obj.draw()
    square_obj.draw()
    circle_obj.draw()
