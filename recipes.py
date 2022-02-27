import spoonacular as sp
api = sp.API("api_key")

def dish_search():
    q = input("Tell me what you want: ")
    response = api.search_recipes_complex(q)
    data = response.json()
    print(data)

def wine_paring():
    q = input("Tell me what you drinking: ")
    try:
        response = api.get_wine_description(q)
        data = response.json()
        print(data)
    except Exception:
        print("Error")

dish_search()
#wine_paring()
