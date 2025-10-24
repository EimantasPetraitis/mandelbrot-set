# Mandelbrot set image generator
# Main file

from datetime import datetime
from PIL import Image

import generator

image_location = r"Mandelbrot Set.png"

image_size = 1024  # Both the width and length
iterations = 64


# Main

print("Generating...")
generation_begin_time = datetime.now()

image = Image.new(
    mode="RGB", size=(image_size, image_size), color=(0, 0, 0)
)
pixels = image.load()

image_center = (int(image_size / 2) + 1, int(image_size / 2) + 1)

for y in range(image_size):
    for x in range(image_size):

        pixels[x, y] = generator.calculate_pixel(
            x, y, image_size, iterations
        )
    
    print(f"{int(y/image_size * 100)}%")

image.save(image_location)

generation_end_time = datetime.now()
generation_time = generation_end_time - generation_begin_time

print("\nDone.")
print(f"Time taken:  {generation_time}")