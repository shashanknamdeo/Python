

# # # # def build_house(length, height, direction):
# # # #     # Roof height
# # # #     roof_height = (length + 1) // 2 if direction in ['U', 'H'] else 0
# # # #     total_height = height + roof_height
    
# # # #     width = length
# # # #     house = [[' ' for _ in range(width)] for _ in range(total_height)]
    
# # # #     # Build walls and base
# # # #     for i in range(height):
# # # #         row_idx = roof_height + i
# # # #         house[row_idx][0] = '@'
# # # #         house[row_idx][width-1] = '&'
# # # #         for j in range(1, width-1):
# # # #             house[row_idx][j] = ' '
# # # #     # Base row
# # # #     for j in range(width):
# # # #         house[roof_height + height - 1][j] = '#'
    
# # # #     # Build roof for U or H
# # # #     if direction in ['U', 'H']:
# # # #         for i in range(roof_height):
# # # #             house[roof_height - i - 1][i] = '/'
# # # #             house[roof_height - i - 1][width - i - 1] = '\\'
# # # #             # Fill middle with spaces (optional, already spaces)
    
# # # #     return [''.join(row) for row in house]


# # # def build_house(length, height):
# # #     """
# # #     Build upright house with base, walls, and roof.
# # #     Returns list of strings representing rows.
# # #     Height includes base.
# # #     """
# # #     # Roof height
# # #     roof_height = (length + 1) // 2
# # #     total_height = height + roof_height

# # #     width = length
# # #     house = [[' ' for _ in range(width)] for _ in range(total_height)]

# # #     # Build walls
# # #     for i in range(height):
# # #         row_idx = roof_height + i
# # #         house[row_idx][0] = '@'
# # #         house[row_idx][width - 1] = '&'
# # #         for j in range(1, width - 1):
# # #             house[row_idx][j] = ' '

# # #     # Build base
# # #     for j in range(width):
# # #         house[roof_height + height - 1][j] = '#'

# # #     # Build roof
# # #     for i in range(roof_height):
# # #         house[roof_height - i - 1][i] = '/'
# # #         house[roof_height - i - 1][width - i - 1] = '\\'

# # #     # Convert to list of strings
# # #     return [''.join(row) for row in house]

# # # def tilt_house(house, direction):
# # #     """
# # #     Tilt/mirror a house.
# # #     house: list of strings
# # #     direction: 'U', 'D', 'L', 'R', 'H'
# # #     """
# # #     if direction == 'H':
# # #         return house
# # #     elif direction == 'U':
# # #         # Flip vertically: base moves to top, roof at bottom
# # #         flipped = house[::-1]
# # #         # Swap roof slashes
# # #         flipped = [row.replace('/', 'X').replace('\\', '/').replace('X', '\\') for row in flipped]
# # #         return flipped
# # #     elif direction == 'D':
# # #         # Keep as upright
# # #         return house
# # #     elif direction == 'L':
# # #         # Mirror horizontally and swap slashes
# # #         mirrored = []
# # #         for row in house:
# # #             row_rev = row[::-1]
# # #             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
# # #             mirrored.append(row_rev)
# # #         return mirrored
# # #     elif direction == 'R':
# # #         # Mirror horizontally and swap slashes
# # #         mirrored = []
# # #         for row in house:
# # #             row_rev = row[::-1]
# # #             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
# # #             mirrored.append(row_rev)
# # #         return mirrored


# # # def join_houses(houses):
# # #     """
# # #     Join multiple tilted houses side by side aligned at base.
# # #     houses: list of list of strings (each house)
# # #     """
# # #     # Find maximum height
# # #     max_height = max(len(h) for h in houses)
    
# # #     # Pad each house at the top with spaces to match max_height
# # #     padded_houses = []
# # #     for h in houses:
# # #         pad_top = max_height - len(h)
# # #         width = len(h[0])
# # #         new_house = [' ' * width] * pad_top + h
# # #         padded_houses.append(new_house)
    
# # #     # Concatenate row by row
# # #     result = []
# # #     for i in range(max_height):
# # #         row = ''.join(padded_houses[j][i] for j in range(len(houses)))
# # #         result.append(row)
    
# # #     return result

# # def build_house(length, height):
# #     roof_height = (length + 1) // 2
# #     total_height = height + roof_height
# #     width = length
# #     house = [[' ' for _ in range(width)] for _ in range(total_height)]

# #     # Build walls
# #     for i in range(height):
# #         row_idx = roof_height + i
# #         house[row_idx][0] = '@'
# #         house[row_idx][width - 1] = '&'

# #     # Base
# #     for j in range(width):
# #         house[roof_height + height - 1][j] = '#'

# #     # Roof
# #     for i in range(roof_height):
# #         house[roof_height - i - 1][i] = '/'
# #         house[roof_height - i - 1][width - i - 1] = '\\'

