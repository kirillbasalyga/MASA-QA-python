list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

not_even_numbers = list(filter(lambda x: x % 2 != 0, list_numbers))
kub = list(map(lambda x: x ** 3, not_even_numbers))
print(kub)