'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'Oprah.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.show()
