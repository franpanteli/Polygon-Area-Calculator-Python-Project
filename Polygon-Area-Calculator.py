"""
  -> We are defining a rectangle class and a square class 
  -> Each of these two classes have different methods 
      -> The square class inherits methods from the  rectangle class 
      -> Square is a special case of rectangle, where the width equals the height 
"""

# THE RECTANGLE CLASS 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Rectangle:

# Initialization (__init__ method) 
# This method initialises the width and height of a rectangle object 
  def __init__(self, width, height):
    self.width = width
    self.height = height

# String representation (__str__ method) 
# This prints out the rectangle object, using f strings 
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

# Setter methods (set_width and set_height) 
# These methods allow us to update the width and or height of the rectangle respectively
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

# Geometric calculation methods (get_area, get_perimeter, get_diagonal) 
  # These methods allow us to calculate the rectangle attributes (area, perimeter and diagonal)
  # This is done using equations for rectangles 
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * (self.width + self.height)

  def get_diagonal(self):
    return (self.width**2 + self.height**2)**0.5

  # Drawing method (get_picture) <- This method returns the rectangle, made out of asterisks
      # If this is too large, then we return the message that this is the case and it can't be printed out 
      # Otherwise, it is printed out as a horizontal line of asterisks 
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    rectangle = ("*" * self.width + "\n") * self.height
    return rectangle

  # Containment check (get_amount_inside) <- This method calculates the number of times a shape can fit in the rectangle 
    # We calculate the maximum number of times the shape can fit horizontally and vertically into the rectangle 
    # And then we return the product of these values as area 
  def get_amount_inside(self, shape):
    max_width = self.width // shape.width
    max_height = self.height // shape.height
    return max_width * max_height

# THE SQUARE CLASS 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class Square(Rectangle):
"""
    -> Defining the methods for the square class
    -> Initialization (__init__ method): <- This method initialises a square object 
      -> This has a single parameter (`length`)
      -> The width of a square equals its height, so we only need one length parameter for this, in comparison to
        the first rectangle class
"""

  def __init__(self, length):
    super().__init__(length, length)

# -> String Representation (__str__ method) <- This method prints the square using strings 
	# -> This also mentions the length of each of the sides of the square

  def __str__(self):
    return f"Square(side={self.width})"

# This method sets the side length of the square 
# We are updating the width and height values of a rectangle object to be the same 
# -> This creates the square object 

"""
    -> The next methods we define are for overriding those inherited from the rectangle class 
    ->The square is a special case of the rectangle, where its height equals its width 
    -> When we redefine the height or width of the square, the alternative dimension needs to update itself - because 
      the square class is based on the rectangle class 
    -> This is what these next two methods do, depending on which of the parameters was updated for the square 
    -> So now we can visualise the square, as well as change its dimensions 
"""

  def set_side(self, side):
    self.width = side
    self.height = side

  # These two methods are not required since Square inherits from Rectangle and
  # the inherited set_width and set_height methods work the same way as set_side.
  # Keeping them for consistency and clarity.
  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side