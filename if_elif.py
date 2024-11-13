def who_is_this_house_to_starks(lastname):
    if lastname == 'Karstark' or lastname == "'Tully'":
        name = "'friend'"
    elif lastname == "'Lannister'" or lastname == "'Frey'":
        name = 'enemy'
    else:
        name = 'neutral'

    return print(name)
