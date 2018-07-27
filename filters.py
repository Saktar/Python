#Creating a Filter
from PIL import Image

def load_img(filename):
    im = Image.open(filename)
    return im

def show_img(im):
    im.show()

def save_img(im, filename):
    im.save(filename, "jpeg")
    show_img(im)

def obamicon(im):
    #Load the pixel data from the image
    pixels = im.getdata()

    #Create a list to hold the new image pixel data
    new_pixels = []

    #Define color constants to use for recoloring
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    #Process the pixels in the Image
    for p in pixels:
        # Pixels intensity = R Value + G Value + B value
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(red)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightBlue)

        elif intensity >= 546:
            new_pixels.append(yellow)

#Save the filtered pixels as a new image
    newim = Image.new("RGB", im.size)
    newim.putdata(new_pixels)
    return newim

def purple(im):
    #Load the pixel data from the image
    pixels = im.getdata()

    #Create a list to hold the new image pixel data
    new_pixels = []

    #Define color constants to use for recoloring
    darkBlue = (0, 51, 76)
    purple = (122, 26, 78)
    lightPurple = (221,160,221)
    yellow = (252, 227, 166)

    #Process the pixels in the Image
    for p in pixels:
        # Pixels intensity = R Value + G Value + B value
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(darkBlue)

        elif intensity >= 182 and intensity < 364:
            new_pixels.append(purple)

        elif intensity >= 364 and intensity < 546:
            new_pixels.append(lightPurple)

        elif intensity >= 546:
            new_pixels.append(yellow)

    newlen = Image.new("RGB", im.size)
    newlen.putdata(new_pixels)
    return newlen
