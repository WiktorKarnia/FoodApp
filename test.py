from __future__ import print_function
import time
import spoonacular

from pprint import pprint
configuration = spoonacular.Configuration()
# Configure API key authorization: apiKeyScheme
configuration.api_key['91d7f957e7f0445f8c8f1fd554afbc51'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# create an instance of the API class
api_instance = spoonacular.WineApi(spoonacular.ApiClient(configuration))
food = 'steak' # str | The food to get a pairing for. This can be a dish (\"steak\"), an ingredient (\"salmon\"), or a cuisine (\"italian\").
max_price = 50 # float | The maximum price for the specific wine recommendation in USD. (optional)

try:
    # Wine Pairing
    api_response = api_instance.get_wine_pairing(food, max_price=max_price)
    pprint(api_response)
except Exception as e:
    print("Exception when calling WineApi->get_wine_pairing: %s\n" % e)