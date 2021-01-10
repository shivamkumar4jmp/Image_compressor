import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename() #Where Your Image is
img = PIL.Image.open(file_path) 

height , width = img.size

img = img.resize((height,width), PIL.Image.ANTIALIAS) #Taking Same Height And Width
save_path = asksaveasfilename() #saving path

img.save(save_path+"_compressed.JPG")
