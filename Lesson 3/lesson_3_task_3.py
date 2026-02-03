from adress import Adress
from mailing import Mailing

to_address = Adress("160000", "Москва", "Ленинградская", "63", "120")
from_address = Adress("160234", "Воронеж", "Пушкина", "12", "71")
cost = "12500"
track = "125698756"

my_mailing = Mailing(to_address, from_address, cost, track)

print(
 f"Отправление {track} из {from_address.index}, {from_address.city}, "
 f"{from_address.street}, {from_address.house} - {from_address.apartment} "
 f"в {to_address.index}, {to_address.city}, {to_address.street}, "
 f"{to_address.house} - {to_address.apartment}. Стоимость {cost} рублей."
)
