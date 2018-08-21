class Point:
    """class that represents a point in the plane"""

    def __init__(self, xcoord=0, ycoord=0):
        """ (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)"""
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        """ (Point,number)->None
        Sets x coordinate of point to xcoord"""
        self.x = xcoord

    def sety(self, ycoord):
        """ (Point,number)->None
        Sets y coordinate of point to ycoord"""
        self.y = ycoord

    def get(self):
        """(Point)->tuple
        Returns a tuple with x and y coordinates of the point"""
        return (self.x, self.y)

    def move(self, dx, dy):
        """(Point,number,number)->None
        changes the x and y coordinates by dx and dy"""
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        """(Point,Point)->bool
        Returns True if self and other have the same coordinates"""
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """(Point)->str
        Returns canonical string representation Point(x, y)"""
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        """(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__"""
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    """Class that creates a rectangle in a plane."""

    def __init__(self, bl, tr, color):
        self.color = color
        self.bl = bl
        self.tr = tr

    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation of Rectangle(p1, p2, color)
        '''
        return "Rectangle(Point(" + str(self.bl.x) + "," + str(self.bl.y) + "),Point(" + str(self.tr.x) + "," + str(self.tr.y) + "),'" + str(self.get_color()) + "')"

    def __str__(self):
        """
        (Rectangle) -> str
        Returns the string representation of Rectangle(p1, p2, color)
        :return: str
        """
        return "I am a " + str(self.get_color()) + " rectangle with my bottom left corner at " + str(self.bl.get()) + " and top right corner at " + str(self.tr.get()) + "."

    def __eq__(self, other):
        """
        (Rectangle, Rectangle) -> bool
        Manages equivalency of two rectangles
        :param other: another rectangle.
        :return: compares the two points and the colors of the rectangles.
        """
        return self.bl == other.bl and self.tr == other.tr and self.get_color() == other.get_color()

    def get_color(self):
        """
        (Rectangle) -> str
        :return: The color of the rectangle as a string.
        """
        return self.color

    def get_bottom_left(self):
        """
        (Rectangle) -> str
        :return: returns a canonical representation of the bottom left Point(x,y)
        """

        return self.bl
        #return "Point(" + str(self.bl.x) + "," + str(self.bl.y) + ")"

    def get_top_right(self):
        """
        (Rectangle) -> str
        :return: returns a canonical representation of the top right Point(x,y)
        """
        return self.tr
        #return "Point(" + str(self.tr.x) + "," + str(self.tr.y) + ")"

    def reset_color(self, new_c):
        """
        (Rectangle, str) -> None
        Changes colour of THIS rectangle.
        :param new_c: The new color for the rectangle.
        :return: None
        """

        self.color = new_c

    def move(self, dx, dy):
        """
        (Rectangle, number, number) -> None
        Move full rectangle by dx and dy.
        :param dx: value to move horizontally.
        :param dy: value to move vertically.
        :return: None
        """
        self.bl.move(dx, dy)
        self.tr.move(dx, dy)

    def get_perimeter(self):
        """
        (Rectangle) -> number
        :return: Returns the perimeter of this rectangle.
        """

        return 2*((self.tr.x - self.bl.x)+(self.tr.y - self.bl.y))

    def get_area(self):
        """
        (Rectangle) -> number
        :return: area of this rectangle.
        """

        return (self.tr.x - self.bl.x)*(self.tr.y - self.bl.y)

    def intersects(self, other):
        """
        (Rectangle, Rectangle) -> bool
        :param other: a rectangle
        :return: True or False for whether the two rectangles share at least one point.
        """

        if (self.bl.x <= other.bl.x <= self.tr.x) or (self.bl.x <= other.tr.x <= self.tr.x):
            if (self.bl.y <= other.bl.y <= self.tr.y) or (self.bl.y <= other.tr.y <= self.tr.y):
                return True
            elif (other.bl.y < self.bl.y) and (self.tr.y < other.tr.y):
                return True
            else:
                return False
        elif (other.bl.x < self.bl.x) and (self.tr.x < other.tr.x):
            if (self.bl.y <= other.bl.y <= self.tr.y) or (self.bl.y <= other.tr.y <= self.tr.y):
                return True
            elif (other.bl.y < self.bl.y) and (self.tr.y < other.tr.y):
                return True
            else:
                return False
        else:
            return False

    def contains(self, x, y):
        """
        (Rectangle, number, number) -> bool
        :param x: the x coordinate
        :param y: the y coordinate
        :return: returns true if the given point falls inside the rectangle.
        """

        if (self.bl.x <= x <= self.tr.x) and (self.bl.y <= y <= self.tr.y):
            return True
        else:
            return False

class Canvas():

    def __init__(self):
        """
        (Canvas) -> None
        Initializes Canvas.
        """

        self.rectCollection = []

    def __len__(self):
        """
        (Canvas) -> int
        :return: the number of rectangles on the canvas.
        """

        return len(self.rectCollection)

    def __repr__(self):
        """
        (Canvas) -> str
        :return: Canonical string representation of Canvas.
        """
        rectAsStr = ""
        for i in self.rectCollection:
            rectAsStr += (repr(i) + ", ")

        return "Canvas([" + rectAsStr[: (len(rectAsStr) - 2)] + "])"

    def add_one_rectangle(self, r):
        """
        (Canvas, Rectangle) -> None
        :param r: Rectangle to be added to Canvas
        :return: None
        """

        self.rectCollection.append(r)

    def count_same_color(self, color):
        """
        (Canvas, str) -> int
        :param color: string of color name
        :return: Number of rectangles in Canvas of same color.
        """
        counter = 0
        for i in self.rectCollection:
            if i.get_color() == color:
                counter += 1

        return counter

    def total_perimeter(self):
        """
        (Canvas) -> number
        :return: returns the sum of all the perimeters of all the rectangles in Canvas.
        """
        sumPeri = 0
        for i in self.rectCollection:
            sumPeri += i.get_perimeter()

        return sumPeri

    def min_enclosing_rectangle(self):
        """
        (Canvas) -> Rectangle
        :return: The smallest rectangle that contains all rectangles on this canvas.
        """

        minX = self.rectCollection[0].bl.x
        maxX = self.rectCollection[0].tr.x

        minY = self.rectCollection[0].bl.y
        maxY = self.rectCollection[0].tr.y

        for rect in self.rectCollection:

            if rect.bl.x < minX:
                minX = rect.bl.x
            if rect.bl.y < minY:
                minY = rect.bl.y

            if maxX < rect.tr.x:
                maxX = rect.tr.x
            if maxY < rect.tr.y:
                maxY = rect.tr.y

        return Rectangle(Point(minX, minY), Point(maxX, maxY), "beige")

    def common_point(self):
        """
        (Canvas) -> bool
        :return: true if all rectangles on Canvas have a common point
        """

        for i in range(len(self.rectCollection)):
            for j in range(i+1, len(self.rectCollection)):
                if not self.rectCollection[i].intersects(self.rectCollection[j]):
                    return False

        return True