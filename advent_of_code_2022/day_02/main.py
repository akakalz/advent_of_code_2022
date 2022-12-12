from advent_of_code_2022.day import Day


class Day2(Day):
    point_map = {
        "X": 1,
        "Y": 2,
        "Z": 3,
        True: 6,
        None: 3,
        False: 0,
    }

    def part_1(self):
        points = 0
        for line in self.input_data:
            play = line.split(" ")
            them, you = play[0], play[1]
            win_lose_draw = self.is_won_round(them, you)
            points += self.point_map[you] + self.point_map[win_lose_draw]
        return points

    def part_2(self):
        points = 0
        for line in self.input_data:
            play = line.split(" ")
            them, you = play[0], play[1]
            points += self.strategy(them, you)
        return points

    def is_won_round(self, them: str, you: str):
        if any([
            them == "A" and you == "X",
            them == "B" and you == "Y",
            them == "C" and you == "Z",
        ]):
            return None
        if them == "A" and you == "Y":
            return True
        if them == "B" and you == "Z":
            return True
        if them == "C" and you == "X":
            return True
        return False


    def strategy(self, them: str, you: str):
        win_lose_draw = {
            "X": False,
            "Y": None,
            "Z": True,
        }
        strat_map = {
            "X": {
                "A": "Z",
                "B": "X",
                "C": "Y",
            },
            "Y": {
                "A": "X",
                "B": "Y",
                "C": "Z",
            },
            "Z": {
                "A": "Y",
                "B": "Z",
                "C": "X",
            }
        }
        point_map = {
            "X": 1,
            "Y": 2,
            "Z": 3,
            True: 6,
            None: 3,
            False: 0,
        }
        the_play = strat_map[you][them]
        return point_map[win_lose_draw[you]] + point_map[the_play]
