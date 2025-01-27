import requests
import urllib.request
from datetime import date

#  Getting a random image from Dog API and saved it.


def DogApi() -> str:
    #  Get a random dog image from the API
    url = "https://dog.ceo/api/breeds/image/random"
    json_data = requests.get(url).json()
    Final_result = json_data['message']
    return (Final_result)


def Download_API_img():

    url = DogApi()
    #  This is for the name of the downloaded image
    name = str(date.today()) + url[42:]
    image_url = url
    save_as = name
    download_image(image_url, save_as)
    print("Image saved successfully", name)


def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)


Download_API_img()
