class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Returna a string that represents the shape using lines of "*".
        """
        if self.heigth > 50:
            return "Too big for picture."
        output = ""
        for _ in range(self.height):
            for __ in range(self.width):
                output += "*"
            output += "\n"
        return output

    def get_amount_inside(self, shape):
        """
        Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        """
        if shape.width > self.width or shape.height > self.height:
            return 0
        return int(self.width/shape.width) * int(self.height/shape.height)


# Subclass of Rectangle
class Square(Rectangle):
    def __init__(self, side) -> None:
        self.side = side
        super().__init__(self.side, self.side)

    def __str__(self) -> str:
        return "Square(side={})".format(self.side)

    def set_side(self, new_side):
        self.side = new_side
        self.__init__(self.side)