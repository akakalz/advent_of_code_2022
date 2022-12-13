from advent_of_code_2022.day import Day
from math import prod

class Tree:
    def __init__(self, height: int) -> None:
        self.height = height

        self.marked = False


class Day8(Day):
    def part_1(self):
        forest = self.setup_forest()
        # horizontal
        for line in forest:
            self.mark_trees(line)
            self.mark_trees(line[::-1])
        # vertical
        cols = len(forest[0])
        for col in range(cols):
            self.mark_trees([line[col] for line in forest])
            self.mark_trees([line[col] for line in forest[::-1]])
        return self.count_marked_trees(forest)

    def part_2(self):
        forest = self.setup_forest()
        max_view_score = 0
        rows = len(forest)
        cols = len(forest[0])
        for y, line in enumerate(forest):
            for x in range(len(line)):
                tree_lines = self.generate_rows_from_location(x, y, rows, cols, forest)
                max_view_score = max(
                    prod(
                        [
                            self.viewable_trees_from_height(tree_line, forest[y][x].height)
                            for tree_line in tree_lines
                        ]
                    ),
                    max_view_score,
                )
        return max_view_score

    def setup_forest(self) -> list[list[Tree]]:
        forest = []
        for line in self.input_data:
            forest.append([Tree(int(tree)) for tree in line])
        return forest

    def mark_trees(self, tree_line: list[Tree]) -> None:
        max_height = -999999
        for tree in tree_line:
            if tree.height > max_height:
                tree.marked = True
                max_height = max(tree.height, max_height)

    def viewable_trees_from_height(self, tree_line: list[Tree], height: int) -> int:
        count = 0
        for tree in tree_line:
            if tree.height < height:
                count += 1
            if tree.height >= height:
                count += 1
                break
        return count

    def count_marked_trees(self, forest: list[list[Tree]]) -> int:
        count = 0
        for line in forest:
            for tree in line:
                if tree.marked:
                    count += 1
        return count

    def generate_rows_from_location(self, x: int, y: int, max_x: int, max_y: int, forest: list[list[Tree]]) -> list[list[Tree]]:
        # up
        if y > 0:
            up = [
                line[x] for line in forest[y - 1::-1]
            ]
        else:
            up = []
        # down
        if y < max_y:
            down = [
                line[x] for line in forest[y + 1:]
            ]
        else:
            down = []
        # left
        if x > 0:
            left = [
                tree for tree in forest[y][x - 1::-1]
            ]
        else:
            left = []
        # right
        if x < max_x:
            right = [
                tree for tree in forest[y][x + 1:]
            ]
        else:
            right = []
        return [up, down, left, right]
