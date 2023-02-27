# importing required modules
from PyPDF2 import PdfReader
from PIL import Image, ImageDraw, ImageFont
import os

# creating a pdf reader object
reader = PdfReader(r"C:\Users\bardr\Downloads\Session_2 (1).pdf")

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[0]

# extracting text from page
text = page.extract_text()

# Create an image object
width, height = int(8.27 * 200), int(11.7 * 200)  # A4 at 200dpi
image = Image.new(mode='RGB', size=(width, height), color='white')

# Specify the font file path
# you need to download a font first at: https://www.dafont.com/theme.php?cat=603
font_path = r"C:\Users\bardr\Downloads\simple_handmade_2\SimpleHandmade.ttf"

# Set the font size
font_size = 30

# Load the font
font = ImageFont.truetype(font_path, font_size)

# Create a draw object
draw = ImageDraw.Draw(image)

# Set the starting position for the text
x = 50
y = 50

# Write the text to the image using the custom font
draw.text((x, y), text, font=font, fill='black')

# Save the image as a JPEG file
image_file = 'handwritten.jpg'
image.save(image_file)

# Convert the image to PDF using PIL
pdf_file = 'handwritten.pdf'
image_pdf = Image.open(image_file)
image_pdf.save(pdf_file)

# Remove the temporary JPEG image file
os.remove(image_file)

# Open the PDF file
os.startfile(pdf_file)
