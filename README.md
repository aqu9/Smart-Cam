# Smart-Cam

In this repository we extract text from image using tessaract-ocr and pytesseract and translate text into other language using textblob. and make a web app using flask.

## How We extract text
1.  convert image to grayscale.
2.  Detect edges of images.
3.  Find contour of image(region were text are present)
4.  Extract text region from image
5.  From extracted region we get image data using pytesseract.

## How we translate text
To transalate text we first we use text blob module it's auto detect input language of text and translate it into desired language in this repo we translate text into three language.
English,Hindi,Punjabi

## Requirement
Here we use ubuntu 20.04 focal fossa
To run this repo on your system you need to download some required module

### 1.  tesseract-ocr

## In Ubuntu
sudo apt install tesseract-ocr

## In Windows
you need to download treeseract ocr from

https://github.com/UB-Mannheim/tesseract/wiki

And add this line in **methods.py** 

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

2.  pytesseract
3.  opencv
4.  textblob
5.  numpy
6.  flask
7.  wekzeug
8.  urllib
9.  os
10. time

# FLASK WEBPAGE OUTPUT

![Screenshot from 2020-12-02 22-22-41](https://user-images.githubusercontent.com/67313757/101056057-94afd680-35b0-11eb-91c0-68aadcee8ba0.png)

![Screenshot from 2020-12-02 22-40-26](https://user-images.githubusercontent.com/67313757/101056155-b01ae180-35b0-11eb-95b8-ee51e2109996.png)

![Screenshot from 2020-12-02 22-40-49](https://user-images.githubusercontent.com/67313757/101056125-a7c2a680-35b0-11eb-9326-20ef7a186f14.png)

![Screenshot from 2020-12-02 22-46-11](https://user-images.githubusercontent.com/67313757/101057097-ae055280-35b1-11eb-9565-c277960ce63d.png)

![Screenshot from 2020-12-02 22-46-22](https://user-images.githubusercontent.com/67313757/101056340-e193ad00-35b0-11eb-8a97-f26b651fc9bd.png)

![Screenshot from 2020-12-02 22-46-55](https://user-images.githubusercontent.com/67313757/101056311-db053580-35b0-11eb-8b23-9002125f7518.png)
