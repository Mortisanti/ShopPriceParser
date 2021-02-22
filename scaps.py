# ShopID: ItemID, BuyPrice, SellPrice, ProduceQuanity; ItemID, BuyPrice, SellPrice, ProduceQuanity;

import re
import csv

# Create regular expression patterns
regex_shop = re.compile('(\d+):')
regex_items = re.compile('(\d+,\d+,\d+,\d+;)+?')

# Open prices data file and split lines based on linebreaks, combine into list as elements
with open('prices.dat', 'r') as f:
    text = f.read().splitlines()

# Create dictionary to store first shop and its inventory (first item)
shop_inventories = {}

# Search for first shop number
shop_match = re.search(regex_shop, text[0]).group(1)

# Search for all of the attributes of the first item
item_matches = re.findall(regex_items, text[0])

# Split each attribute into its own element of a list, remove semicolon in the process
item_matches_split = re.split(',', item_matches[0].replace(';', ''))

# Create dictionary where we will store item attributes and nest within shop_inventories dictionary
item_attributes = {
    'ItemID': '',
    'BuyPrice': '',
    'SellPrice': '',
    'ProduceQuantity': ''
}

# Interate through each item attribute key and assign each respective value from the item_matches_split list
value = 0
for key in item_attributes:
    item_attributes[key] = item_matches_split[value]
    value += 1

# Assign item_attributes dict as a value to the shop key in shop_inventories dictionary, nesting within
shop_inventories[shop_match] = item_attributes

# Write the end result to shop_mess.txt file
with open('shop_mess.txt', 'w') as f:
    f.write(str(shop_inventories))