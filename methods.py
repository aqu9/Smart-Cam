#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pytesseract
import time
from textblob import TextBlob
# import os


# In[27]:


def resize_image(image,width,height):
    image=cv2.resize(image,(width,height))
    return image

def gray_image(image):
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return image

def edge_detection(image):
    blurred_image=cv2.GaussianBlur(image,(5,5),0)
    edge=cv2.Canny(blurred_image,0,50)
    return edge

def find_contor(image):
    (contors,_)=cv2.findContours(image,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    contors=sorted(contors, key=cv2.contourArea,reverse=True)
    for i in contors:
        p=cv2.arcLength(i,True)
        approx=cv2.approxPolyDP(i,0.02*p,True)
        if len(approx)==4:
            target=approx
            break
    return target

def rectify(h):
    h=h.reshape((4,2))
    hnew=np.zeros((4,2),dtype=np.float32)
    add=h.sum(1)
    hnew[0]=h[np.argmin(add)]
    hnew[2]=h[np.argmax(add)]
    
    diff=np.diff(h,axis=1)
    hnew[1]=h[np.argmin(diff)]
    hnew[3]=h[np.argmax(diff)]
    
    return hnew

def draw_contor(orig_image,image,target):
    approx=rectify(target)
    pts2=np.float32([[0,0],[800,0],[800,800],[0,800]])
    
    M=cv2.getPerspectiveTransform(approx,pts2)
    result=cv2.warpPerspective(image,M,(800,800))
    
    cv2.drawContours(image,[target],-1,(0,255,0),2)
    result=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    return result

def extract_text_and_location(image,ext,iplang):
    if iplang=="en":
        s="eng"
    elif iplang=="hi":
        s="hin"
    else:
        s="pan"
    hImg,WImg=image.shape
    data=pytesseract.image_to_data(image,lang=s)
    st=""
    blank=[]
    for x,b in enumerate(data.splitlines()):
        if x!=0:
            b=b.split()
            # print(b)
            blank.append(b)
            if len(b)==12:
                x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(image,(x,y),(w+x,h+y),(0,0,255),2)
                st=st+b[11]+" "
                cv2.putText(image,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                # print(b[11])
    dir="static/uploads/"
    processed_image=time.strftime("%d%m%Y_%H%M%S")+"."+ext
    cv2.imwrite(dir+processed_image,image)
    # print(str)
    return st,processed_image,blank

def text(eng_test,from_lang,to_lang):
    # translator= Translator(from_lang=from_lang,to_lang=to_lang)
    # translation = translator.translate(eng_test)
    blob=TextBlob(eng_test)
    translation=blob.translate(to=to_lang)
#   print(translation)
    # return translator
    # s=str(eng_test)
    # print(s)
    # translator=Translator()
    # translated_sentence=translator.translate(s,src='en',dest='hindi')
    # output_text=translated_sentence.text
    return translation
# print(text("hello","en","hi"))


def read_image_and_extension(path):
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    image=cv2.imread(path)
    ext=path[-3:]
    if ext in ALLOWED_EXTENSIONS:
        pass
    else:
        ext="jpeg"
    return image,ext

    

# In[ ]:




