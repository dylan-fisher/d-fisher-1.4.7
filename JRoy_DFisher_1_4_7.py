import PIL
import matplotlib.pyplot as plt
import os.path              
import PIL.ImageDraw 

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'Will Smith.jpg')

# Open and show the Will Smith image in a new Figure window
Will_Smith_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 6)
axes[0].imshow(Will_Smith_img, interpolation='none')

# Display Will Smith in second axes and set window to the right eye
axes[1].imshow(Will_Smith_img, interpolation='none')
fig.show()

student_file = os.path.join(directory, 'Oprah.jpg')
Oprah_img = PIL.Image.open(student_file)
axes[1].imshow(Oprah_img, interpolation='none')
fig.show()

student_file = os.path.join(directory, 'Young Channing Tatum.jpg')
Young_Channing_Tatum_img = PIL.Image.open(student_file)
axes[3].imshow(Young_Channing_Tatum_img, interpolation='none')
fig.show()

student_file = os.path.join(directory, 'Ariana Grande.jpg')
Ariana_Grande_img = PIL.Image.open(student_file)
axes[2].imshow(Ariana_Grande_img, interpolation='none')
fig.show()

student_file = os.path.join(directory, 'Morgan Freeman.jpg')
Morgan_Freeman_img = PIL.Image.open(student_file)
axes[4].imshow(Morgan_Freeman_img, interpolation='none')
fig.show()

student_file = os.path.join(directory, 'Angelina Jolie.jpg')
Angelina_Jolie_img = PIL.Image.open(student_file)
axes[5].imshow(Angelina_Jolie_img, interpolation='none')
fig.show()

import Image, ImageOps
ImageOps.expand(Image.open('Will Smith.jpg'),border=30,fill='black').save('Will Smith.png')