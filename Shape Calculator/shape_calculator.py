class Rectangle:
    def __init__(self, width, height):
    # Constructor sets width and height to passed numbers
        self.width = width
        self.height = height

    def set_width(self, side_length):
    # This method sets the width to a passed number
        self.width = side_length

    def set_height(self, side_length):
    # This method sets the height to a passed number
        self.height = side_length

    def get_area(self):
    # This method calculates and returns the area using w * h
        return self.width * self.height

    def get_perimeter(self):
    # This method calculates and returns the perimeter using 2*w + 2*l
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
    # This method calculates and returns the diagonal using (w^2 + h^2)^.5
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
    # This method returns a string represantion of the shape. If the
    # width or height > 50 return "Too big for picure."
        output_line = ""; height = 0

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            while height < self.height:
                new_line = ""
                new_line = new_line.ljust(self.width,"*") + "\n"
                output_line += new_line
                height += 1
            return output_line

    def get_amount_inside(self, shape):
    # This method calculates and returns the number of times a passed in shape could
    # fit inside of the called shape. Using (width1 // width2) * (height1 // height2)
        return (self.width // shape.width) * (self.height // shape.height)

    def __str__(self):
    # Instances of Rectangle represented as a string: `Rectangle(width=x, height=y)`
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
    # Constructor uses inherited set_width() and set_height() to set side length
        self.set_width(side_length)
        self.set_height(side_length)

    def set_side(self, side_length):
    # This method updates the width & height of square using passed side length
        self.width = side_length
        self.height = side_length

    def __str__(self):
    # Instances of Square represented as a string: `Square(side=x)`
        return f"Square(side={self.width})"
