shopping_list =["молоко", "хлеб", "яйца", "сыр", "масло"]
shopping_list.append("сок")
shopping_list.insert(1, 'йогурт')
shopping_list[2] = "батон"
shopping_list.remove("масло")
print(shopping_list[0], shopping_list[-1])
print(shopping_list[1:5])
shopping_list.sort()
print(f"{shopping_list} \nДлина списка покупок {len(shopping_list)}")
