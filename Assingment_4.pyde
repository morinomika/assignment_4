def setup():
    global image1
    size(500, 500)
    image1 = loadImage("disneyLand.jpg")
    image(image1, 0, 0, 500, 500)
    # loadPixels()   #read the colors into the list called "pixels".
    # for i in range(width*5):    #iterate through the first 5 rows
    #     pixels[i] = color(255, 102, 204)
    # updatePixels()  #this must be called to update the image with the changes

    
# def draw():
#     global image1
#     pixels1 = width * height 
#     m = 0
#     i = 0
#     for m in range (width):
#         for i in range (height):
#             loadPixels()   #read the colors into the list called "pixels".
#             r = red(pixels[i]) * 0.8    #get the red component of the first pixel
#             g = green(pixels[i]) * 0.1     #get the green component of the first pixel
#             b = blue(pixels[i]) * 0.8      #get the blue component of the first pixel
#             pixels[i] = color(r, g, b)
#             i = i + 1
#             updatePixels()  #this must be called to update the image with the changes
#         m = m + 1
#     image(image1, 0, 0, 500, 500)  #displays the image