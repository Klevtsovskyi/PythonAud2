from turtle import *


class Figure:
    """ Клас Фігура """

    def __init__(self, x, y, color):
        """ Конструктор

        :param x: координата x положення фігури
        :param y: координата y положення фігури
        :param color: колір фігури
        """
        self._x = x  # _x - координата x
        self._y = y  # _y - координата y
        self._visible = False  # _visible - чи є фіруга видимою на екрані
        self._color = color    # _color - колір фігури

    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує фігуру заданим кольором
        Тут здійснюється лише декларація методу, а конкретна
        реалізація буде здійснюватися у конкретних нащадках
        :param color: колір
        """
        pass

    def show(self):
        """ Зображує фігуру на екрані """
        if not self._visible:
            self._visible = True
            self._draw(self._color)

    def hide(self):
        """ Ховає фігуру (робить її невидимою на екрані) """
        if self._visible:
            self._visible = False
            # щоб сховати фігуру, потрібно
            # зобразити її кольором фону.
            self._draw(bgcolor())

    def move(self, dx, dy):
        """ Переміщує об'єкт
        :param dx: зміщення у пікселях по осі X
        :param dy: зміщення у пікселях по осі Y
        """
        isVisible = self._visible
        if isVisible:
            self.hide()
        self._x += dx
        self._y += dy
        if isVisible:
            self.show()


######################  клас Circle  ###########################
################################################################
class Circle(Figure):
    """ Клас Коло """

    def __init__(self, x, y, r, color):
        """ Конструктор
        Ініціалізує положення кола, його радіус і колір
        :param x: координата x центру кола
        :param y: координата y центру кола
        :param r: радіус кола
        :param color: колір кола
        """
        super().__init__(x, y, color)  # Обов’язковий виклик конструктора базового класу
        self._r = r  # _r - радіус кола

    def _draw(self, color):
        """ Допоміжний метод, що зображує коло заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        # малює починаючи знизу кола
        setpos(self._x, self._y - self._r)
        down()
        circle(self._r)
        up()


#################### клас Quadrate  ############################
################################################################

class Quadrate(Figure):
    """ Клас Квадрат """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижнього кута квадрата,
        довжину його сторони і колір.
        :param x: координата x лівого нижнього кута квадрата
        :param y: координата y лівого нижнього кута квадрата
        :param a: довжина сторони квадрата
        :param color: колір квадрата
        """
        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        """ Допоміжний метод, що зображує квадрат заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(4):
            forward(self._a)
            left(90)
        up()

#################### клас Triangle  ############################
################################################################

class Triangle(Figure):
    """ Клас Трикутник

    Використовується для зображення правильного трикутника на екрані
    """

    def __init__(self, x, y, a, color):
        """ Конструктор
        Ініціалізує положення лівого нижньої вершини трикутника,
        довжину його сторони і колір.
        :param x: координата x лівої нижньої вершини трикутника
        :param y: координата y лівої нижньої вершини трикутника
        :param a: довжина сторони трикутника
        :param color: колір трикутника
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a

    def _draw(self, color):
        """ Допоміжний віртуальний метод, що зображує трикутник заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(3):
            forward(self._a)
            left(120)
        up()

#################### клас Trapezoid  ###########################
################################################################

class Trapezoid(Figure):
    """ Клас Трапеція

    Використовується для зображення рівнобічної трапеції на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: довжина більшох основий трапеції
        :param b: довжина меншої основий трапеції
        :param color: колір трапеції
        """

        super().__init__(x, y, color)  # виклик конструктора базового класу
        self._a = a
        self._b = b

    def _draw(self, color):
        """ Віртуальний метод, що зображує трапецію на екрані заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        forward(self._a)
        left(120)
        forward(self._a - self._b)
        left(60)
        forward(self._b)
        left(60)
        forward(self._a - self._b)
        left(120)
        up()

#################### клас Rectangle  ###########################
################################################################

class Rectangle(Trapezoid):
    """ Клас Прямокутник

    Використовується для зображення прямокутника на екрані
    """

    def __init__(self, x, y, a, b, color):
        """ Конструктор
        Ініціалізує положення лівої нижньої вершини,
        довжини його основ і колір.
        :param x: координата x лівої нижньої вершини
        :param y: координата y лівої нижньої вершини
        :param a: перша сторона прямокутника
        :param b: друга сторона прямокутника
        :param color: колір прямокутника
        """
        super().__init__(x, y, a, b, color)  # виклик конструктора базового класу

    def _draw(self, color):
        """ Віртуальний метод, що зображує прямокутник на екрані заданим кольором
        :param color: колір
        """
        pencolor(color)
        up()
        setpos(self._x, self._y)
        down()
        for i in range(2):
            forward(self._a)
            left(90)
            forward(self._b)
            left(90)
        up()


class Cross(Figure):

    def __init__(self, x, y, a, color):
        super().__init__(x, y, color)
        self._a = a

    def _draw(self, color):
        pencolor(color)
        up()
        setpos(self._x, self._y)
        d = (2 * self._a**2)**0.5
        setheading(45)
        forward(d / 2)
        down()
        backward(d)
        up()
        left(45)
        forward(self._a)
        left(45)
        down()
        backward(d)
        up()
        setheading(0)


################################################################
################################################################
# Перевірка роботи описаних класів.
if __name__ == '__main__':
    # Ініціалізація turtle
    home()
    delay(30)
    speed(10)

    ###### Перевірка кола ############
    c = Circle(120, 120, 50, "blue")
    c.show()
    c.move(-30, -140)
    c.hide()

    ###### Перевірка квадрата ############
    q = Quadrate(0, 0, 150, "red")
    q.show()
    q.move(0, 140)
    q.hide()

    ###### Перевірка трикутника ############
    t = Triangle(120, 120, 50, "blue")
    t.show()
    t.move(-30, -140)
    t.hide()

    ###### Перевірка трапеції ############
    t = Trapezoid(120, 120, 50, 30, "red")
    t.show()
    t.move(-30, -140)
    t.hide()

    ###### Перевірка прямокутника ############
    t = Rectangle(120, 120, 50, 30, "red")
    t.show()
    t.move(-30, -140)
    t.hide()

    c = Cross(100, 100, 50, "red")
    c.show()
    c.move(-30, -140)
    c.hide()

    mainloop()
