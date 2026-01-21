
def get_valid_float(prompt):
    while True:
        try:
            prompt = input(prompt)
            return float(prompt)
        except ValueError:
            print(f"Invalid input format. Please enter a number.")


def get_valid_index(prompt, max_index):
    while True:
        try:
            return int(prompt) - 1
        except ValueError:
            print(f"Invalid input format. Please enter a integer number.")
        except 1 <= prompt <= max_index:
            print(f"Please enter a number between 1 and {max_index}.")




