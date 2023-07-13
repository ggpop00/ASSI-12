def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found!")
        return []

def write_file(file_path, data):
    try:
        with open(file_path, "a") as file:
            file.write(data)
    except FileNotFoundError:
        print(f"File '{file_path}' not found!")