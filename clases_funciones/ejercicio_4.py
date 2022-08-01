recipes = [
    {'recipe': 'Arroz con Verduras', 'ingredients': ['arroz', 'cebolla', 'morron', 'zanahoria', 'castañas', 'zuchini']},
    {'recipe': 'Ensalada de Quinoa',
     'ingredients': ['quinoa', 'huevo', 'cebolla morada', 'tomate', 'morron', 'almendras']},
    {'recipe': 'Carne al Horno', 'ingredients': ['colita', 'papa', 'zanahoria', 'batata', 'cebolla', 'ajo']},
    {'recipe': 'Fideos al Pesto', 'ingredients': ['fideos', 'queso', 'nueces', 'albahaca', 'ajo', 'aceite de oliva']},
    {'recipe': 'Guiso de Lentejas',
     'ingredients': ['lentejas', 'cebolla', 'zanahoria', 'papa', 'carne', 'puerro', 'morron']},
]

ingredients = []


def recipe_recommender():
    recommend_recipes = []

    for input_ingredient in ingredients:
        for recipe_dict in recipes:
            for recipe_ingredients in recipe_dict['ingredients']:
                if recipe_ingredients == input_ingredient:
                    if not (recipe_dict in recommend_recipes):
                        recommend_recipes.append(recipe_dict)

    return recommend_recipes


def print_recipes(recipe_reco):
    for recipe in recipe_reco:
        print(f"\nReceta: {recipe['recipe']}")
        for ingredient in recipe['ingredients']:
            print(f"\t* {ingredient}")


def main_menu():
    print("\n0000000000000000")
    print("¿Que cocino hoy?")
    print("0000000000000000\n")

    while True:
        print("(1) - Agregar ingrediente")
        print("(2) - Buscar receta")
        print("(3) - A cocinar...")

        option = input(">> ")

        if option == "1":
            ingredient = input("\tIngrediente: ")
            ingredients.append(ingredient)

        elif option == "2":
            if len(ingredients) >= 2:
                recipe_reco = recipe_recommender()
                print_recipes(recipe_reco)
            else:
                print("Debes ingresar al menos 2 ingredientes")

        elif option == "3":
            break

        else:
            print("Opcion invalida")


main_menu()
