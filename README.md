Conics
======

For a Maths assignment, this is very buggy, and is currently incapable of performing its task well.
It will spit out hundreds of equations for a simple image.

It uses OpenCV to detect the contours of the image, turn the contours into single bits. Starting from the top point of a line, it continues along the line, determining the equation of the line, until a point no longer fits in the equation (using a threshold).
It then starts again from that point. 

The code was rushed, porly written and poorly commented. I only keep it up here so that I can fix it in the future.

This:

![alt tag](https://raw.github.com/noahingham/Conics/master/rio-ro.jpg)

Becomes (using 1140 equations):

![alt tag](http://i.imgur.com/TlJuLSm.jpg)
