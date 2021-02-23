import json

# Test to read json data
with open('prices.json', 'r') as f:
    json_data = json.loads(f.read())

price = json_data['ShopID']['3']['ItemID']['28']['SellPrice']
print(price)
# >>> 29