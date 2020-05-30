# author : Lsh
# date: 2019/12/24 9:29
# file_name:tree

def color_string(self, style=0, font_color=32, back_color=42, fill_string="*"):
    """
    return string with input settings
    :param style: font display style, default as console default
    :param font_color: color of font, default as black
    :param back_color: background color, default as white
    :param fill_string: symbol inside the color block
    :return: String with console display style settings
    """
    try:
        return "\033[" \
               + str(style) + ";" + str(font_color) + ";" + str(back_color) \
               + "m" \
               + fill_string \
               + "\033[0m"
    except:
        raise TypeError


def text_xmas_tree(self, height=6):
    """
    decoration is the string to be showed as decoration
    fills is the base element of the santa tree
    :param height: total height of the tree, also the total lines of the whole text
    :return: None
    """
    # minimum height is 6 or the tree looks ugly
    if height < 6:
        height = 6
    fills = 1
    for i in range(1, height):
        # decoration color depends on the number of the level
        if i % 3 == 0:
            # red font and red back with default style
            decoration = self.color_string(0, 32, 41, "*")
        elif i % 2 == 0:
            # green font and green back with default style
            decoration = self.color_string(0, 31, 42, "*")
        else:
            # yellow font and yellow back with default style
            decoration = self.color_string(0, 31, 43, "*")

        if fills > 1:
            # combine string with the format:
            # spaces + decoration + fills + decoration
            print((' ' * (height - i)) \
                  + decoration \
                  + (self.color_string(0, 37, 42, "+") * (fills - 2)) \
                  + decoration)
        else:
            # first line has only one symbol
            print((' ' * (height - i)) + decoration)
        fills += 2

    # bottom of the tree, red font and red back
    print((' ' * (height - 1)) + self.color_string(5, 31, 41, "|"))


text_xmas_tree()