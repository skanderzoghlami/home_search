# api_calls/views.py
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def make_api_calls(request):
    # Make a GET request to the desired URL
    url = "https://trouverunlogement.lescrous.fr/tools/31/search?bounds=4.8583622_45.7955875_4.9212614_45.7484524"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the specified HTML content
            target_text = "<h2 class=\"SearchResults-mobile svelte-8mr8g\">Aucun logement trouvÃ©</h2>"
            
            if target_text in str(soup):
                # The target text exists in the page
                data = {
                    "message": "Nothing available"
                }
            else:
                # The target text doesn't exist in the page
                data = {
                    "message": "Something is available!"
                }
            
            return JsonResponse(data)
        else:
            # Handle other status codes as needed
            data = {
                "message": "API call failed with status code: {}".format(response.status_code)
            }
            return JsonResponse(data, status=response.status_code)
    
    except requests.exceptions.RequestException as e:
        # Handle any exceptions that may occur during the request
        data = {
            "message": "API call failed with exception: {}".format(str(e))
        }
        return JsonResponse(data, status=500)