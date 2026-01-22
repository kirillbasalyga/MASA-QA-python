
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(f"Invalid input format. Please enter a number.")


def get_valid_index(prompt, max_index):
    while True:
        try:
            prompt = int(input(prompt))
            if not max_index >= prompt >= 1:
                raise IndexError
            else:
                return prompt - 1
        except ValueError:
            print(f"Invalid input format. Please enter a integer number.")
        except IndexError:
            print(f"Please enter a number between 1 and {max_index}.")




