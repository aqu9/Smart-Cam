import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import methods
from textblob import TextBlob


def conv(text,iplang,oplang):
    blob=TextBlob(text)
    translation=blob.translate(to=oplang)
    # translated_text=methods.text(text,iplang,oplang)
    return translation

def language(lang):
    l=["ENGLISH","HINDI","PUNJABI"]
    if lang=="en":
        return l[0]
    elif lang=="hi":
        return l[1]
    else:
        return l[2]

# print(language("en"))

def grab(path,iplang,oplang):
	image,ext=methods.read_image_and_extension(path)
	orig=image.copy()
	gray=methods.gray_image(image)
	edges=methods.edge_detection(gray)
	target=methods.find_contor(edges)
	output=methods.draw_contor(orig,image,target)
	text,output_image_path,data=methods.extract_text_and_location(output,ext,iplang)
	max_len=max(len(x) for x in data)
	if max_len<12:
		text,output_image_path,data=methods.extract_text_and_location(gray,ext,iplang)
	output_text=methods.text(text,iplang,oplang)
	# output_text=0
	print(output_image_path)
	return text,output_image_path,output_text

def nothing():
	pass
def delete():
    print(os.listdir("static/uploads"))
    list_dir=os.listdir("static/uploads")
    for file in list_dir:
        filename=os.path.join("static/uploads",file)
        os.unlink(filename)
    print(os.listdir("static/uploads"))

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('home.html')

@app.route('/next', methods=("GET","POST"))
def next():
    if request.method=="POST":
        file=request.files["ipfile"]
        # language=["ENGLISH","HINDI","PUNJABI"]
        print(request.files)
        iplang=request.form["slct"]
        oplang=request.form["slct1"]
        ip=language(iplang)
        op=language(oplang)
        user_input=request.form["iptext"]
        print("filename is",file.filename,iplang,oplang,user_input)
        if file.filename=="" and user_input!="":
            optext=conv(user_input,iplang,oplang)
            image="noimage.png"
            return render_template('next.html',t=user_input,optext=optext,iplang=ip,oplang=op,filename=image)
        if file and allowed_file(file.filename):
            filename=secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            filepath=app.config['UPLOAD_FOLDER']+filename
            text,process_path,optext=grab(filepath,iplang,oplang)
            print(text,process_path)
            print('UPLOAD_IMAGE_FILENAME: '+filename)
            user_photo_path='uploads/'+filename
            return render_template('next.html',t=text,optext=optext,iplang=ip,oplang=op,filename=user_photo_path)
    else:
        return redirect(request.url)


if __name__ == "__main__":
    app.run()
