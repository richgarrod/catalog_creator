import unicodedata
import wand.image
from wand.color import Color
import os
from fpdf import FPDF
from pdfrw import PageMerge, PdfReader, PdfWriter

# Requiredments:
# 1. Each directory is format <nameOfStyle>_<Material>
# 2. logo.jpg exists next to the python file
# 3. Each show is named <nameOfStyle>_<nameOfShoe>
# 4. Images are jpgs

# Helper functions for dealing with names

def get_style_name(n):
    return im[:-3].replace("_trimmed.", "").split("_")[1].capitalize()

def get_image_count():
    files = os.listdir()
    print(files)
    count = 0
    for f in files:
        if "trimmed" in f and f[-3:] == 'jpg':
            count += 1
    print(count)
    return count

# Create the main PDF

pdf = FPDF()

# For each directory/style
directories = []
for p in os.listdir():
    if os.path.isdir(p):
        directories.append(p)

for directory in directories:
    print("Moving into: ", directory)
    os.chdir(directory)
    # Create the trimmed files
    files = os.listdir()
    print("changing files")
    for im in files:
        print(im)
        if "trimmed" not in im and im[-3:]=="jpg" and im[:-4]+"_trimmed.jpg" not in files and 'logo' not in im.lower():
            # Fuzz of 30,000 seems to trim shoes nicely
            with wand.image.Image(filename=im) as w:
                w.trim(fuzz=30000)
                w.save(filename=im[:-4]+"_trimmed.jpg")

    print("Finished transforming files")

    # Create the PDF page
    pdf.add_page(orientation='L')
    # Add the title
    pdf.set_font('Arial', 'B', 36)
    pdf.text(10, 20, directory.split("_")[0])
    # Add material under the title
    pdf.set_font('Arial', '', 24)
    pdf.text(10, 30, directory.split("_")[1])

    # Set font for the smaller style titles
    pdf.set_font('Arial', '', 16)

    # Standard Sizes
    mainImageSize = 120
    smallImageWidth=70
    smallImageOffset=95
    smallImageTopOffset=150

    # Style of pag for one image
    if get_image_count() == 1:
        for im in os.listdir():
            if im[-3:]=="jpg" and "trimmed" in im:
                pdf.image(im, 40, 55, 220, 0)
                pdf.text(10, 50, get_style_name(im))

    # Style of page for two images
    elif get_image_count() == 2:
        iterator=0
        for im in os.listdir():
            if im[-3:]=="jpg" and "trimmed" in im:
                if iterator == 0:
                    pdf.image(im, 10, 85, 160, 0)
                    pdf.text(10, 85, get_style_name(im))
                    iterator += 1
                elif iterator == 1:
                    pdf.image(im, 140, 60, 110, 0)
                    pdf.text(140, 55, get_style_name(im))
                    iterator += 1
                else:
                    continue

    # Style of page for three images
    elif get_image_count() == 3:
        iterator=0
        smallImageWidthThreeLayout=80
        smallImageOffsetThreeLayout=130
        smallImageTopOffsetThreeLayout=140
        for im in os.listdir():
            print(im)
            if im[-3:]=="jpg" and "trimmed" in im:
                if iterator == 0:
                    pdf.image(im, 10, 55, mainImageSize, 0)
                    pdf.text(10, 50, get_style_name(im))
                    iterator += 1
                elif iterator == 1:
                    pdf.image(im, 170, 55, smallImageWidthThreeLayout, 0)
                    pdf.text(170, 50, get_style_name(im))
                    iterator += 1
                elif iterator == 2:
                    pdf.image(im, 170, 130, smallImageWidthThreeLayout, 0)
                    pdf.text(170, 125, get_style_name(im))
                    iterator += 1
                else:
                    continue

    # Style of page for four images
    elif get_image_count() == 4:
        iterator=0
        for im in os.listdir():
            print(im)
            if im[-3:]=="jpg" and "trimmed" in im:
                if iterator == 0:
                    pdf.image(im, 10, 55, mainImageSize, 0)
                    pdf.text(10, 50, get_style_name(im))
                    iterator += 1
                elif iterator == 1:
                    pdf.image(im, 10, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 2:
                    pdf.image(im, 10+smallImageOffset*1, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*1, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 3:
                    pdf.image(im, 10+smallImageOffset*2, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*2, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                else:
                    continue

    # Style of page for five images
    elif get_image_count() == 5:
        iterator=0
        for im in os.listdir():
            print(im)
            if im[-3:]=="jpg" and "trimmed" in im:
                if iterator == 0:
                    pdf.image(im, 10, 55, mainImageSize, 0)
                    pdf.text(10, 50, get_style_name(im))
                    iterator += 1
                elif iterator == 1:
                    pdf.image(im, 10, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 2:
                    pdf.image(im, 10+smallImageOffset*1, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*1, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 3:
                    pdf.image(im, 10+smallImageOffset*2, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*2, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 4:
                    pdf.image(im, 10+smallImageOffset*2, smallImageTopOffset-60, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*2, smallImageTopOffset-65, get_style_name(im))
                    iterator += 1
                else:
                    continue

    # Style of page for six images
    elif get_image_count() == 6:
        iterator=0
        for im in os.listdir():
            print(im)
            if im[-3:]=="jpg" and "trimmed" in im:
                if iterator == 0:
                    pdf.image(im, 10, 55, mainImageSize, 0)
                    pdf.text(10, 50, get_style_name(im))
                    iterator += 1
                elif iterator == 1:
                    pdf.image(im, 10, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 2:
                    pdf.image(im, 10+smallImageOffset*1, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*1, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 3:
                    pdf.image(im, 10+smallImageOffset*2, smallImageTopOffset, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*2, smallImageTopOffset-5, get_style_name(im))
                    iterator += 1
                elif iterator == 4:
                    pdf.image(im, 10+smallImageOffset*2, smallImageTopOffset-60, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*2, smallImageTopOffset-65, get_style_name(im))
                    iterator += 1
                elif iterator == 5:
                    pdf.image(im, 10+smallImageOffset*2, smallImageTopOffset-120, smallImageWidth, 0)
                    pdf.text(10+smallImageOffset*2, smallImageTopOffset-125, get_style_name(im))
                    iterator += 1
                else:
                    continue

    pdf.image("../logo.jpg", 245, 5, 50, 0)

    print("Finished creating pdf")

    # Save the image
    os.chdir("..")

pdf.output("newpdf.pdf")


