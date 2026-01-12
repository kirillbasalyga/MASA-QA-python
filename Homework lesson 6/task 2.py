data = {"price": "10.5", "id": "abc"}
def get_as_float(data_dict, key):
    try:
        float(data_dict[key])
        print(f'Успех: Получено число 10.5')
    except ValueError:
        print('Ошибка: Значение по ключу id нельзя превратить в число!')
    except KeyError:
        print(f"Ошибка: Значение по ключу amount нельзя превратить в число!")

get_as_float(data, "price")
get_as_float(data, "id")
get_as_float(data, "amount")