import json
from advent_of_code_2022.day import Day


class CPU:
    def __init__(self, cmd_queue: list[str]) -> None:
        self.cmd_queue = cmd_queue

        self.register = 1
        self.cycle = 0
        self.cycle_checks = {20, 60, 100, 140, 180, 220}
        self.regsiter_at_checks: list[int] = []
        self.crt = [
            [],
            [],
            [],
            [],
            [],
            [],
        ]

    def run_cycles(self, part: int) -> None:
        for cmd in self.cmd_queue:
            if cmd == "noop":
                self.pass_cycle(part)
                self.cmd_noop()
            elif cmd.startswith("addx"):
                n = int(cmd.split(" ")[1])
                self.pass_cycle(part)
                self.pass_cycle(part)
                self.cmd_addx(n)

    def pass_cycle(self, part: int) -> None:
        self.cycle += 1
        if part == 1:
            if self.cycle in self.cycle_checks:
                self.regsiter_at_checks.append(self.cycle * self.register)
        elif part == 2:
            for lst in self.crt:
                if len(lst) < 40:
                    break
            col = ((self.cycle - 1) % 40)
            if col - 1 <= self.register <= col + 1:
                pixel = "#"
            else:
                pixel = "."
            lst.append(pixel)

    def cmd_noop(self) -> None:
        pass

    def cmd_addx(self, n: int) -> None:
        self.register += n


class Day10(Day):
    def part_1(self):
        cpu = CPU(self.input_data)
        cpu.run_cycles(1)
        return sum(cpu.regsiter_at_checks)

    def part_2(self):
        cpu = CPU(self.input_data)
        cpu.run_cycles(2)
        return json.dumps(["".join(x) for x in cpu.crt], indent=4)
