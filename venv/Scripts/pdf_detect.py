from PIL import Image

def getRGB(filename):
    im = Image.open(filename)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x,y))
            rgb = (r, g, b)
            array.append(rgb)
    return [array,width,height]

def compare(pdf_original_RGB,pdf_edited_RGB,pdf_witdth,pdf_height):
    count = 0;
    for x in range(pdf_width*pdf_height):
        if pdf_edited_RGB[x] == pdf_original_RGB[x]:
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
    #pdf_width = getRGB(file1)[1]
    #pdf_height = getRGB(file1)[2]
    pdf_width = 1654
    pdf_height = 2339
    value = compare(pdf_original_RGB,pdf_edited_RGB,pdf_width,pdf_height)
    if value > 0:
        print(str(value)+"\n")
        print("edited"+i+".jpg is different from origin" +i+".jpg")
    else:
        print("edited"+i+".jpg is normal")
input()
