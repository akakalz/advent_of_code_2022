from advent_of_code_2022.day import Day


class Node:
    x: int
    y: int
    link: "Node"
    label: str

    def __init__(self, label: str):
        self.label = label

        self.x = 0
        self.y = 0
        self.link = None

    def move(self, direction: tuple[int, int]) -> None:
        self.x += direction[0]
        self.y += direction[1]

        if self.link:
            self.move_link()

    def move_link(self) -> None:
        move =self.calculate_move_link_to_head(self.position, self.link.position)
        self.link.move(move)

    def calculate_move_link_to_head(self, head_pos: tuple[int, int], link_pos: tuple[int, int]) -> tuple[int, int]:
        dist_apart = head_pos[0] - link_pos[0], head_pos[1] - link_pos[1]
        if abs(dist_apart[0]) + abs(dist_apart[1]) == 3:
            diag = True
        else:
            diag = False

        if dist_apart[0] > 1:
            x = 1
        elif dist_apart[0] < -1:
            x = -1
        else:
            x = 0

        if dist_apart[1] > 1:
            y = 1
        elif dist_apart[1] < -1:
            y = -1
        else:
            y = 0

        if diag:
            if not x:
                x = dist_apart[0]
            else:
                y = dist_apart[1]

        return x, y

    @property
    def position(self) -> tuple[int, int]:
        return self.x, self.y


class Rope:
    head: Node
    tail: list[Node]

    def __init__(self, segments: int = 2) -> None:
        self.head = Node("H")
        self.tail = [Node(str(i)) for i in range(1, segments)]
        self.head.link = self.tail[0]
        for idx in range(1, segments - 1):
            self.tail[idx - 1].link = self.tail[idx]

    def move_head(self, direction: tuple[int, int]) -> None:
        self.head.move(direction)


class Day9(Day):
    def part_1(self):
        rope = Rope(2)
        positions = set()
        for line in self.input_data:
            quantity, move = self.parse_move(line)
            for _ in range(quantity):
                rope.move_head(move)
                positions.add(rope.tail[-1].position)
        return len(positions)

    def part_2(self):
        rope = Rope(10)
        print(len(rope.tail))
        positions = set()
        for line in self.input_data:
            quantity, move = self.parse_move(line)
            for _ in range(quantity):
                rope.move_head(move)
                positions.add(rope.tail[-1].position)
        return len(positions)

    def parse_move(self, move_cmd: str) -> tuple[int, tuple[int, int]]:
        d, q = move_cmd.split(" ")
        if d == "R":
            move = (1, 0)
        elif d == "L":
            move = (-1, 0)
        elif d == "U":
            move = (0, 1)
        elif d == "D":
            move = (0, -1)
        return int(q), move
