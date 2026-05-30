from PIL import Image
import os
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def make_waits_and_bises_array():
    blank= []
    waits = []
    layers = int(input("enter number of layers including input but not output"))
    for x in range (layers):
        waits.append([])
    for x in range (layers):
        nurons = int(input("enter number of nurons in layer"))
        for i in range(nurons):
            waits[x].append([])
    return waits,waits

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
                pixel_values[0].append((image.getpixel((i,y)))/255)
        training_values[num].extend(pixel_values)
    print(training_values[5][1])
    end = input("enter to end")
    return training_values

def make_input_array_testing():
    num=0
    testing_values= [[],[],[],[],[],[],[],[],[],[]]
    for x in range(1,60001):
        not_found=True
        file_name = ""
        while not_found and num <= 10:
            try:
                image = Image.open("images/testing/"+str(num)+"_"+str(x)+".png")
                not_found = False
            except:
                num+=1
        width, hight = image.size
        pixel_values= [[]]
        for y in range(hight):
             for i in range(width):
                pixel_values[0].append((image.getpixel((i,y)))/255)
        testing_values[num].extend(pixel_values)
    print(testing_values[5][1])
    end = input("enter to end")
    return testing_values

def run_nuron(inputs): 
    WxN=[]
    un_sigmoided = 0
    for x in range(len(waits[layer][nuron])):
        WxN.append(waits[layer][nuron][x]*inputs[x])
    for x in range (len(WxN)):
        un_sigmoided+=WxN[x]
    un_sigmoided+=bieses[layer][nuron]
    output = sigmoid(un_sigmoided)
    return output

def run_network(image_array,digit,image):
    inputs=image_array[digit][image]
    outputs=[]
    for x in range(len(waits)):
        for i in range(len(waits[x])):
            outputs.append(run_nuron(inputs))
        inputs = outputs
        outputs=[]
    np.exp(x) / np.sum(np.exp(inputs), axis=0)
     
def rate_output(output,corect_digit):
    for x in range (len(output)):
        if x != corect_digit
            if output[corect_digit]-output[x]>0:
                corect = True
            else:
                corect=False
    closness = 1-output[corect_digit]
    return closness,corect

waits,bieses = make_waits_and_bises_array()

training_input_array = make_input_array_training()

testing_input_array = make_input_array_testing


