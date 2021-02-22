# ShopID: ItemID, BuyPrice, SellPrice, ProduceQuanity; ItemID, BuyPrice, SellPrice, ProduceQuanity;

import re
import csv

'''
with open('prices.dat', 'r') as f:
    shop_list = f.read().splitlines()
'''

'''
with open('prices.dat', 'r') as f:
    text = f.read().replace('\n', 'w').splitlines()
    with open('shop_mess.txt', 'w') as f:
        f.write(str(re.split(':|,|;', str(text))))
'''

regex_shop = re.compile('(\d+):')
regex_items = re.compile('(\d+,\d+,\d+,\d+;)+?')

with open('prices.dat', 'r') as f:
    text = f.read().splitlines()

shop_inventories = {}
shop_match = re.search(regex_shop, text[0])
item_matches = re.findall(regex_items, text[0])
shop_inventories[shop_match] = item_matches

with open('shop_mess.txt', 'w') as f:
    f.write(str(shop_inventories))