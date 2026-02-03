from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy S25", "+79115823689"),
    Smartphone("Nokia", "N75", "+79112224455"),
    Smartphone("iPhone", "15", "+79113336677"),
    Smartphone("Xiaomi", "Redmi 15", "+79118889900"),
    Smartphone("Motorola", "G06", "+79111111111")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
