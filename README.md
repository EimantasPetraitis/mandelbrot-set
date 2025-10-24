# mandelbrot-set

A Python program to generate static images of the Mandelbrot set using the "escape time" algorithm. The colors of the pixels outside the Mandelbrot set are determined using a simplified HSV to RGB conversion.

Note that the method used is unoptimized and rather slow. On a 9th Gen Intel Core i7, images took the following times to generate:

|Image dimensions   |Number of iterations   |Generation time
|-------------------|-----------------------|---------------
|1024x1024          |64                     |12 s
|2048x2048          |64                     |47 s
|4096x4096          |64                     |190 s
|4096x4096          |128                    |315 s

To run the program, modify `image_location`, `image_size` and `iterations` in `main.py` as desired, then run `main.py`.