# #     return [''.join(row) for row in house]

# # def tilt_house(house, direction):
# #     if direction == 'H':
# #         return house
# #     elif direction == 'U':
# #         flipped = house[::-1]
# #         flipped = [row.replace('/', 'X').replace('\\', '/').replace('X', '\\') for row in flipped]
# #         return flipped
# #     elif direction == 'D':
# #         return house
# #     elif direction == 'L':
# #         mirrored = []
# #         for row in house:
# #             row_rev = row[::-1]
# #             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
# #             mirrored.append(row_rev)
# #         return mirrored
# #     elif direction == 'R':
# #         mirrored = []
# #         for row in house:
# #             row_rev = row[::-1]
# #             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
# #             mirrored.append(row_rev)
# #         return mirrored

# # def join_houses(houses):
# #     max_height = max(len(h) for h in houses)
# #     padded_houses = []
# #     for h in houses:
# #         pad_top = max_height - len(h)
# #         width = len(h[0])
# #         new_house = [' ' * width] * pad_top + h
# #         padded_houses.append(new_house)

# #     result = []
# #     for i in range(max_height):
# #         row = ''.join(padded_houses[j][i] for j in range(len(houses)))
# #         # Remove all spaces
# #         result.append(row.replace(' ', ''))
# #     return result

# # # Example usage
# # houses_specs = [
# #     (6, 3, 'U'),
# #     (4, 2, 'U'),
# #     (8, 4, 'L'),
# #     (2, 2, 'H')
# # ]

# # houses = []
# # for length, height, direction in houses_specs:
# #     h = build_house(length, height)
# #     h_tilted = tilt_house(h, direction)
# #     houses.append(h_tilted)

# # final_art = join_houses(houses)
# # for row in final_art:
# #     print(row)

# def build_house(length, height):
#     """
#     Build upright house with base, walls, and roof.
#     Height includes base. Width = length.
#     Returns list of strings (rows).
#     """
#     roof_height = (length + 1) // 2
#     total_height = height + roof_height
#     width = length
#     house = [[' ' for _ in range(width)] for _ in range(total_height)]

#     # Build walls
#     for i in range(height):
#         row_idx = roof_height + i
#         house[row_idx][0] = '@'
#         house[row_idx][width - 1] = '&'

#     # Build base
#     for j in range(width):
#         house[roof_height + height - 1][j] = '#'

#     # Build roof
#     for i in range(roof_height):
#         house[roof_height - i - 1][i] = '/'
#         house[roof_height - i - 1][width - i - 1] = '\\'

#     return [''.join(row) for row in house]

# def tilt_house(house, direction):
#     """
#     Tilt/mirror house in given direction: 'U', 'D', 'L', 'R', 'H'.
#     Returns new list of strings.
#     """
#     if direction == 'H':
#         return house
#     elif direction == 'U':
#         flipped = house[::-1]
#         flipped = [row.replace('/', 'X').replace('\\', '/').replace('X', '\\') for row in flipped]
#         return flipped
#     elif direction == 'D':
#         return house
#     elif direction == 'L':
#         mirrored = []
#         for row in house:
#             row_rev = row[::-1]
#             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
#             mirrored.append(row_rev)
#         return mirrored
#     elif direction == 'R':
#         mirrored = []
#         for row in house:
#             row_rev = row[::-1]
#             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
#             mirrored.append(row_rev)
#         return mirrored

# def join_houses(houses):
#     """
#     Join multiple tilted houses side by side aligned at base.
#     Removes all unnecessary spaces.
#     """
#     max_height = max(len(h) for h in houses)
#     padded_houses = []
#     for h in houses:
#         pad_top = max_height - len(h)
#         width = len(h[0])
#         new_house = [' ' * width] * pad_top + h
#         padded_houses.append(new_house)

#     result = []
#     for i in range(max_height):
#         row = ''.join(padded_houses[j][i] for j in range(len(houses)))
#         result.append(row.replace(' ', ''))
#     return result

# def parse_input(input_line):
#     """
#     Parse input line like '6x3U 4x2U 8x4L 2x2H'
#     Returns list of tuples: (length, height, direction)
#     """
#     specs = input_line.strip().split()
#     parsed = []
#     for s in specs:
#         if 'x' in s:
#             length_part, rest = s.split('x')
#             height_part = ''.join(filter(str.isdigit, rest))
#             direction = ''.join(filter(str.isalpha, rest))
#             parsed.append((int(length_part), int(height_part), direction.upper()))
#     return parsed

# # -------- Main Execution --------
# if __name__ == "__main__":
#     input_line = input().strip()  # e.g., "6x3U 4x2U 8x4L 2x2H"
#     houses_specs = parse_input(input_line)

