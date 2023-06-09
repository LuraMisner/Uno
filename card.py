class Card:
    def __init__(self, v, c):
        self.value = v
        self.color = c

        if self.value != self.color:
            self.image_path = f'images/{self.color}-{self.value}'
        else:
            # Wild card
            self.image_path = f'images/{self.color}'

    def get_image_path(self):
        return self.image_path

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color
