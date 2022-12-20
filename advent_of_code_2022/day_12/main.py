# from copy import deepcopy
from advent_of_code_2022.day import Day


class Map:
    def __init__(self, map: list[list[str]], start_pos: tuple[int, int], end_pos: tuple[int, int]) -> None:
        self.map = map
        self.start_pos = start_pos
        self.end_pos = end_pos
        e_pos = (0, 20)
        self.map[e_pos[1]] = self.map[e_pos[1]][:e_pos[0]] + "a" + self.map[e_pos[1]][e_pos[0] + 1:]
        self.map[end_pos[1]] = self.map[end_pos[1]][:end_pos[0]] + "z" + self.map[end_pos[1]][end_pos[0] + 1:]
        self.x_bound = len(self.map[0]) - 1
        self.y_bound = len(self.map) - 1
        self.ever_visited = set()

    def shortest_path(self) -> int:
        self.ever_visited = set()
        paths: list[list[tuple[int, int]]] = []
        for candidate in self.find_candidate_moves(self.start_pos):
            paths.append([candidate])
        steps = 1

        while paths and not any([path for path in paths if path and path[-1] == self.end_pos]):
            paths_to_trim = []
            for idx in range(len(paths)):
                if not paths[idx]:
                    paths_to_trim.append(idx)
                    continue
                candidates = self.find_candidate_moves(paths[idx][-1])
                if not candidates:
                    paths_to_trim.append(idx)
                    continue
                if len(candidates) == 1:
                    paths[idx].extend(candidates)
                else:
                    for candidate in candidates:
                        new_path = [x for x in paths[idx]] + [candidate]
                        paths.append(new_path)
                    paths_to_trim.append(idx)  # getting rid of the orig path
            steps += 1
            for path in sorted(paths_to_trim, reverse=True):
                paths.pop(path)
        return steps

    def find_candidate_moves(
        self,
        pos: tuple[int, int],
    ) -> list[tuple[int, int]]:
        candidates = []
        directions = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )
        for dir in directions:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if not all([
                0 <= new_pos[0] <= self.x_bound,
                0 <= new_pos[1] <= self.y_bound,
                new_pos not in self.ever_visited,
            ]):
                continue
            if ord("a") <= ord(self.map[new_pos[1]][new_pos[0]]) <= ord(self.map[pos[1]][pos[0]]) + 1:
                candidates.append(new_pos)
                self.ever_visited.add(new_pos)
        return candidates


class Day12(Day):
    def part_1(self):
        map_, start_pos, end_pos = self.parse_input()
        map = Map(map_, start_pos, end_pos)
        return map.shortest_path()

    def part_2(self):
        map_, start_pos, end_pos = self.parse_input()
        answer = 380
        # all the Bs are on the left edge on column 1
        # so using only the As on column 0
        starts = (
            (0, i)
            for i in range(41)
            if i != start_pos[1]
        )
        for start in starts:
            map = Map(map_, start, end_pos)
            answer = min(answer, map.shortest_path())
        return answer

    def parse_input(self) -> tuple[list[list[str]], tuple[int, int], tuple[int, int]]:
        for y, line in enumerate(self.input_data):
            if "S" in line:
                start_y = y
                start_x = line.index("S")
            if "E" in line:
                end_y = y
                end_x = line.index("E")
        return (
            [
                line
                for line in self.input_data
            ],
            (start_x, start_y),
            (end_x, end_y),
        )
