**base line (session 0)**





*what is the project?*



the aim is to build a basic neural network based on my current knowledge without the use of libraries like pytorch and tensor flow



*what is my current knowledge?*



I am currently a y9 student studying computer science who occasionally dose python and unity projects outside of school I have looked at some neural network things but not that many



*what is the point of this project?*



the aim is to use this a learning experiment and possibly as a project to go onto a portfolio



*how will I do / what are the rules?*



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



**session 1** (will be formatted so first just by my thoughts on what I might do and just thoughts before starting the session on the whole project and that session then when it says session 1 dev log will be me reporting on what I did this will continue for the whole project)



*plan*



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



*session 1 dev log (this is what I actually did)*



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



*any way end of session 1*

&#x09;

