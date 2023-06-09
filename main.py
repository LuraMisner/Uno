from deck import Deck


def main():
    d = Deck()

    while len(d.deck) > 0:
        card = d.draw_card()
        print(card.get_image_path())


main()
