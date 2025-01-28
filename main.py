# sa salvam niste imagini cu niste caini intr-un dpf
import json
import os
from json import JSONDecodeError
import time
import requests
import pdf_functions as pdf
import image_functions

MENU = """
1. Save Random Image
2. Show all images
3. Save images to pdf
4. Delete all images
5. Exit
Type your choice: """


def read_config(path: str = "config.json") -> dict:
    try:
        with open(path, "r") as f:
            data = f.read()
            conf_dict = json.loads(data)
    except FileNotFoundError as e:
        print(f"The config file is missing..{e}")
    except JSONDecodeError as e:
        print(f"Watch your JSON..{e}")
    except Exception as e:
        print(f"Unknwon exception: {e}")

    return conf_dict



if __name__ == '__main__':
    config = read_config()

    while True:
        user_pick = input(MENU)
        match user_pick:
            case "1":
                random_image_dict = image_functions.get_dog_image(config['url_dog_images'])
                content = image_functions.download_dog_image(random_image_dict['message'])
                image_functions.save_dog_image(content)
            case "2":
                image_functions.show_all_images()
            case "3":
                pdf.create_pdf("test.pdf")
            case "4":
                pass
            case "5":
                exit(0)



