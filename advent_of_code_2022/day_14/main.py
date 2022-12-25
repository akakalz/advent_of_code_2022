from advent_of_code_2022.day import Day


class Day14(Day):
    offset = 0
    max_x = 0
    min_x = 0

    def part_1(self):
        slice = self.parse_input()
        return self.drop_sand(slice)

    def part_2(self):
        slice = self.parse_input(with_floor=True)
        return self.drop_sand(slice)

    def parse_input(self, with_floor: bool = False) -> list[list]:
        max_x = max_y = 0
        min_x = min_y = 99999
        coords = []
        for line in self.input_data:
            tuples = line.split(" -> ")
            for tup in tuples:
                x, y = tup.split(",")
                x, y = int(x), int(y)
                coords.append((x, y))
                max_x = max(max_x, x)
                max_y = max(max_y, y)
                min_x = min(min_x, x)
                min_y = min(min_y, y)
            coords.append(None)
        self.offset = min_x
        self.min_x = min_x
        self.max_x = max_x
        rocks = set()
        prior_coord = None
        if with_floor:
            max_y += 2
            # coords.extend([(0, max_y), (max_x, max_y), None])
        for coord in coords:
            if coord is None:
                prior_coord = None
                continue
            if prior_coord:
                if coord[0] == prior_coord[0]:
                    start_y = min(prior_coord[1], coord[1])
                    end_y = max(prior_coord[1], coord[1])
                    for i in range(end_y - start_y + 1):
                        new_coord = (prior_coord[0], start_y + i)
                        rocks.add(new_coord)
                else:
                    start_x = min(prior_coord[0], coord[0])
                    end_x = max(prior_coord[0], coord[0])
                    for i in range(end_x - start_x + 1):
                        new_coord = (start_x + i, prior_coord[1])
                        rocks.add(new_coord)
                prior_coord = coord
            else:
                prior_coord = coord
        return self.create_slice(rocks, max_x + 500, max_y, with_floor=with_floor)

    def create_slice(self, rock_coords: set, max_x: int, max_y: int, with_floor: bool = False) -> list[list[str]]:
        slice: list[list[str]] = []
        for y in range(max_y + 1):
            slice.append([])
            for x in range(max_x + 1):
                if (x, y) in rock_coords:
                    slice[y].append("#")
                else:
                    slice[y].append(".")
        if with_floor:
            slice[-1] = ["#" for _ in range(len(slice[-1]))]
        return slice

    def drop_sand_particle(self, slice: list[list[str]]) -> bool:
        y = 0
        x = 500
        stopped = False
        while y < len(slice) and not stopped:
            if (slice[0][500] == "o") or (y + 1 >= len(slice)):
                return False
            if slice[y + 1][x] != ".":
                left_path = (x - 1, y + 1)
                right_path = (x + 1, y + 1)
                if x + 1 >= len(slice[0]):
                    slice[y][x] = "o"
                    y += 1
                    continue
                left_empty = bool(slice[left_path[1]][left_path[0]] == ".")
                right_empty = bool(slice[right_path[1]][right_path[0]] == ".")
                if left_empty:
                    x -= 1
                    y += 1
                    continue
                elif not left_empty and right_empty:
                    x += 1
                    y += 1
                    continue
                else:
                    slice[y][x] = "o"
                    stopped = True
            else:
                y += 1
        return True

    def drop_sand(self, slice: list[list[str]]) -> int:
        sand_stopped = 0
        check = True
        while check:
            check = self.drop_sand_particle(slice)
            if check:
                sand_stopped += 1
        return sand_stopped
