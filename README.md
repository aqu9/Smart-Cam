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
1.  fla
