from PIL import Image,ImageFilter
import matplotlib.pyplot as plt

img=Image.open("Tom and Jerry.jpg")
plt.imshow(img)
plt.show()

converted_image=img.convert('LA')
plt.imshow(converted_image)
plt.show()

angles=[30,60,90,120,150]
rotate_images=[img.rotate(angle) for angle in angles]

for rotated_images in rotate_images:
 plt.imshow( rotated_images)
 plt.show()   

 base_img=Image.open("Tom and Jerry.jpg")
 paste_img=Image.open("scinshan.jpg")

plt.imshow(base_img)
plt.show()

plt.imshow(paste_img)
plt.show()

X=100
Y=100
base_img.paste(paste_imp,(x,y))
filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.EDGE_ENHANCE, ImageFilter.SHARPEN, ImageFilter.EMBOSS]
filter_names = ['Blur', 'Contour', 'Edge Enhance', 'Sharpen', 'Emboss']

fig,axs=plt.subplots(1,len(filters),figsize=(20,5))

for i,filt in enumerate(filters):
      filtered_img=img.filter(flit)
      axs[i].imshow(filtered_img)
      axs[i].set_title(filter_names[i])

plt.show()