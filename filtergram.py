import filters

def main():
    #what image the user wants to edit
    filename = input("Enter the name of the image file to edit:")

    #Load the image from the specified filename
    img = filters.load_img(filename)

    #Apply filters
    newimg = filters.obamicon(img)

    newlen = filters.purple(img)

    #Save the final filtered image
    filters.save_img(newimg, "recolored.jpg")
    filters.save_img(newlen, "recolored.jpg")

    #Setup code
if __name__ == "__main__":
  main()
