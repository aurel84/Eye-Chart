#!/usr/bin/env python3

import random
import string


class snellen_chart_input:
    def __init__(self):
        pass

    def do_character_chart(style, case):
        prev = 0
        character_list = []
        grid_output = []

        if style == 0:
            grid_length = int(45)
            grid_index = [1, 3, 6, 10, 15, 21, 28, 36]

        elif style == 1:
            grid_length = int(55)
            grid_index = [4, 9, 15, 21, 28, 36, 45, 56]

        for i in range(grid_length):
            if case == 0:
                character = random.choice(string.ascii_uppercase)
            elif case == 1:
                character = random.choice(string.ascii_lowercase)
            elif case == 2:
                character = random.choice(string.ascii_letters)
            elif case == 3:
                character = random.choice(
                    string.ascii_uppercase + str(random.randint(0, 9))
                )
            elif case == 4:
                character = random.choice(
                    string.ascii_lowercase + str(random.randint(0, 9))
                )
            elif case == 5:
                character = random.choice(
                    string.ascii_letters + str(random.randint(0, 9))
                )
            else:
                character = random.randint(0, 9)

            character_list.append(character)

        for index in grid_index:
            grid_output.append(character_list[prev:index])
            prev = index

        grid_output.append(character_list[prev:])

        return grid_output


def snellen_chart(arg1, arg2):
    divid = 1

    for indice in snellen_chart_input.do_character_chart(arg1, arg2):
        indice = (
            str(indice)
            .strip("{")
            .strip("}")
            .strip("[")
            .strip("]")
            .replace(",", "")
            .replace("'", "")
        )

        mdiv = "m" + str(divid)

        display(indice, target=mdiv, append=False)

        divid += 1


for x in range(2):
    for y in range(7):
        snellen_chart(x, y)


if __name__ == "__main__":
    snellen_chart(0, 0)
