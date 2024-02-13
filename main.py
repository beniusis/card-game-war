import utils


def main():
    name1 = utils.get_the_name_of_the_first_player()
    name2 = utils.get_the_name_of_the_second_player()
    p1, p2 = utils.initialize_players(name1, name2)

    round = 1
    while p1.get_deck_size() and p2.get_deck_size():
        print(f"Round: {round}")
        utils.play_round(p1, p2)
        round += 1

        if not p1.get_deck_size():
            print(f"{p2.name} wins the game!")
        elif not p2.get_deck_size():
            print(f"{p1.name} wins the game!")


if __name__ == "__main__":
    main()
