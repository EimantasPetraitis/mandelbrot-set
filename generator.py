# Functions and classes related to pixel generation

class Complex:
    """A complex number x+yi."""

    def __init__(self, real: float, imaginary: float):

        self.x = real
        self.y = imaginary

    def __add__(self, other):

        sum = Complex(self.x + other.x, self.y + other.y)
        return sum
        
    def __repr__(self) -> str:

        return f"{self.x} + {self.y}i"


def square(z: Complex):
    """Returns z squared."""

    real = z.x**2 - z.y**2
    imaginary = 2 * z.x * z.y

    return Complex(real, imaginary)


def calculate_pixel(
    x: int, y: int, image_width: int, iterations: int
) -> tuple:
    "Calculates and returns the RGB color values for the pixel at x, y."

    c = Complex(
        (x/image_width) * 4 - 2,
        (1 - y/image_width) * 4 - 2
    )
    z = c

    in_Mandelbrot_set = True
    pixel_iterations = None

    for i in range(iterations):

        if z.x**2 + z.y**2 >= 4:
            in_Mandelbrot_set = False
            pixel_iterations = i
            break

        z = square(z) + c
    
    if in_Mandelbrot_set:
        return (0, 0, 0)
    else:
        return determine_color(
            pixel_iterations, iterations,
            reverse_colors=False
        )


def determine_color(
    iterations: int, max_iterations: int,
    reverse_colors: bool = False
) -> tuple:
    """Determine the color of a pixel outside the Mandelbrot set
    based on the number of interations needed to escape 
    (this method uses a simplified HSV to RGB calculation).
    reverse_colors specifies whether to reverse the way hue is
    asigned.
    """

    if reverse_colors:
        iterations = max_iterations - iterations
    
    h = 6 * iterations/max_iterations
    x = int(255 * (h - int(h)))

    if h >= 0 and h < 1:
        return (255, x, 0)
    elif h >= 1 and h < 2:
        return (255-x, 255, 0)
    elif h >= 2 and h < 3:
        return (0, 255, x)
    elif h >= 3 and h < 4:
        return (0, 255-x, 255)
    elif h >= 4 and h < 5:
        return (x, 0, 255)
    elif h >= 5:
        return (255, 0, 255-x)