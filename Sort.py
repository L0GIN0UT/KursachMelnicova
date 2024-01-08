
def sortByFirmOfCamera1(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[0] == "Canon" and choice == 1:
            newArrOfCameras.append(camera)
        if camera[0] == "Nikon" and choice == 2:
            newArrOfCameras.append(camera)
        if camera[0] == "Sony" and choice == 3:
            newArrOfCameras.append(camera)
        if camera[0] == "Panasonic" and choice == 4:
            newArrOfCameras.append(camera)
        if camera[0] == "Fujifilm" and choice == 5:
            newArrOfCameras.append(camera)
        if camera[0] == "Olympus" and choice == 6:
            newArrOfCameras.append(camera)
        if camera[0] == "Leica" and choice == 7:
            newArrOfCameras.append(camera)
        if camera[0] == "Pentax" and choice == 8:
            newArrOfCameras.append(camera)
        if camera[0] == "Samsung" and choice == 9:
            newArrOfCameras.append(camera)
        if camera[0] == "Kodak" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByFirmOfCamera2(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[0] == "Hasselblad" and choice == 1:
            newArrOfCameras.append(camera)
        if camera[0] == "Phase One" and choice == 2:
            newArrOfCameras.append(camera)
        if camera[0] == "Ricoh" and choice == 3:
            newArrOfCameras.append(camera)
        if camera[0] == "Minolta" and choice == 4:
            newArrOfCameras.append(camera)
        if camera[0] == "Yashica" and choice == 5:
            newArrOfCameras.append(camera)
        if camera[0] == "Mamiya" and choice == 6:
            newArrOfCameras.append(camera)
        if camera[0] == "Contax" and choice == 7:
            newArrOfCameras.append(camera)
        if camera[0] == "Polaroid" and choice == 8:
            newArrOfCameras.append(camera)
        if camera[0] == "Zeiss" and choice == 9:
            newArrOfCameras.append(camera)
        if camera[0] == "GoPro" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByFirmOfCamera3(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[0] == "DJI" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[0] == "Casio" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[0] == "Lomography" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[0] == "Konica" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[0] == "Voigtländer" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[0] == "Epson" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[0] == "Rollei" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[0] == "Lytro" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[0] == "Sigma" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[0] == "Vivitar" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByLenses1(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[1] == "Стандартный объектив (обычно 50мм)" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[1] == "Широкоугольный объектив" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[1] == "Телеобъектив" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[1] == "Макрообъектив" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[1] == "Фиксированный объектив" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[1] == "Зум-объектив" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[1] == "Рыбий глаз (Fisheye) объектив" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[1] == "Тилт-шифт (Lensbaby) объектив" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[1] == "Портретный объектив" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[1] == "Гелиос" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByLenses2(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[1] == "Оникс" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[1] == "Панкейк объектив" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[1] == "Superzoom объектив" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[1] == "Телеконвертер" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[1] == "Адаптер объектива" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[1] == "Анаморфный объектив" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[1] == "Перископный объектив" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[1] == "Призменный объектив" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[1] == "Астроснайпер" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[1] == "Вариообъектив" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByFirmOfLenses1(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[2] == "Canon" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[2] == "Nikon" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[2] == "Sony" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[2] == "Panasonic" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[2] == "Fujifilm" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[2] == "Olympus" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[2] == "Leica" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[2] == "Pentax" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[2] == "Samsung" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[2] == "Kodak" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByFirmOfLenses2(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[2] == "Hasselblad" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[2] == "Phase One" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[2] == "Ricoh" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[2] == "Minolta" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[2] == "Yashica" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[2] == "Mamiya" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[2] == "Contax" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[2] == "Polaroid" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[2] == "Zeiss" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[2] == "GoPro" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByFirmOfLenses3(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[2] == "DJI" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[2] == "Casio" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[2] == "Lomography" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[2] == "Konica" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[2] == "Voigtländer" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[2] == "Epson" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[2] == "Rollei" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[2] == "Lytro" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[2] == "Sigma" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[2] == "Vivitar" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByGenre1(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[3] == "пейзаж" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[3] == "натюрморт" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[3] == "портрет" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[3] == "репортаж" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[3] == "документальная фотография" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[3] == "жанровая фотография" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[3] == "рекламная фотография" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[3] == "репродукция" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[3] == "фотоохота" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[3] == "макрофотография" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByGenre2(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[3] == "панорамная фотография" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[3] == "ночная фотография" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[3] == "свадебная фотография" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[3] == "контент съемка" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[3] == "аэросъемка" and choice == 5:
            newArrOfCameras.append(camera)
        elif camera[3] == "откровенная фотография" and choice == 6:
            newArrOfCameras.append(camera)
        elif camera[3] == "творческая съемка" and choice == 7:
            newArrOfCameras.append(camera)
        elif camera[3] == "пленочная фотография" and choice == 8:
            newArrOfCameras.append(camera)
        elif camera[3] == "семейная съемка" and choice == 9:
            newArrOfCameras.append(camera)
        elif camera[3] == "интерьерная съемка" and choice == 10:
            newArrOfCameras.append(camera)
    return newArrOfCameras


def sortByPlace(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[4] == "в помещении" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[4] == "на улице" and choice == 2:
            newArrOfCameras.append(camera)
    return newArrOfCameras


# Если на улице
def sortByWeather(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[5] == "солнечно" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[5] == "пасмурно" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[5] == "дождь" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[5] == "снег" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[5] == "туман" and choice == 5:
            newArrOfCameras.append(camera)
    return newArrOfCameras


# Если на улице
def sortByTime(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[6] == "рассвет (6:00 - 9:00)" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[6] == "утро (9:00 - 12:00)" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[6] == "день (12:00 - 16:00)" and choice == 3:
            newArrOfCameras.append(camera)
        elif camera[6] == "вечер (17:00 - 21:00)" and choice == 4:
            newArrOfCameras.append(camera)
        elif camera[6] == "ночь (21:00 - 6:00)" and choice == 5:
            newArrOfCameras.append(camera)
    return newArrOfCameras


# Если в помещении
def sortByAmountOfLight(choice, cameras):
    newArrOfCameras = []
    for camera in cameras:
        if camera[5] == "яркий свет" and choice == 1:
            newArrOfCameras.append(camera)
        elif camera[5] == "нормальное освещение" and choice == 2:
            newArrOfCameras.append(camera)
        elif camera[5] == "темно" and choice == 3:
            newArrOfCameras.append(camera)
    return newArrOfCameras


