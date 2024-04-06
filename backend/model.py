# Importing required libs
import numpy as np
from PIL import Image
from flask import Flask, render_template
import os
from inference_sdk import InferenceHTTPClient
from ultralytics import YOLO

model_path = 

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="VElRvTezwWYSf6MhxsKq"
)
 
# Predicting function
def predict_result(image):
    predictions = ["egg", "marshmallows", "dirt", "pears"]
    return predictions
    ## PUT ACTUAL CODE HERE TO ACTUALLY PREDICT


def convert_spooled_tempfile_to_image(spooled_tempfile):
    # Rewind the file pointer to the beginning
    spooled_tempfile.seek(0)
    
    # Open the spooled tempfile as an image
    image = Image.open(spooled_tempfile)
    
    return image

def preprocess_img(op_img):
    print("aaa")
    img_resize = op_img.resize((224, 224))
    return img_resize

def predict_photo(img_path, model_path):
    
  model = YOLO(model_path)  # pretrained 
  # Run batched inference on a list of images
  results = model.predict(img_path, conf = 0.3)  # return a list of Results objects
  l = [model.names[int(c)] for r in results for c in r.boxes.cls]
  return l
    
# def predict_photo(photo):

#     result = CLIENT.infer(photo, model_id="aicook-lcv4d/3")
#     print(result)
#     classes = [prediction['class'] for prediction in result['predictions']]
#     print(classes)
#     print(set(classes))
#     return set(classes)

