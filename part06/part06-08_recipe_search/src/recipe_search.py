from collections import defaultdict

def initialize_dict(filename):
    recipe_to_time = defaultdict(int)
    recipe_to_ingredients = defaultdict(list[str])
    with open(filename) as file:
        for line in file:
            line = line.strip()
            recipe_to_time[line] = int(file.readline().strip())
            while True:
                ingredient = file.readline().strip()
                if not ingredient:
                    break
                recipe_to_ingredients[line].append(ingredient)
    return recipe_to_time, recipe_to_ingredients

def search_by_name(filename, word):
    recipe_to_time, recipe_to_ingredients = initialize_dict(filename)
    return [recipe for recipe in recipe_to_time
            if word in recipe.lower()
            ]

def search_by_time(filename, prep_time):
    recipe_to_time, recipe_to_ingredients = initialize_dict(filename)
    return [f"{recipe}, preparation time {time} min"
            for recipe, time in recipe_to_time.items()
            if time <= prep_time
            ]

def search_by_ingredient(filename, ingredient):
    recipe_to_time, recipe_to_ingredients = initialize_dict(filename)
    ingredient = ingredient.lower().strip()
    return [f"{recipe}, preparation time {time} min"
            for recipe, time in recipe_to_time.items()
            for recipe_ingredient in recipe_to_ingredients[recipe]
            if ingredient in recipe_ingredient
            ]

if __name__ == '__main__':
    recipe_to_time, recipe_to_ingredients = initialize_dict("recipes1.txt")
    print(recipe_to_time)
    print(recipe_to_ingredients)
    print()

    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    print()

    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)

    print()

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)
