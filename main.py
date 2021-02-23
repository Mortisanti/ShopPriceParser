# ShopID: ItemID, BuyPrice, SellPrice, ProduceQuanity; ItemID, BuyPrice, SellPrice, ProduceQuanity;

# print(dictionary.items()) #prints keys and values
# print(dictionary.keys()) #prints keys
# print(dictionary.values()) #prints values

#TODO Create json files in separate directory, compress said directory to 7z archive

import re
# import json
# import py7zr

# Regular expression patterns
regex_shop_id = re.compile('(\d+):')
regex_items = re.compile('(\d+),(\d+),(\d+),(\d+);')

# Open prices data file and split lines based on linebreaks, store in list
with open('prices.dat', 'r') as f:
    text = f.read()
shops = text.splitlines()


item_attributes_dict = {}
indiv_item_dict = {}
inventory_dict = {}
shops_dict = {}
main_dict = {}

for i in range(len(shops)):
    shop_id = int(re.search(regex_shop_id, shops[i]).group(1))
    shop_inventory = re.findall(regex_items, shops[i])
    for item in shop_inventory:
        item_id = int(item[0])
        item_attributes_dict.update({
            'BuyPrice': int(item[1]),
            'SellPrice': int(item[2]),
            'ProduceQuanity': int(item[3])
        })
        indiv_item_dict.update({item_id: item_attributes_dict.copy()})
        inventory_dict.update({'Items': indiv_item_dict.copy()})
    shops_dict.update({shop_id: inventory_dict.copy()})
main_dict['Shops'] = shops_dict


# with open('shops_dict.txt', 'w') as f:
#     f.write(str(main_dict))

# with open('prices.json', 'w') as f:
#     f.write(json.dumps(main_dict))

# with open('prices_preformatted.json', 'w') as f:
#    f.write(json.dumps(main_dict, indent=4))