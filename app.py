from flask import Flask, render_template, request, session, url_for, redirect
import os
from backend.model import preprocess_img, predict_result
from backend.cookbook import reciepesbyId, findRecipes



app = Flask(__name__)
PHOTO_FOLDER = os.path.join('static', 'photo')
app.config['UPLOAD_FOLDER'] = PHOTO_FOLDER

 
 ## ok so this one has like uhhhh the photo upload stuff
@app.route('/')
def main():
    return render_template("index.html")


@app.route('/text_entry')
def what():
    ## this is fucking janky
    if (request.args.get('recipetext')):
        ingredients = request.args.get('recipetext')
        ingredients_words = ingredients.split(",")
        recipes = findRecipes(ingredients_words)
        return recipes

    else:
        return render_template("textinput.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    try:
        if request.method == 'POST':
            ##processed = preprocess_img(request.files['file'].stream)
            ingredients = predict_result("aaa")
            ##ingredients_words = ingredients.split(",")
            recipes = findRecipes(ingredients)
            return recipes
            return render_template("result.html", predictions=recipes)
 
    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)



@app.route('/result')
def show_result():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'junketpudding.jpg')
    return render_template("output.html", user_image = full_filename)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