#     houses = []
#     for length, height, direction in houses_specs:
#         h = build_house(length, height)
#         h_tilted = tilt_house(h, direction)
#         houses.append(h_tilted)

#     final_art = join_houses(houses)
#     for row in final_art:
#         print(row)

def build_house(length, height):
    """
    Build upright house with base, walls, and roof.
    Height includes base. Width = length.
    Returns list of strings (rows).
    """
    roof_height = (length + 1) // 2
    total_height = height + roof_height
    width = length
    house = [[' ' for _ in range(width)] for _ in range(total_height)]

    # Build walls
    for i in range(height):
        row_idx = roof_height + i
        house[row_idx][0] = '@'
        house[row_idx][width - 1] = '&'

    # Build base
    for j in range(width):
        house[roof_height + height - 1][j] = '#'

    # Build roof
    for i in range(roof_height):
        house[roof_height - i - 1][i] = '/'
        house[roof_height - i - 1][width - i - 1] = '\\'

    return [''.join(row) for row in house]

# def tilt_house(house, direction):
#     """
#     Tilt/mirror house in given direction: 'U', 'D', 'L', 'R', 'H'.
#     Returns new list of strings.
#     """
#     if direction == 'H':
#         return house
#     elif direction == 'U':
#         flipped = house[::-1]
#         flipped = [row.replace('/', 'X').replace('\\', '/').replace('X', '\\') for row in flipped]
#         return flipped
#     elif direction == 'D':
#         return house
#     elif direction == 'L':
#         mirrored = []
#         for row in house:
#             row_rev = row[::-1]
#             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
#             mirrored.append(row_rev)
#         return mirrored
#     elif direction == 'R':
#         mirrored = []
#         for row in house:
#             row_rev = row[::-1]
#             row_rev = row_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
#             mirrored.append(row_rev)
#         return mirrored

def tilt_house(house, direction):
    """
    Tilt/mirror a single house.
    house: list of strings
    direction: 'U', 'D', 'L', 'R', 'H'
    """
    if direction == 'H':
        return house

    # Split into roof, walls, base
    roof_rows = []
    wall_rows = []
    base_row = ''
    for row in house:
        if '#' in row:
            base_row = row
        elif '@' in row or '&' in row:
            wall_rows.append(row)
        else:
            roof_rows.append(row)

    if direction == 'U':
        # Roof stays on top, walls above base
        # Flip roof vertically
        new_roof = []
        for r in reversed(roof_rows):
            r_new = r.replace('/', 'X').replace('\\', '/').replace('X', '\\')
            new_roof.append(r_new)
        return wall_rows + new_roof + [base_row]

    elif direction == 'D':
        # Base at top, walls below, roof at bottom
        new_roof = []
        for r in reversed(roof_rows):
            r_new = r.replace('/', 'X').replace('\\', '/').replace('X', '\\')
            new_roof.append(r_new)
        return [base_row] + wall_rows + new_roof

    elif direction == 'L':
        mirrored = []
        for r in house:
            r_rev = r[::-1]
            r_rev = r_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
            mirrored.append(r_rev)
        return mirrored

    elif direction == 'R':
        mirrored = []
        for r in house:
            r_rev = r[::-1]
            r_rev = r_rev.replace('/', 'X').replace('\\', '/').replace('X', '\\')
            mirrored.append(r_rev)
        return mirrored






def join_houses(houses):
    """
    Join multiple tilted houses side by side aligned at base.
    Keeps all blank spaces (inside and outside houses).
    """
    max_height = max(len(h) for h in houses)
    padded_houses = []
    for h in houses:
        pad_top = max_height - len(h)
        width = len(h[0])
        new_house = [' ' * width] * pad_top + h
        padded_houses.append(new_house)

    result = []
    for i in range(max_height):
        row = ''.join(padded_houses[j][i] for j in range(len(houses)))
        result.append(row)
    return result

def parse_input(input_line):
    """
    Parse input line like '6x3U 4x2U 8x4L 2x2H'
    Returns list of tuples: (length, height, direction)
    """
    specs = input_line.strip().split()
    parsed = []
    for s in specs:
        if 'x' in s:
            length_part, rest = s.split('x')
            height_part = ''.join(filter(str.isdigit, rest))
            direction = ''.join(filter(str.isalpha, rest))
            parsed.append((int(length_part), int(height_part), direction.upper()))
    return parsed

# -------- Main Execution --------
if __name__ == "__main__":
    input_line = input().strip()  # e.g., "6x3U 4x2U 8x4L 2x2H"
    houses_specs = parse_input(input_line)

    houses = []
    for length, height, direction in houses_specs:
        h = build_house(length, height)
        h_tilted = tilt_house(h, direction)
        houses.append(h_tilted)

    final_art = join_houses(houses)
    for row in final_art:
        print(row)
