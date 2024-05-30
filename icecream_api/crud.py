def read(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write(file_path: str, data: str):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)
