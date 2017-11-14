# def setup():
#     global image1
#     size(500, 500)
#     image1 = loadImage("disneyLand.jpg")
#     image(image1, 0, 0, 500, 500)
#     loadPixels()   #read the colors into the list called "pixels".
    
#     # for i in range(width*5):    #iterate through the first 5 rows
#     #     pixels[i] = color(255, 102, 204)
#     # updatePixels()  #this must be called to update the image with the changes

    
# def draw():
#     global image1
#     pixels1 = width * height 
#     m = 0
#     i = 0
#     for m in range (width):
#         for i in range (height):
#             loadPixels()   #read the colors into the list called "pixels".
#             r = red(pixels[i])    #get the red component of the first pixel
#             g = green(pixels[i])     #get the green component of the first pixel
#             b = blue(pixels[i])    #get the blue component of the first pixel
#             i = i + 1
#             updatePixels()  #this must be called to update the image with the changes
#         m = m + 1
#         pixels[i] = color(r *.1, g, b)
#     image(image1, 0, 0, 500, 500)  #displays the image


size(300, 300)
image1 = loadImage("disneyLand.jpg")
i = 0
for i in range (20):
    loadPixels()   #read the colors into the list called "pixels".
    r = red(pixels[i])
    g = green(pixels[i])
    b = blue(pixels[i])
    pixels[i] = color(255 - r, 255 - g, 255 - b)
    i = i + 1
updatePixels()  #this must be called to update the image with the changes
image(image1, 0, 0, 300, 300)
