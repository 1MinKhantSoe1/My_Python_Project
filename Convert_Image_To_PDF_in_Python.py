import img2pdf
from PIL import Image

img_path = "bd.jpg"  # storing image location

pdf_path = "bd.pdf"  # storing pdf location

image = Image.open(img_path)  # opening image
pdf_bytes = img2pdf.convert(image.filename)  # converting into chunks using img2pdf

file = open(pdf_path, "wb")  # opening or creating pdf file
file.write(pdf_bytes)  # writing pdf files with chunks

image.close()  # closing image file
file.close()  # closing pdf file

print("Successfully convert to pdf file")
