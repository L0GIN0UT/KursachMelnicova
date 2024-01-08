# * количество света: (если съемка в помещении)
# яркий свет
# нормальное освещение
# темно
#
# - фирма фотоаппарата:
import random

"Canon", "Nikon", "Sony", "Panasonic", "Fujifilm", "Olympus", "Leica", "Pentax", "Samsung", "Kodak", "Hasselblad", \
    "Phase One", "Ricoh", "Minolta", "Yashica", "Mamiya", "Contax""Polaroid", "Zeiss", "GoPro", "DJI", "Casio", "Lomography", "Konica", "Voigtländer", "Epson", "Rollei", "Lytro", "Sigma", "Vivitar"
#
# Выход
#
# Объективы:
# 1. Стандартный объектив (обычно 50мм)
# 2. Широкоугольный объектив
# 3. Телеобъектив
# 4. Макрообъектив
# 5. Фиксированный объектив
# 6. Зум-объектив
# 7. Рыбий глаз (Fisheye) объектив
# 8. Тилт-шифт (Lensbaby) объектив
# 9. Портретный объектив
# 10. Гелиос
# 11. Оникс
# 12. Панкейк объектив
# 13. Superzoom объектив
# 14. Телеконвертер
# 15. Адаптер объектива
# 16. Анаморфный объектив
# 17. Перископный объектив
# 18. Призменный объектив
# 19. Астроснайпер
# 20. Вариообъектив
#
# - фирма объективов:
# 1. Canon
# 2. Nikon
# 3. Sony
# 4. Sigma
# 5. Tamron
# 6. Zeiss
# 7. Fujinon
# 8. Tokina
# 9. Panasonic
# 10. Leica
# 11. Olympus
# 12. Samyang
# 13. Carl Zeiss
# 14. Pentax
# 15. Schneider Kreuznach
# 16. Voigtländer
# 17. Rokinon
# 18. Hasselblad
# 19. Cooke
# 20. Angenieux
# 21. Laowa
# 22. SLR Magic
# 23. Meike
# 24. Yongnuo
# 25. Bower
# 26. Kamlan
# 27. Mitakon
# 28. Arri
# 29. DJI
# 30. Veydra

genre = ["пейзаж", "натюрморт", "портрет", "репортаж", "документальная фотография", "жанровая фотография",
         "рекламная фотография", "репродукция", "фотоохота", "макрофотография", "панорамная фотография",
         "ночная фотография", "свадебная фотография", "контент съемка", "аэросъемка", "откровенная фотография",
         "творческая съемка", "пленочная фотография", "семейная съемка", "интерьерная съемка"]

place = ["на улице", "в помещении"]

weather_if_outside = ["солнечно", "пасмурно", "дождь", "снег", "туман"]

time_if_outside = ["рассвет (6:00 - 9:00)", "утро (9:00 - 12:00)", "день (12:00 - 16:00)",
                   "вечер (17:00 - 21:00)", "ночь (21:00 - 6:00)"]

amount_light_if_inside = ["яркий свет", "нормальное освещение", "темно"]

firm = ["Canon", "Nikon", "Sony", "Panasonic", "Fujifilm", "Olympus", "Leica", "Pentax", "Samsung", "Kodak",
        "Hasselblad", "Phase One", "Ricoh", "Minolta", "Yashica", "Mamiya", "Contax", "Polaroid", "Zeiss",
        "GoPro", "DJI", "Casio", "Lomography", "Konica", "Voigtländer", "Epson", "Rollei", "Lytro",
        "Sigma", "Vivitar"]

lenses = ["Стандартный объектив (обычно 50мм)", "Широкоугольный объектив", "Телеобъектив", "Макрообъектив",
          "Фиксированный объектив", "Зум-объектив", "Рыбий глаз (Fisheye) объектив",
          "Тилт-шифт (Lensbaby) объектив", "Портретный объектив", "Гелиос", "Оникс", "Панкейк объектив",
          "Superzoom объектив", "Телеконвертер", "Адаптер объектива", "Анаморфный объектив", "Перископный объектив",
          "Призменный объектив", "Астроснайпер", "Вариообъектив"]


def Restart():
    amount = 1000
    arr_of_obj = []
    while amount != 0:
        temp = []
        if len(firm) > 0:
            temp.append(firm[random.randint(0, len(firm) - 1)])
        if len(lenses) > 0:
            temp.append(lenses[random.randint(0, len(lenses) - 1)])
        if len(firm) > 0:
            temp.append(firm[random.randint(0, len(firm) - 1)])
        if len(genre) > 0:
            temp.append(genre[random.randint(0, len(genre) - 1)])
        if len(place) > 0:
            places = place[random.randint(0, len(place) - 1)]
        temp.append(places)
        if places == "на улице":
            if len(weather_if_outside) > 0:
                temp.append(weather_if_outside[random.randint(0, len(weather_if_outside) - 1)])
            if len(time_if_outside) > 0:
                temp.append(time_if_outside[random.randint(0, len(time_if_outside) - 1)])
        else:
            temp.append(amount_light_if_inside[random.randint(0, len(amount_light_if_inside) - 1)])
        arr_of_obj.append(temp)
        amount -= 1
    return arr_of_obj
