from random import randint
import configparser

config = configparser.ConfigParser()
config.read("task2.input")

candies_amount = [int(config["DEFAULT"]["candies_amount"])]
take_limit = int(config["DEFAULT"]["take_limit"])

player2_bot_or_human_chooser = input("Играть с ботом - 1, с человеком - любое другое значение: ")
player2_is_bot = True if player2_bot_or_human_chooser == "1" else False
move_transferred_to_player = randint(1, 2)
last_move_made_player = move_transferred_to_player


def ask_human_about_of_candies_count():
    while True:
        take_amount = int(input("Выберете количество конфет:"))
        if take_amount < 1 or take_amount > take_limit:
            print(f"Можно взять конфет в количестве от 1 до {take_limit} включительно")
            continue
        if take_amount > candies_amount[0]:
            print("Запршенное количество конфет больше оставшихся")
            continue
        return take_amount

def ask_bot_about_of_candies_count():
    if candies_amount[0] <= take_limit:
        return candies_amount[0]
    take_amount = candies_amount[0] % (take_limit + 1)
    if take_amount == 0:
        take_amount = randint(1, take_limit)
    return take_amount


def take_candies(mode):
    take_amount = ask_human_about_of_candies_count() if mode == "human" else ask_bot_about_of_candies_count()
    candies_amount[0] = candies_amount[0] - take_amount
    return take_amount


while True:
    if candies_amount[0] == 0:
        with open("task2.output", "w", encoding="utf-8") as f:
            f.write(f"Победу одержал игрок {last_move_made_player}")
        print(f"Победу одержал игрок {last_move_made_player}")
        break

    print(f"Ход делает игрок {'1' if move_transferred_to_player == 1 else '2'}")
    mode = "bot" if move_transferred_to_player == 2 and player2_is_bot else "human"
    print(f"Игроком взято конфет в количестве: {take_candies(mode)}")
    print(f"Осталось конфет: {candies_amount[0]}\n")
    last_move_made_player = 1 if move_transferred_to_player == 1 else 2
    move_transferred_to_player = 1 if move_transferred_to_player == 2 else 2
