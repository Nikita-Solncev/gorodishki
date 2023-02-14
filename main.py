import random
import json
from pprint import pprint



# with open("russia.json", "r", encoding="UTF-8") as file:
#     cities_and_regions = json.load(file)

cities = {}

used_word = []

letters = list("ёйцукенгшщзхфвапролджэячсмитбю".upper())

# for letter in letters:
#     cities[letter.capitalize()] = [] #заполняем cities буквами русского алфавита со значением равным пустому списку

# for i in cities_and_regions: 
#     first_letter = i["city"][0] #перебираем города и вытаскиваем первую букву каждого
#     for letter in cities:
#         if letter == first_letter:
#             cities[letter].append(i["city"]) #в соответствии с первой буквой записывай города в словарь cities

# with open("cities.json", "w", encoding="UTF-8") as json_file:
#     json.dump(cities, json_file, indent=4 ,ensure_ascii=False)

with open("cities.json", "r", encoding="UTF-8") as json_file:
    cities = json.load(json_file)





is_player_move =  random.randint(0, 1) #рандомно получаем True или False

def check_city(word: str, last_letter: str):
    "Функция проверяет правильность введённого слова: наличие его в словаре, написано ли оно на русском и т.д."
    word = word.lower().capitalize()
    
    if last_letter.upper() not in ("", word[0]):
        print(f"{last_letter} {word[0]}")
        return False

    if word not in cities[word[0]]:
        print("Такого города не существует в России\n")
        return False
    elif word in used_word:
        print("Такой город уже был назван.")
        return False
    else:
        return True

def get_user_selection(last_letter=""):
    player_city = input("Введите название города\n")
    is_word_right = check_city(player_city, last_letter)
    while not is_word_right:
        player_city = input("Введите название города\n")
        is_word_right = check_city(player_city, last_letter)
    return player_city

def get_last_letter(city: str):
    if city[-1] in ('ы','ь','ъ'):
        return city[-2]
    return city[-1]
    

def get_computer_selection(last_letter=""):
   
    computer_city = random.choice(cities[last_letter.capitalize()])

    return computer_city


    

def start_game():
    if is_player_move:
        print("Первым ходит игрок.")
        player_city = get_user_selection()
        last_letter = get_last_letter(player_city)
        
        while True:
            computer_city = get_computer_selection(last_letter)
            print(computer_city)
            last_letter =  get_last_letter(computer_city)
            used_word.append(computer_city.lower().capitalize())
            print(f"Введите город на букву {last_letter}")
            player_city = get_user_selection(last_letter)
            last_letter = get_last_letter(player_city)
            used_word.append(player_city.lower().capitalize())


    else:
        print("Первым ходит компутер.")
        computer_city = get_computer_selection(random.choice(letters))
        print(computer_city)
        while True:
            last_letter =  get_last_letter(computer_city)
            print(f"Введите город на букву {last_letter}")
            used_word.append(computer_city.lower().capitalize())
            player_city = get_user_selection(last_letter)
            last_letter = get_last_letter(player_city)
            used_word.append(player_city.lower().capitalize())



start_game()
        
    

    

    



    
"""
проверка слова
цикл игры
ход игрока
ход компуктера
обработка тупиков

функция получения последней буквы 

"""
    
