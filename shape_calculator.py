class Rectangle:
  def __init__(self, width, height):
    self.set_width(width)
    self.set_height(height)

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.heigth = height

  def get_area(self):
    return (self.width * self.heigth)
  
  def get_perimeter(self):
    return (2 * self.width + 2 * self.heigth)

  def get_diagonal(self):
    return ((self.width ** 2 + self.heigth ** 2) ** .5)
    
  def get_picture(self):
    output = ""
    if self.width > 50 or self.heigth > 50:
      return "Too big for picture."
    for i in range(self.heigth):
      for j in range(self.width):
        output += "*"
      output += "\n"
    return output

  def get_amount_inside(self, sqr):
    return (int(self.get_area() / sqr.get_area()))
    
  def __str__(self):
    if self.width != self.heigth:
      return (f"Rectangle(width={self.width}, height={self.heigth})")
    else:
      return (f"Square(side={self.width})")


class Square(Rectangle):
  def __init__(self, side):
    self.set_side(side)
  
  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)
  
  def set_width(self, width):
    self.width = width
    self.heigth = width


  