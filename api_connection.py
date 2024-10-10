from osrsbox import items_api
import json
import requests
from PIL import Image
from io import BytesIO

BASE_URL = "http://services.runescape.com/m=itemdb_oldschool"

class APIConnection():
    def __init__(self):
        self.items = self.read_items_from_json()


    def read_items_from_json(self):
        with open("resources/items.json") as json_file:
            return json.loads(json_file.read())



    #Only run when need to - json is saved
    def load_items_to_json(self):
        item_dict = {}
        items = items_api.load()
        for item in items:
            if not item.tradeable_on_ge:
                continue
            item_dict[item.name] = item.id

        with open("resources/items.json", "w") as outfile:
            json.dump(item_dict, outfile)



    def get_item_icon(self, item_id):
        response = requests.get(BASE_URL + "/api/catalogue/detail.json?item=" + str(item_id))
        if response.status_code == 200:
            data = response.json()

            img_response = requests.get(data['item']['icon'])
            img = Image.open(BytesIO(img_response.content))
            if img_response.status_code == 200:
                return img


    def get_item_id(self, item_name):
        return self.items[item_name]