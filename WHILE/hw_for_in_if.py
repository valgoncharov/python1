my_motorbike = {
    'brand': 'bmw',
    'country': 'germany',
    'owner': 'val'
}
bike = {k: v.upper() for k, v in my_motorbike.items()}

print(bike)
print(my_motorbike)


my_motorbike1 = ['BMV', 'Germany', 'Valik']

bike1 = [el for el in my_motorbike1 if len(el) > 3]

print(bike1)
print(my_motorbike1)
