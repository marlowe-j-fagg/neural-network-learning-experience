from PIL import Image

# Setting the size of the image
size = (28, 28)

# Creating a new image with RGB mode
new_image = Image.new('L', size, color='white')
new_image.putpixel((10,10),(0))
# Save the image
new_image.save('new_image.png')
