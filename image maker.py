from mnist import MNIST
from PIL import Image

#start of not mine
mndata = MNIST('./mnist_data')
mndata.gz = True

train_images, train_labels = mndata.load_training()
test_images, test_labels = mndata.load_testing()

def flatten_image(flat_img):
    return flat_img 

def group_by_digit(images, labels):
    grouped = [[] for _ in range(10)]
    for img, label in zip(images, labels):
        grouped[label].append(flatten_image(img))
    return grouped

train_grouped = group_by_digit(train_images, train_labels)
test_grouped = group_by_digit(test_images, test_labels)

print("Training counts:", [len(x) for x in train_grouped])
print("Test counts:", [len(x) for x in test_grouped])
#end of not mine [rest is mine]


for a in range(10):
    for i in range (len(test_images[a])):
        size = (28, 28)
        new_image = Image.new('L',size)
        n=0
        for y in range (28):
            for x in range (28):
                new_image.putpixel((x,y),test_grouped[a][i][n])
                n+=1
        name="images/testing/"+str(a)+"_"+str(i)+".png"
        new_image.save(name)
