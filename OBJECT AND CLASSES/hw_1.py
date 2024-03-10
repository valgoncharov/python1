class Image:
    # Атрибут класса
    resolution = "1334x780"
    title = "Family"
    extention = ".jpg"

    def __init__(self, resolution):
        # Атрибут экземпляра класса
        self.resolution = resolution

    def resize(self, resolution):
        self.resolution = resolution


# Использование атрибутов класса и экземпляра
print(Image.title)  # Выведет: Значение атрибута класса

new = Image("3540x2100")
print(new.resolution)  # Выведет: Значение экземпляра
print(new.extention)  # Выведет: Значение атрибута класса

new.resize("1340x780")
print(new.resolution)
