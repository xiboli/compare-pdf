# compare-pdf
This compare-pdf project is a small project which based on the requirement of our Institute.

In our Institute, we have different versions of scripts and those were editted by a lot of scientific Assistants. Then we need to find the difference between two script files and return the page number. In the beginning, this is a part of my work as a student assistant. Everytime I compare it artificially and it costs me too much times. Sometimes I even skip some small differences. This is so awful and I decide to use my python knowledge to solve this problem.

Python is a programming language, which is wildly used in computer vision, deep learning and web crawler. Because of its simplicity and the usability, this language is my favorite language and I also use it to write many small programs. Python has plenty of libraries including PIL, wand and numpy, which provides the posibility for me, to bulid a prototype of pdf-compare program. In the following I will introduce some libraries I have used and upload some links for each of you to download those libraries.

# coding environment

Integrated Developer Environments (IDEs): JetBrains PyCharm Edu 2018.1 x64

Third-party Libraries:

1. Wand 0.4.4
Installation Tutorial: ImageMagick on Windows

http://docs.wand-py.org/en/0.4.4/guide/install.html#install-imagemagick-on-windows

2. Version of ImageMagick

http://ftp.icm.edu.pl/packages/ImageMagick/binaries/

Windows 32-bit

ImageMagick-6.9.3-1-Q16-x86-dll.exe

Windows 64-bit

ImageMagick-6.9.3-1-Q16-x64-dll.exe

# Generation of executable file
When we finish our python program, we also need to generate an executable file to let others use our programs. During the compilation process I always meet an error：lib not found. Because I have use the library of scipy and my pyinstaller can always not find this library. So I solve it by following strings: pyinstaller -F --paths C:\Users\2018.04.23\venv\Lib\site-packages\scipy\extra-dll pdf_num_detect.py

# Algorithm of my program
The Algorithm of this project is very easy. Firstly we shoud take our pdf as jpg format. Every page can be cutted into a jpg format pictures. And we compare the RGB value of each pictures from A version to B version. If the RGB value between two versions is different, it means that this page was editted. We return our results in the cmd windows.
