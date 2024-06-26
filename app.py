from flask import Flask, render_template, request, session, url_for, redirect
import os
from backend.model import preprocess_img, predict_result, predict_photo, convert_spooled_tempfile_to_image
from backend.cookbook import reciepesbyId, findRecipes
from backend.parse_recipes import parse_recipe
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
PHOTO_FOLDER = os.path.join('static', 'photo')
app.config['UPLOAD_FOLDER'] = PHOTO_FOLDER
logo_path = os.path.join(app.root_path, PHOTO_FOLDER, "lenswhite.png")
logo = Image.open(logo_path)
model_file_path = os.path.join(app.root_path, "models", "yolov8s.pt")

 ## ok so this one has like uhhhh the photo upload stuff
@app.route('/')
def main():
    return render_template("upload.html")


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
    debug = False
    try:
        if request.method == 'POST':
            print(app.config['UPLOAD_FOLDER'])
            print(PHOTO_FOLDER)
            file = request.files['file']
            if file.filename != '':
                filename = secure_filename(file.filename)
                path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], "new.jpg")
                file.save(path)
                print(path)

            ingredients = predict_photo(path, model_file_path)

            if (debug):
                recipes = sample_recipes
            else:
                recipes = findRecipes(ingredients)
                print(recipes)
            ##ingredients_words = ingredients.split(",")
            title1, photo1, description1, title2, photo2, description2, title3, photo3, description3 = parse_recipe(recipes)

            return render_template("index.html", title1=title1, photo1=photo1, description1=description1, title2=title2, photo2=photo2, description2=description2, title3=title3, photo3=photo3, description3=description3)

    except:
        error = "File cannot be processed."
        return render_template("result.html", err=error)

@app.route('/testcss')
def show():
    recipes = sample_recipes
    title1, photo1, description1, title2, photo2, description2, title3, photo3, description3 = parse_recipe(recipes)

    return render_template("index.html", logo=logo_path, title1=title1, photo1=photo1, description1=description1, title2=title2, photo2=photo2, description2=description2, title3=title3, photo3=photo3, description3=description3)



@app.route('/result')
def show_result():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'junketpudding.jpg')
    return render_template("render_image.html", user_image = full_filename)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

sample_recipes = [[716245,"Avocado Egg Salad","https://img.spoonacular.com/recipes/716245-312x231.jpg",["Boil your eggs and immerse in water to cool.Peel your avocado and mash in a bowl.Squirt your lemon over the avocado.Peel the eggs, chop and mix with the avocado.","Mix the black pepper, seasoning and scotch bonnet pepper and set aside.Toast your bread and roll out with a rolling pin, cut the edges off and serve the avocado egg salad on the bread."]],[664328,"Vanilla Pears With Ginger Ice Cream","https://img.spoonacular.com/recipes/664328-312x231.jpg",["Whisk the eggs and sugar together in a large bowl.In another bowl whip the cream until soft peaks form","Fold the whipped cream into the egg and sugar mixture.","Add the chopped ginger and ginger syrup and gently combine.","Pour into a suitable freezer container and freeze for 24 hours.Gently stir the ice cream after approx 2 hours to ensure even distribution of the ginger pieces. Repeat this process after a further 1 hour freezing time","When the ice cream is ready remove from the freezer and allow to soften slightly.To serve:-","Drizzle chocolate sauce in a zig zag over the serving plate.Slice the pears thinly and gently arrange in a fan shape on the plate","Place two quenelles of ice cream next to the fanned pears and then lightly dust with icing sugar. Decorate with a few pieces of chopped ginger"]],[644650,"Ginger Sweet Potato Casserole","https://img.spoonacular.com/recipes/644650-312x231.jpg",["Boil sweet potatoes with skins on until tender, 15-18 minutes. Peel and mash.","While potatoes are cooking, heat cream, add tea bags and remove from heat.","Let steep for 5 minutes.","To the mashed potatoes, add salt, butter, egg, tea infused cream. Beat until smooth.","Place in 2 quart buttered baking dish, (sprinkle with marshmallows if desired) and bake in oven at 375 for 15-20 minutes or until heated through (and marshmallows are browned*).","Serve hot.","* If made ahead, bring to room temperature, heat for 25 minutes.  Top with marshmallows, if desired, and bake another 10 minutes or until marshmallows are browned."]]]