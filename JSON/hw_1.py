import json

json_srt = '{"squadName": "Super hero squad","homeTown": "Metro City","formed": 2016,"secretBase": "Super tower", "active": true}'

hw_json = json.loads(json_srt)

print(hw_json)
