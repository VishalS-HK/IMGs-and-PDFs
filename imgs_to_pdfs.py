import os
import img2pdf

path = "" #path to the directory which contains the files

images = [imgs for imgs in os.listdir(path) if imgs.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

images.sort()

#list to store image bytes of images in directory
image_bytes = list()

#conveting all the images to image bytes and appending them to a list
for i in images:
    with open(os.path.join(path, i), 'rb') as im:
        image_bytes.append(im.read())

#to convert image bytes to pdf bytes
pdf_bytes = img2pdf.convert(image_bytes)

#consolidating pdf bytes to a pdf file
with open('Output.pdf', 'wb') as pdfFile:
    pdfFile.write(pdf_bytes)