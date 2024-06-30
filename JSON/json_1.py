import json

json_str = '{"id":245, "brand": "Nike", "qty":84, "status": {"isForSale":true}}'
json_array = '[1, 2, 3]'
sneakers = json.loads(json_str)

print(type(sneakers))
print(sneakers)

print(sneakers["brand"])
print(sneakers["qty"])
print(sneakers["status"]["isForSale"])

list_json = json.loads(json_array)

print(type(list_json))
print(list_json)
# Форматирование

json.dumps(sneakers, indent=1)

# Обратная конвертация
json_from_dict = json.dumps(sneakers)

print(json_from_dict)
print(type(json_from_dict))

# Форматирование

json_from_dict = json.dumps(sneakers, indent=2)

print(json_from_dict)
