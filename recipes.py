import spoonacular as sp
from config import api_key
api = sp.API("api_key")

def dish_search():
    q = input("Tell me what you want: ")
    response = api.search_recipes_complex(q)
    data = response.json()
    print(data)

def wine_description():
    q = input("Tell me what you drinking: ")
    try:
        response = api.get_wine_description(q)
        data = response.json()
        print(data)
    except Exception:
        print("Error")

def wine_paring():
    q = input("Tell me what you eating: ")
    try:
        response = api.get_wine_pairing(q)
        data = response.json()
        print(data['pairingText'])
        print(data['productMatches'][0]['title'])
        #print(data['productMatches']['title'])
        #print(data['productMatches']['description'])
        #print(data['productMatches']['link'])
    except Exception:
        print("Error")
        
#dish_search()
#wine_description()
wine_paring()
