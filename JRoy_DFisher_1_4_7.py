import PIL
import matplotlib.pyplot as plt
import os.path              
import PIL.ImageDraw 

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'Will Smith.jpg')

# Open and show the Will Smith image in a new Figure window
Will_Smith_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 3)
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
axes[2].imshow(Young_Channing_Tatum_img, interpolation='none')
fig.show()

axes[1].imshow(Oprah_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.show()

Oprah_file = os.path.join(directory, 'Oprah.jpg')
Oprah_img = PIL.Image.open(Oprah_file)
Oprah_small = Oprah_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(Oprah_img)
axes2[1].imshow(Oprah_small)
fig2.show()