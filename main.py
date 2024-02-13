import utils


def main():
    name1 = utils.get_the_name_of_the_first_player()
    name2 = utils.get_the_name_of_the_second_player()
    p1, p2 = utils.initialize_players(name1, name2)
    p1_card, p2_card = utils.draw_cards(p1, p2)


if __name__ == "__main__":
    main()
