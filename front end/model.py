# Importing required libs
import numpy as np
from PIL import Image
from flask import Flask, render_template
import os

 
 
# Preparing and pre-processing the image
def preprocess_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224, 224))
    return img_resize
 
 
# Predicting function
def predict_result(predict):
    full_filename = "/Users/molly/Desktop/fridgeFront/maxresdefault.jpg"
    return full_filename
    return render_template("index.html", user_image = full_filename)
