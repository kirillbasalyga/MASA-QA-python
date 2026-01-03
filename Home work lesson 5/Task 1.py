Anna = {
    "name": "Анна Иванова",
    "phone": "+79001234567",
    "email": "anna.ivanova@example.com"
}

Petr = {
    "name": "Петр Сидоров",
    "phone": "+79119876543",
    "email": "petr.sidorov@example.com"
}

print(Anna)
Petr["phone"] = "+79225551122"
Anna["address"] = "г.Москва, ул. Пушкина, д. 10"
del Petr["email"]

print(f"{Anna}, \n{Petr}")