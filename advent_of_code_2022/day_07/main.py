from advent_of_code_2022.day import Day


class Directory:
    def __init__(self, name: str, parent: "Directory"):
        self.name = name
        self.parent = parent
        self.files: list[File] = []
        self.sub_directories: list["Directory"] = []

    @property
    def total_size(self) -> int:
        total = 0
        for file in self.files:
            total += file.size
        for dir in self.sub_directories:
            total += dir.total_size
        return total


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Day7(Day):
    def part_1(self):
        root = Directory("root", None)
        cwd = root
        for line in self.input_data:
            cwd = self.handle_line(cwd, line)
        candidates = self.search_file_system_for_candidate_dirs(root, 100_000)
        return sum(candidate[1] for candidate in candidates)

    def part_2(self):
        MAX_SIZE = 70_000_000
        SIZE_NEEDED = 30_000_000
        root = Directory("root", None)
        cwd = root
        for line in self.input_data:
            cwd = self.handle_line(cwd, line)
        root_size = root.total_size
        candidates = self.search_file_system_for_candidate_dirs(
            root,
            SIZE_NEEDED - (MAX_SIZE - root_size),
            under=False,
        )
        candidates = sorted(candidates, reverse=True, key=lambda x: x[1])
        return candidates[-1][1]

    def handle_line(self, cwd: Directory, line: str) -> Directory:
        if line.startswith("$"):
            return self.handle_command(cwd, line)
        elif line[0].isalpha():
            return self.handle_directory(cwd, line)
        elif line[0].isnumeric():
            return self.handle_file(cwd, line)

    def search_file_system_for_candidate_dirs(self, root: Directory, limit: int, under: bool = True) -> list[tuple[Directory, int]]:
        dir_collection: set[Directory] = set()
        candidates: list[tuple[Directory, int]] = []
        self.search_helper(root, dir_collection)
        for dir in dir_collection:
            size = dir.total_size
            if under:
                if size <= limit:
                    candidates.append((dir, size))
            else:
                if size >= limit:
                    candidates.append((dir, size))
        return candidates

    def search_helper(self, dir: Directory, dir_collection: set) -> None:
        for sub_dir in dir.sub_directories:
            dir_collection.add(sub_dir)
            self.search_helper(sub_dir, dir_collection)

    def handle_command(self, cwd: Directory, cmd: str) -> Directory:
        if cmd == "$ ls":
            return cwd
        if cmd == "$ cd /":
            while cwd.parent:
                cwd = cwd.parent
            return cwd
        if cmd == "$ cd .." and cwd.parent:
            return cwd.parent
        elif cmd == "$ cd .." and not cwd.parent:
            return cwd
        if cmd.startswith("$ cd "):
            name = cmd.split(" ")[2]
            new_dir = [sub_dir for sub_dir in cwd.sub_directories if sub_dir.name == name][0]
            return new_dir

    def handle_directory(self, cwd: Directory, dir: str) -> Directory:
        splits = dir.split(" ")
        the_dir = Directory(name=splits[1], parent=cwd)
        cwd.sub_directories.append(the_dir)
        return cwd

    def handle_file(self, cwd: Directory, file: str) -> Directory:
        splits = file.split(" ")
        the_file = File(name=splits[1], size=int(splits[0]))
        cwd.files.append(the_file)
        return cwd
