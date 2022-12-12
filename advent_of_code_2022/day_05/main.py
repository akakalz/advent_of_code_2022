from advent_of_code_2022.day import Day


class Day5(Day):
    def part_1(self):
        stacks, instructions = self.get_initial_state_and_instructions()
        for instruction in instructions:
            self.apply_instruction(
                stacks=stacks,
                instruction=self.parse_instruction(instruction)
            )
        return "".join(stack[-1] if stack else " " for stack in stacks)

    def part_2(self):
        stacks, instructions = self.get_initial_state_and_instructions()
        for instruction in instructions:
            self.apply_instruction_part_2(
                stacks=stacks,
                instruction=self.parse_instruction(instruction)
            )
        return "".join(stack[-1] if stack else " " for stack in stacks)

    def get_initial_state_and_instructions(self) -> tuple[list[list], list[str]]:
        append_to_state = True
        state = []
        instructions = []
        for line in self.input_data:
            if not line:
                append_to_state = False
                continue
            if append_to_state:
                state.append(line)
            else:
                instructions.append(line)
        return self.construct_initial_state(state), instructions

    def construct_initial_state(self, strings: list[str]) -> list[list]:
        stacks = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        ]
        indexes = (1, 5, 9, 13, 17, 21, 25, 29, 33)
        for line in strings[-2::-1]:
            for stack, line_idx in enumerate(indexes):
                if line[line_idx] != " ":
                    stacks[stack].append(line[line_idx])
        return stacks

    def parse_instruction(self, instruction: str) -> tuple[int, int, int]:
        """returns tuple (quantity, source stack #, destination stack #)"""
        commands = instruction.split(" ")
        # -1 for index normalization
        return (int(commands[1]), int(commands[3]) - 1, int(commands[5]) - 1)

    def apply_instruction(self, stacks: list[list], instruction: tuple[int, int, int]) -> None:
        for _ in range(instruction[0]):
            try:
                moved = stacks[instruction[1]].pop()
                stacks[instruction[2]].append(moved)
            except IndexError:
                continue

    def apply_instruction_part_2(self, stacks: list[list], instruction: tuple[int, int, int]) -> None:
        moved = stacks[instruction[1]][-1 * instruction[0]:]
        stacks[instruction[2]].extend(moved)
        for _ in range(instruction[0]):
                stacks[instruction[1]].pop()
