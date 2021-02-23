# ShopID: ItemID, BuyPrice, SellPrice, ProduceQuanity; ItemID, BuyPrice, SellPrice, ProduceQuanity;

# print(dictionary.items()) #prints keys and values
# print(dictionary.keys()) #prints keys
# print(dictionary.values()) #prints values

import re
import json
import csv

# Regular expression patterns
regex_shop_id = re.compile('(\d+):')
regex_items = re.compile('(\d+),(\d+),(\d+),(\d+);')

# Open prices data file and split lines based on linebreaks, store in list
with open('prices.dat', 'r') as f:
    text = f.read()
shops = text.splitlines()

shops_dict = {}
item_dict = {}
# Comments go here
for i in range(len(shops)):
    shop_id = re.search(regex_shop_id, shops[i]).group(1)
    shop_inventory = re.findall(regex_items, shops[i])
    item_list = []
    # More comments here, maybe
    for item in shop_inventory:
        item_id = item[0]
        item_attributes_dict = {
            "BuyPrice": item[1],
            "SellPrice": item[2],
            "ProduceQuanity": item[3]
        }
        item_dict[item_id] = item_attributes_dict
    # Moral of the story: append COPIES of dictionaries, lest they overwrite originals
    item_list.append(item_dict.copy())
    shops_dict[shop_id] = item_list

with open('shops_dict.txt', 'w') as f:
    f.write(str(shops_dict))

# with open('prices.json', 'w') as f:
#     f.write(json.dumps(shops_dict))
# 
# with open('prices_preformatted.json', 'w') as f:
#     f.write(json.dumps(shops_dict, indent=4))