from PIL import Image
from scipy.misc import fromimage

def getRGB(filename):
    im = Image.open(filename)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    data = fromimage(im)
    return [data,width,height]

def compare(pdf_original_RGB, pdf_edited_RGB):
    count = 0
    if (pdf_edited_RGB == pdf_original_RGB).all():
        count = count
    else:
        count = count +1
    return count

print('begin to compare the jpg files  ')
print('input as the root file name "C://2018.04.23//pdf_jpg" ')
name = input("What is the root file of pdf_jpg ")
page = input("please input page numbers of pdf ")
page = int(page)
for i in range(page):
    i = str(i)
    file1 = name + "//edited" + i + ".jpg"
    file2 = name + "//origin" + i + ".jpg"
    pdf_original_RGB = getRGB(file1)[0]
    pdf_edited_RGB = getRGB(file2)[0]
    value = compare(pdf_original_RGB, pdf_edited_RGB)
    if value > 0:
        print(value)
        print("edited"+i+".jpg is different from origin" + i + ".jpg")
    else:
        print("edited"+i+".jpg is normal")
input('type any thing to exit')
