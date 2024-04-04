from flask import Flask, render_template, request
import os
from model import preprocess_img, predict_result


app = Flask(__name__)
PHOTO_FOLDER = os.path.join('static', 'photo')
app.config['UPLOAD_FOLDER'] = PHOTO_FOLDER

 
@app.route('/')
def main():
    return render_template("index.html")

def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/result')
def show_result():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'maxresdefault.jpg')
    return render_template("output.html", user_image = full_filename)

# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            img = predict_result(request.files['file'].stream)
            return render_template("result.html", predictions=img)
 
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
