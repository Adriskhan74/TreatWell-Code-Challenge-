TOP_LEFT_CORNER = '┌'
TOP_RIGHT_CORNER = '┐'
BOTTOM_LEFT_CORNER = '└'
BOTTOM_RIGHT_CORNER = '┘'
HORIZONTAL_LINE = '─'
VERTICAL_LINE = '│'


def create_box(width, height):
    box = []
    for row_i in range(height):
        row = ''
        for col_i in range(width):
            if row_i == 0 and col_i == 0:
                row += TOP_LEFT_CORNER
            elif row_i == 0 and col_i == width - 1:
                row += TOP_RIGHT_CORNER
            elif row_i == height - 1 and col_i == 0:
                row += BOTTOM_LEFT_CORNER
            elif row_i == height - 1 and col_i == width - 1:
                row += BOTTOM_RIGHT_CORNER
            elif row_i == 0 or row_i == height - 1:
                row += HORIZONTAL_LINE
            elif col_i == 0 or col_i == width - 1:
                row += VERTICAL_LINE
            else:
                row += ' '
        box.append(row)
    return box
