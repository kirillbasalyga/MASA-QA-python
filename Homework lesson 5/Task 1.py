contacts = {
    "Anna" : {
        "name": "Анна Иванова",
        "phone": "+79001234567",
        "email": "anna.ivanova@example.com"
    },
    "Petr":{
        "name": "Петр Сидоров",
        "phone": "+79119876543",
        "email": "petr.sidorov@example.com"
    }
}


print(contacts["Anna"])
contacts["Petr"]["phone"] = "+79225551122"
contacts["Anna"]["address"] = "г.Москва, ул. Пушкина, д. 10"
del contacts["Petr"]["email"]
print(contacts)