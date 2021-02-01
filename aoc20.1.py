
def open_file(location:str='20.1.input.txt') -> list:
    with open(location, 'r', encoding='utf8') as f:
        input_lines = f.readlines()

    return input_lines


# Remember to include empty line at the end of file
def process_input(lines: list) -> dict:
    tiles = []

    for line in lines:
        if line == '\n':
            tiles.append(Tile(tile_number, new_tile))

        elif line[0:4] == 'Tile':
            tile_number = line[5:-2]
            new_tile = []
        else:
            new_tile.append(line.replace('\n', ''))

    return tiles


class Tile:

    def __init__(self, id, rows):
        self.id = id
        self.rows = rows

    def flip_vertically(self):
        new_rows = [line[::-1] for line in self.rows]
        self.rows = new_rows

    def rotate_90_clockwise(self):   
        new_tile = []
        
        for line in (zip(*self.rows[::-1])):
            new_tile.append(''.join(list(line)))

        self.rows = new_tile

    def get_rows(self):
        return self.rows
    
    def get_id(self):
        return self.id

    def get_first_row(self):
        return self.rows[0]

    def get_last_row(self):
        return self.rows[-1]

    def get_left_column(self):
        return ''.join(list(zip(*self.rows))[0])

    def get_right_column(self):
        return ''.join(list(zip(*self.rows))[-1])

    def print_tile(self):
        for row in self.rows:
            print(row)


def assemble_tiles(tiles: list):
    # column, row
    field = {0: {0: tiles.pop()}}

    iteration = 0
    while tiles:
        iteration += 1
        print(f'Iteration: {iteration}, remaining tiles: {len(tiles)}')

        # Compare all from top
        match_found = False
        for column in field.keys():
            top_tile_row = max(field[column].keys())
            top_tile = field[column][top_tile_row]

            top_tile_top_row = top_tile.get_first_row()
            for tile_index, compare_tile in enumerate(tiles):
                match_found = False

                for _ in range(4):
                    if compare_tile.get_last_row() == top_tile_top_row:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()

                if match_found:
                    break

                compare_tile.flip_vertically()
                for _ in range(4):
                    if compare_tile.get_last_row() == top_tile_top_row:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()
                
                if match_found:
                    break
                
            if match_found:
                field[column][top_tile_row + 1] = compare_tile
                tiles.pop(tile_index)

        # Compare all from bottom
        match_found = False
        for column in field.keys():
            bottom_tile_row = min(field[column].keys())
            bottom_tile = field[column][bottom_tile_row]

            bottom_tile_bottom_row = bottom_tile.get_last_row()
            for tile_index, compare_tile in enumerate(tiles):
                match_found = False

                for _ in range(4):
                    if compare_tile.get_first_row() == bottom_tile_bottom_row:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()

                if match_found:
                    break

                compare_tile.flip_vertically()
                for _ in range(4):
                    if compare_tile.get_first_row() == bottom_tile_bottom_row:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()
                
                if match_found:
                    break
                
            if match_found:
                field[column][bottom_tile_row - 1] = compare_tile
                tiles.pop(tile_index)

        # Compare all from left
        edge_coordinates = []
        rows_accounted_for = []
        for column in field:
            for row in field[column]:
                if not row in rows_accounted_for:
                    for candidate_column in sorted(field):
                        if row in field[candidate_column]:
                            rows_accounted_for.append(row)
                            edge_coordinates.append((candidate_column, row))
                            break
        
        match_found = False
        for leftmost_column, row in edge_coordinates:
            leftmost_tile = field[leftmost_column][row]

            left_tile_left_column = leftmost_tile.get_left_column()
            for tile_index, compare_tile in enumerate(tiles):
                match_found = False

                for _ in range(4):
                    if compare_tile.get_right_column() == left_tile_left_column:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()

                if match_found:
                    break

                compare_tile.flip_vertically()
                for _ in range(4):
                    if compare_tile.get_right_column() == left_tile_left_column:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()
                
                if match_found:
                    break
                
            if match_found:
                if leftmost_column - 1 in field:
                    field[leftmost_column - 1][row] = compare_tile
                else:
                    field[leftmost_column - 1] = {row: compare_tile}
                tiles.pop(tile_index)

        # Compare all from right
        edge_coordinates = []
        rows_accounted_for = []
        for column in field:
            for row in field[column]:
                if not row in rows_accounted_for:
                    for candidate_column in sorted(field, reverse=True):
                        if row in field[candidate_column]:
                            rows_accounted_for.append(row)
                            edge_coordinates.append((candidate_column, row))
                            break

        match_found = False
        for rightmost_column, row in edge_coordinates:
            rightmost_tile = field[rightmost_column][row]

            right_tile_right_column = rightmost_tile.get_right_column()
            for tile_index, compare_tile in enumerate(tiles):
                match_found = False

                for _ in range(4):
                    if compare_tile.get_left_column() == right_tile_right_column:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()

                if match_found:
                    break

                compare_tile.flip_vertically()
                for _ in range(4):
                    if compare_tile.get_left_column() == right_tile_right_column:
                        match_found = True
                        break
                    compare_tile.rotate_90_clockwise()
                
                if match_found:
                    break

            if match_found:
                if rightmost_column + 1 in field:
                    field[rightmost_column + 1][row] = compare_tile
                else:
                    field[rightmost_column + 1] = {row: compare_tile}
                tiles.pop(tile_index)

    return field


def field_print(field: dict):
    for column in sorted(field, reverse=False):
        # print(f'\nColumn: {column}')

        for row in sorted(field[column], reverse=True):
            print(f'\nColumn: {column}, row: {row}, tile ID: {field[column][row].get_id()}')

            field[column][row].print_tile()


all_tiles = process_input(open_file())
# all_tiles = process_input(open_file('20.1.input.test.txt'))

completed_field = assemble_tiles(all_tiles)


max_column = max(completed_field.keys())
min_column = min(completed_field.keys())

max_row = max(completed_field[max_column].keys())
min_row = min(completed_field[max_column].keys())

corner1 = int(completed_field[max_column][max_row].get_id())
corner2 = int(completed_field[max_column][min_row].get_id())
corner3 = int(completed_field[min_column][max_row].get_id())
corner4 = int(completed_field[min_column][min_row].get_id())

total_product = corner1 * corner2 * corner3 * corner4

print(total_product)