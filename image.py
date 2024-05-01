from PIL import Image,ImageFilter
import matplotlib.pyplot as plt

img=Image.open("Tom and Jerry.jpg")
plt.imshow(img)  
plt.show()

#convert from RGBA to gray scale 
converted_img =img.convert('LA')
plt.imshow(converted_img)
plt.show()

#rotate image into 5 angles
angles = [30, 60, 90, 120, 150]
rotate_images = [img.rotate(angle) for angle in angles]

# Display the rotated images
for rotated_image in rotate_images:
    plt.imshow(rotated_image)
    plt.show()


# Open the images
base_img = Image.open("Tom and Jerry.jpg")
paste_img = Image.open("scinshan.jpg")

# Display the base image
plt.imshow(base_img)
plt.show()

# Display the paste image
plt.imshow(paste_img)
plt.show()

# Paste the paste image onto the base image at coordinates (x, y)
x = 100  # Adjust as needed 
y = 100  # Adjust as needed
base_img.paste(paste_img, (x, y))

# Display the result
plt.imshow(base_img)
plt.show()

# Apply five different filters to the image
filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.EDGE_ENHANCE, ImageFilter.SHARPEN, ImageFilter.EMBOSS]
filter_names = ['Blur', 'Contour', 'Edge Enhance', 'Sharpen', 'Emboss']

fig, axs = plt.subplots(1, len(filters), figsize=(20, 5))
for i, filt in enumerate(filters):
    filtered_img = img.filter(filt)
    axs[i].imshow(filtered_img)
    axs[i].set_title(filter_names[i])


plt.show()