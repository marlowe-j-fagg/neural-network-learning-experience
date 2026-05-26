base line (session 0)





what is the project?



the aim is to build a basic neural network based on my current knowledge without the use of libraries like pytorch and tensor flow



what is my current knowledge?



I am currently a y9 student studying computer science who occasionally dose python and unity projects outside of school I have looked at some neural network things but not that many



what is the point of this project?



the aim is to use this a learning experiment and possibly as a project to go onto a portfolio



how will I do / what are the rules?



it will be done in 3 main stages (I think) u will put the rules for each below



stage 1

aim - make a basic thing based of only my current understanding on neural networks



&#x09;rules

&#x09;- no use of ai

&#x09;- can not copy and past large sections of code for logic

&#x09;- can use some sources to try to fix a problem after identifying it

&#x09;- all code must be hand written and based of own ideas



stage 2

aim - use are first draft from stage one then do some more deeper research on how neural networks work to make one that works better



&#x09;rules

&#x09;- no use of ai

&#x09;- can not copy and past large sections of code for logic

&#x09;- can use some sources to try to fix a problem

&#x09;- all code must be hand written

&#x09;- can do more research on neural networks to improve model



stage 3

aim - currently unknown hoping to do it based off how the rest of it goes



session 1 (will be formatted so first just by my thoughts on what I might do and just thoughts before starting the session on the whole project and that session then when it says session 1 dev log will be me reporting on what I did this will continue for the whole project)



plan



ok this is the initial plan and idea for the network no idea if it correct or even a real neural network



stages of the program



stage 1

find out data of who many neurons and layers and set up any other things that are needed early

stage 2

run the neural network

stage 3

evaluate success/fail or out put result depending on weather training or testing

stage 4

august weights



this session aim to just start and see where it goes



session 1 dev log (this is what I actually did)



started with testing systems to make the aray wich would store the difearnt waight intialy I could not find a dicent scalabul version my test was using a manuel method like



waits = \[]

&#x20;   layers = int(input("enter number of hiden layers: 1 2 3 4 or 5"))

&#x20;   while layers >5 :

&#x20;       print ("enter a number from 1-5")

&#x20;       layers = int(input("enter number of hiden layers: 1 2 3 4 or 5"))

&#x20;   if layers ==5:

&#x20;       waits = \[waits,waits,waits,waits,waits,waits]

&#x20;   if layers ==4:

&#x20;       waits = \[waits,waits,waits,waits,waits]

&#x20;   if layers ==3:

&#x20;       waits = \[waits,waits,waits,waits]

&#x20;   if layers ==2:

&#x20;       waits = \[waits,waits,waits]

&#x20;   if layers ==1:

&#x20;       waits = \[waits,waits]



thow after looking at the following sorce https://www.w3schools.com/python/python\_lists\_add.asp and test using the exend function and blank arrays to add demention variabuly without having a if for each test using the following test



array = \[\[],\[]]

blank = \[\[]]

num = int(input("enter"))

for x in range (num):

&#x20;   array\[0].extend(blank)

print (array)



output if input = 3



\[\[\[], \[], \[]], \[]]



from this I then could use it to make the number of layers and nurons more atomatic and varabul changing the system to



blank= \[\[]]

waits = \[]

layers = int(input("enter number of layers"))

for x in range (layers):

&#x20;   waits.extend(blank)

print (waits)

for x in range (layers):

&#x20;   nurons = int(input("enter number of nurons in layer",x))

&#x20;   waits\[x].extend(blank)

print(waits)



this xan be done as it allows us to add the contence of blank without removing or using the origan version like bufor I just tested and tern out you can do this with append like waits.append(\[]) but I have done this now and do not see a reason to change anyway the whole reason for the step is to generate the intal array to stor the waits it works as follows



when talking I will be refering to the aereas with a # in them



