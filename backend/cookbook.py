import requests

def reciepesbyId(id):
    baseString = 'https://api.spoonacular.com/recipes/'+str(id)+'/analyzedInstructions?apiKey=79001ad4da024048843e722ecdb550ef'
    
    APIresponse = requests.get(baseString).json()
    APIresponse = APIresponse[0]["steps"]

    instructions = []
    for step in APIresponse:
        instructions.append(step['step'])
    
    return instructions
    
def findRecipes(ingredients):
    baseString = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients='

    for ingredient in ingredients:
        baseString += ingredient +',+'
    
    baseString = baseString[:-2] + '&number=3&apiKey=79001ad4da024048843e722ecdb550ef'

    APIresponse = requests.get(baseString).json()

    dishOptions = []

    for dish in APIresponse:
        instructions = reciepesbyId(dish['id'])
        dishOptions.append((dish['id'], dish['title'], dish['image'], instructions))

    return dishOptions

##print(findRecipes(['apples', 'flour', 'vanilla', 'sugar']))

