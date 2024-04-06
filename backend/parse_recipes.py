
def parse_recipe(recipe):
    parsed_data = []

    title1 = recipe[0][1]
    photo1 = recipe[0][2]
    description1 = "\n   ".join(recipe[0][3])
    title2 = recipe[1][1]
    photo2 = recipe[1][2]
    description2 = "\n   ".join(recipe[1][3])
    title3 = recipe[2][1]
    photo3 = recipe[2][2]
    print(recipe[2][3])
    description3 = "\n\n".join(recipe[2][3])
    print(description3)

    return title1, photo1, description1, title2, photo2, description2, title3, photo3, description3

