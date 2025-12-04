# mandelbrot-set

A Python program to generate static images of the Mandelbrot set using the "escape time" algorithm. The colors of pixels outside the set itself are determined using a simplified HSV to RGB conversion.

![A 2048x2048 rendering of the Mandelbrot set](https://github.com/EimantasPetraitis/mandelbrot-set/blob/main/Mandelbrot%20Set%202048x2048.png?raw=true)

Note that the method used is unoptimized and rather slow (take a look at [this GPU-based implementation](https://github.com/EimantasPetraitis/mandelbrot-shader) for something faster). On a 9th Gen Intel Core i7, images took the following times to generate:

|Image dimensions   |Number of iterations   |Generation time
|-------------------|-----------------------|---------------
|1024x1024          |64                     |12 s
|2048x2048          |64                     |47 s
|4096x4096          |64                     |190 s
|4096x4096          |128                    |315 s

To run the program, modify `image_location`, `image_size` and `iterations` in `main.py` as desired, then run `main.py`.
