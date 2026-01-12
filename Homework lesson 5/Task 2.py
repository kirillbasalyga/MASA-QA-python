city_str = input("Напишите 5 городов через запятую")
city_list = city_str.split(",")

for i in range(5):
    city = city_list[i]
    if city.lower().find("a") != -1:
        print(f"Город {i + 1}: {city_list[i]} (в это городе есть 'a')")
    else:
        print(f"Город {i + 1}: {city_list[i]}")