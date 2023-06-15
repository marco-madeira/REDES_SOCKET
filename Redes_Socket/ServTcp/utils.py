def get_number_of_lines(file_name: str):
    with open(f"database/{file_name}.txt") as file:
        return sum(1 for l in file) 