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
def predict_result(image):
    predictions = ["egg", "marshmallows", "dirt", "pears"]
    return predictions
    ## PUT ACTUAL CODE HERE TO ACTUALLY PREDICT

