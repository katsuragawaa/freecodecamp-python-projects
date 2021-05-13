class Rectangle:
    def __init__(self) -> None:
        self.width = None
        self.heigth = None



# Subclass of Rectangle
class Square(Rectangle):
    def __init__(self) -> None:
        super().__init__()