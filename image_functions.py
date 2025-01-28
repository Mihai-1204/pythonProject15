import json

import cv2
import requests
from json import JSONDecodeError
import os
import time




def get_dog_image(url: str) -> dict:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            #print(response.text)
            data = json.loads(response.text)
            return data
        else:
            raise Exception("Status code is not 200, therefore the api didn't work")
    except Exception as e:
        print(f"Something wrent wrong with the api. {e}"
              f"{response.status_code}"
              f"{response.text}")


def download_dog_image(url: str):
    try:
        response = requests.get(url)
        return response.content
    except Exception as e:
        print(e)


def save_dog_image(content: bytes, path: str = "images"):
    os.makedirs("images", exist_ok=True)
    timestamp = int(time.time())

    with open(f"./{path}/dog_image_{timestamp}.png", "wb") as f:
        f.write(content)


def show_all_images(path: str = "images"):
    images_list = os.listdir(path)

    for image in images_list:
        image_content = cv2.imread(f"./{path}/{image}")
        cv2.imshow(image, image_content)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


