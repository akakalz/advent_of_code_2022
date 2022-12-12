def get_input(file_name: int):
    with open(file_name, 'r') as in_file:
        input_list = in_file.read().split('\n')
    return input_list


def pad_left(s: str, size: int, char: str = '0'):
    padding = size - len(s)
    return ''.join([char * (padding if padding > 0 else 0), s])