waits = \[\[#],\[#]] for this each # will be array sotring all the lists of waits for each nuron in that layer wich lists will be the waits = \[\[\[#],\[#]],\[\[#],\[#],\[#]]] in this exsample we have to hiden layers the first with 2 nurons and the second with 3



note : I have not included the waits for the conections between the last hiden layer and the output will add that later



(should mention nurel network will be to identify numbers from a pixel image)



I think this is where I will elave it for this session and next will work on what ever I use to prosses the images or data for training and testing/recognition(I put something in it tells me) for this I currently have a few ideas



\-use the mnist dataset (currently do not now how that would work without the libarys)

\-make a separate program to tern the minst into actual image files then use pillow for processing

\-make my own images though asprite and use pillow

\-learn tkinter and make a drawing pad (I think this might be something for stage 2 but not now)



any way end of session 1



session 2



for this session I decided to go for making a program to convert the mnist dataset into pngs wich may seam counter productive as I will convert them strait back into numbers in the program but I chose this method as I think I will learn th most and it means I can use the system for any saved image if I waa\\nt to add a drawing pad or use my own images later on a started by testing image generation using pillow



from PIL import Image



\# Setting the size of the image

size = (28, 28)



\# Creating a new image with RGB mode

new\_image = Image.new('L', size, color='white')

new\_image.putpixel((10,10),(0))

\# Save the image

new\_image.save('new\_image.png')



and found some code to get the data formatted nicly note: thr following was not done by me I classed this as not agensit the rules as this is kind of an extra program just to get the data I will still make the actual image maker thow just usiong code that's not mine for garthering and making the arrays \[my network will go of the images made not this]



mndata = MNIST('./mnist\_data')

mndata.gz = True



train\_images, train\_labels = mndata.load\_training()

test\_images, test\_labels = mndata.load\_testing()



def flatten\_image(flat\_img):

&#x20;   return flat\_img

def group\_by\_digit(images, labels):

&#x20;   grouped = \[\[] for \_ in range(10)]

&#x20;   for img, label in zip(images, labels):

&#x20;       grouped\[label].append(flatten\_image(img))

&#x20;   return grouped



train\_grouped = group\_by\_digit(train\_images, train\_labels)

test\_grouped = group\_by\_digit(test\_images, test\_labels)



print("Training counts:", \[len(x) for x in train\_grouped])

print("Test counts:", \[len(x) for x in test\_grouped])



so then I tested just making one image



from mnist import MNIST

from PIL import Image



\#start of not mine

mndata = MNIST('./mnist\_data')

mndata.gz = True



train\_images, train\_labels = mndata.load\_training()

test\_images, test\_labels = mndata.load\_testing()



def flatten\_image(flat\_img):

&#x20;   return flat\_img



def group\_by\_digit(images, labels):

&#x20;   grouped = \[\[] for \_ in range(10)]

&#x20;   for img, label in zip(images, labels):

&#x20;       grouped\[label].append(flatten\_image(img))

&#x20;   return grouped



train\_grouped = group\_by\_digit(train\_images, train\_labels)

test\_grouped = group\_by\_digit(test\_images, test\_labels)



print("Training counts:", \[len(x) for x in train\_grouped])

print("Test counts:", \[len(x) for x in test\_grouped])

\#end of not mine \[rest is mine]



size = (28, 28)

new\_image = Image.new('L',size)

n=0

for y in range (28):

&#x20;   for x in range (28):

&#x20;       new\_image.putpixel((x,y),train\_grouped\[8]\[0]\[n])

&#x20;       n+=1

new\_image.save('test1.png')



this sucsesfuly made a image so I will now scale this to make them all and this is the code that makes all 70,000 \[I am just showing the imag generation code I made]



for a in range(10):

&#x20;   for i in range (len(train\_grouped\[a])):

&#x20;       size = (28, 28)

&#x20;       new\_image = Image.new('L',size)

&#x20;       n=0

&#x20;       for y in range (28):

&#x20;           for x in range (28):

&#x20;               new\_image.putpixel((x,y),train\_grouped\[a]\[i]\[n])

&#x20;               n+=1

&#x20;       name="images/training/"+str(a)+"\_"+str(i)+".png"

&#x20;       new\_image.save(name)

for a in range(10):

&#x20;   for i in range (len(test\_images\[a])):

&#x20;       size = (28, 28)

&#x20;       new\_image = Image.new('L',size)

&#x20;       n=0

&#x20;       for y in range (28):

&#x20;           for x in range (28):

&#x20;               new\_image.putpixel((x,y),test\_grouped\[a]\[i]\[n])

&#x20;               n+=1

&#x20;       name="images/testing/"+str(a)+"\_"+str(i)+".png"

&#x20;       new\_image.save(name)



the code makes all images saving them in 2 separate files for the training set and one for the test set the names are also named like a\_i.png as a represents the correct number wich iu can use for training / testing and the I then gives them all a speert name



session 3



aim



make a program to tern the images back into an array for the network to procces



log I started with a slight edit to how the image maker works so now instead or reseting the second number every new digit it carrys so for training gose from 1-60000 new code bellow



from mnist import MNIST

from PIL import Image



mndata = MNIST('./mnist\_data')

mndata.gz = True



train\_images, train\_labels = mndata.load\_training()

test\_images, test\_labels = mndata.load\_testing()



def flatten\_image(flat\_img):

&#x20;   return flat\_img

def group\_by\_digit(images, labels):

&#x20;   grouped = \[\[] for \_ in range(10)]

&#x20;   for img, label in zip(images, labels):

&#x20;       grouped\[label].append(flatten\_image(img))

&#x20;   return grouped



train\_grouped = group\_by\_digit(train\_images, train\_labels)

test\_grouped = group\_by\_digit(test\_images, test\_labels)



print("Training counts:", \[len(x) for x in train\_grouped])

print("Test counts:", \[len(x) for x in test\_grouped])

count=0

for a in range(10):

&#x20;   for i in range (len(train\_grouped\[a])):

&#x20;       size = (28, 28)

&#x20;       new\_image = Image.new('L',size)

&#x20;       n=0

&#x20;       count+=1

&#x20;       for y in range (28):

&#x20;           for x in range (28):

&#x20;               new\_image.putpixel((x,y),train\_grouped\[a]\[i]\[n])

&#x20;               n+=1

&#x20;       name="images/training/"+str(a)+"\_"+str(count)+".png"

&#x20;       new\_image.save(name)

for a in range(10):

&#x20;   for i in range (len(test\_images\[a])):

&#x20;       size = (28, 28)

&#x20;       new\_image = Image.new('L',size)

&#x20;       n=0



this allows for the method I will be using to tern it back into an array to work wich starts as follows



&#x20;   num=0

&#x20;   for x in range(1,60001):

&#x20;       training\_values= \[\[],\[],\[],\[],\[],\[],\[],\[],\[],\[]]

&#x20;       not\_found=True

&#x20;       file\_name = ""

&#x20;       while not\_found and num <= 10:

&#x20;           try:

&#x20;               image = Image.open("images/training/"+str(num)+"\_"+str(x)+".png")

&#x20;               not\_found = False

&#x20;           except:

&#x20;               num+=1



this loops thought all the images and makes the name for the file change if it is not found this in practise means that it will loop thought all the 0s lets say there is 10000 but then when it trys 0\_10001 it will fail and num will increase meaning it will now try 1\_10001 this will continue for all digits up till num gose past 10



I then did the following test



training\_values= \[\[],\[],\[],\[],\[],\[],\[],\[],\[],\[]]

test = \[\[1,65,3,4,5,6,7,8,43]]

test2 = \[\[1,2,3,4,5,6,7,8,9]]

training\_values\[0].extend(test)

training\_values\[0].extend(test2)

print(training\_values)



output



\[\[\[1, 65, 3, 4, 5, 6, 7, 8, 43], \[1, 2, 3, 4, 5, 6, 7, 8, 9]], \[], \[], \[], \[], \[], \[], \[], \[], \[]]



to test my idea for the method of actualy making the array and it worked so I will make it do the following loop thought the image from left to right adding each iimage inside of something that will act like test/test2 then use the extend to add them at training\_values\[num] so they will be assigned the index maching there digit this was the first full test



def make\_input\_array\_training():

&#x20;   num=0

&#x20;   for x in range(1,60001):

&#x20;       training\_values= \[\[],\[],\[],\[],\[],\[],\[],\[],\[],\[]]

&#x20;       not\_found=True

&#x20;       file\_name = ""

&#x20;       while not\_found and num <= 10:

&#x20;           try:

&#x20;               image = Image.open("images/training/"+str(num)+"\_"+str(x)+".png")

&#x20;               not\_found = False

&#x20;           except:

&#x20;               num+=1

&#x20;       width, hight = image.size

&#x20;       pixel\_values= \[\[]]

&#x20;       for y in range(hight):

&#x20;            for i in range(width):

&#x20;               pixel\_values\[0].append(image.getpixel((i,y)))

&#x20;       training\_values\[num].extend(pixel\_values)

&#x20;   print(training\_values)

&#x20;   end = input("enter to end")

make\_input\_array\_training()





but it only output one image for 9 so there was an issue sorry editing this as coding tern out I was just re seting the training values every time and now it works so here is the final code



def make\_input\_array\_training():

&#x20;   num=0

&#x20;   training\_values= \[\[],\[],\[],\[],\[],\[],\[],\[],\[],\[]]

&#x20;   for x in range(1,60001):

&#x20;       not\_found=True

&#x20;       file\_name = ""

&#x20;       while not\_found and num <= 10:

&#x20;           try:

&#x20;               image = Image.open("images/training/"+str(num)+"\_"+str(x)+".png")

&#x20;               not\_found = False

&#x20;           except:

&#x20;               num+=1

&#x20;       width, hight = image.size

&#x20;       pixel\_values= \[\[]]

&#x20;       for y in range(hight):

&#x20;            for i in range(width):

&#x20;               pixel\_values\[0].append(image.getpixel((i,y)))

&#x20;       training\_values\[num].extend(pixel\_values)

&#x20;   print(training\_values)

&#x20;   end = input("enter to end")

&#x20;   return training\_values

training\_input\_array = make\_input\_array\_training()

