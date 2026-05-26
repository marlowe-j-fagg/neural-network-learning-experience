from PIL import Image
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def make_waits_aray():
    blank= [[]]
    waits = []
    layers = int(input("enter number of layers"))
    for x in range (layers):
        waits.extend(blank)
    print (waits)
    for x in range (layers):
        nurons = int(input("enter number of nurons in layer",x))
        waits[x].extend(blank)
    print(waits)
def make_input_array_training():
    num=0
    training_values= [[],[],[],[],[],[],[],[],[],[]]
    for x in range(1,60001):
        not_found=True
        file_name = ""
        while not_found and num <= 10:
            try:
                image = Image.open("images/training/"+str(num)+"_"+str(x)+".png")
                not_found = False
            except:
                num+=1
        width, hight = image.size
        pixel_values= [[]]
        for y in range(hight):
             for i in range(width):
                pixel_values[0].append(image.getpixel((i,y)))
        training_values[num].extend(pixel_values)
    print(training_values)
    end = input("enter to end")
    return training_values
training_input_array = make_input_array_training()
