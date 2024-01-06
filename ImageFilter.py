'''
This program reads in an image file and outputs the associated image filter applied to it. The available filters for images are:

1. mirror: flips the image about the y-axis
2. grey: greys out the colours of the pixels
3. invert: swaps the max and min values of pixels resulting in colour change of image
4. compress: compresses dimensions of the image given

Refer to the ImageFilterTest class to see visual representation of image filters applied to the "tree.png" image
'''

from PIL import Image
from typing import List

# Modifies raw by reversing all the rows of the data.
def mirror(raw: List[List[List[int]]]):
    for row in raw:
        row.reverse()
    return raw

'''
Modifies image "averaging out" each
pixel of image. Specifically, for each pixel it totals the RGB
values, integer divides by three, and sets the all RGB values
equal to this new value
'''
def grey(raw: List[List[List[int]]]):    
    for row in raw:
        for pixel in row:
            average_value = sum(pixel) // 3

            for i in range(3):

                pixel[i] = average_value
    return raw

'''
Modifies image by inverting each pixel.
To invert a pixel, swap all the max values, with all the
minimum values. Refer to the doc tests class for examples.
'''
def invert(raw: List[List[List[int]]]):
    for row in raw:
        # Loop through each of the pixels
        for pixel in row:
            # Find the min and max values for the pixel
            min_val = min(pixel)
            max_val = max(pixel)
            for i in range(3):
                # Swap the minimum and maximum values in the pixel
                if pixel[i] == min_val:
                    pixel[i] = max_val
                elif pixel[i] == max_val:
                    pixel[i] = min_val
    return raw

'''
Compresses raw by going through the pixels and combining a pixel with
the ones directly to the right, below and diagonally to the lower right.
For each RGB values it takes the average of these four pixels using integer
division. If is is a pixel on the "edge" of the image, it only takes the
relevant pixels to average across. See the second doctest for an example of
this.
'''   
def compress(raw: List[List[List[int]]])-> List[List[List[int]]]:
    height = len(raw)
    width = len(raw[0])
    
    # Initialize list to store the compressed pixels
    compressed_raw = []
    
    for i in range(0, height, 2):
        compressed_row = []
        
        for j in range(0, width, 2):
            neighbors = [] 
            total_red, total_green, total_blue = 0, 0, 0
            
            # Iterate over neighboring pixels and retreive the values
            for x in range(2):
                for y in range(2):
                    if i + x < height and j + y < width:
                        neighbors.append(raw[i + x][j + y])
                        total_red += raw[i + x][j + y][0]
                        total_green += raw[i + x][j + y][1]
                        total_blue += raw[i + x][j + y][2]
            
            # Calculate the average of each pixel   
            avg_r = total_red // len(neighbors)
            avg_g = total_green // len(neighbors)
            avg_b = total_blue // len(neighbors)
            
            compressed_row.append([avg_r, avg_g, avg_b])
        
        compressed_raw.append(compressed_row)
    return compressed_raw


"""
Given an image path, returns the associated
image data as a list of list of pixels.
"""
def get_raw_image(name: str)-> List[List[List[int]]]:
    
    image = Image.open(name)
    num_rows = image.height
    num_columns = image.width
    pixels = image.getdata()
    new_data = []
    
    for i in range(num_rows):
        new_row = []
        for j in range(num_columns):
            new_pixel = list(pixels[i*num_columns + j])
            new_row.append(new_pixel)
        new_data.append(new_row)

    image.close()
    return new_data

'''
Given the image data, save the image in a file.
'''
def image_from_raw(raw: List[List[List[int]]], name: str)->None:
    image = Image.new("RGB", (len(raw[0]),len(raw)))
    pixels = []
    for row in raw:
        for pixel in row:
            pixels.append(tuple(pixel))
    image.putdata(pixels)
    image.save(name)