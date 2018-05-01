from PIL import Image
from scipy.misc import fromimage

def getRGB(filename):
    im = Image.open(filename)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    data = fromimage(im)
    return [data,width,height]

def compare(pdf_original_RGB,pdf_edited_RGB,pdf_witdth,pdf_height):
    count = 0;
    C = (pdf_edited_RGB == pdf_original_RGB).all()
    if (pdf_edited_RGB == pdf_original_RGB).all():
        count = count;
    else:
        count = count +1;
    return count

for i in range(19):
    i = str(i)
    file1 = "edited"+i+".jpg"
    file2 = "origin"+i+".jpg"
    pdf_original_RGB = getRGB(file1)[0]
    pdf_edited_RGB = getRGB(file2)[0]
    pdf_width = 1654
    pdf_height = 2339
    value = compare(pdf_original_RGB,pdf_edited_RGB,pdf_width,pdf_height)
    if value > 0:
        print(value)
        print("edited"+i+".jpg is different from origin" +i+".jpg")
    else:
        print("edited"+i+".jpg is normal")
input()

