from wand.image import Image
import os
import shutil


if os.path.exists("pdf_jpg"):
    print("pdf_jpg file exits, begin to delete it ")
    shutil.rmtree("pdf_jpg")
    print("generate new pdf_jpg file ")
    os.mkdir("pdf_jpg")
else:
    print("generate new pdf_jpg file ")
    os.mkdir("pdf_jpg")
print("begin to transform the edited pdf file to jpg file ")
page = input("please input page numbers of pdf ")
page = int(page)
for i in range(page):
    i = str(i)
    with Image(filename="edited.pdf"+"["+i+"]",resolution= 200) as img:
        img.compression_quality = 99
        img.save(filename="edited"+i+".jpg")
print("begin to transform the origin pdf file to jpg file ")
for i in range(page):
    i = str(i)
    with Image(filename="origin.pdf"+"["+i+"]",resolution= 200) as img:
        img.compression_quality = 99
        img.save(filename="origin"+i+".jpg")
print("begin to move jpg file ")
print('input as the root file name "C://Users//lixib//Desktop//Hiwi_job//Code//2018.04.23//pdf_jpg" ')
name = input("What is the root file of pdf_jpg ")
for i in range(page):
    shutil.move("edited"+str(i)+".jpg",name)
    shutil.move("origin"+str(i)+".jpg",name)
"C://Users//lixib//Desktop//Hiwi_job//Code//2018.04.23//pdf_jpg"


