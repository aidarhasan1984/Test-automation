from address import Address
from mailing import Mailing

# Создание экземпляра класса Address для адреса получателя
to_address = Address("123456", "Москва", "Проходная улица", "10", "20")

# Создание экземпляра класса Address для адреса отправителя
from_address = Address("654321", "Санкт-Петербург", "Усадебная улица", "5", "10")

# Создание экземпляра класса Mailing
mailing = Mailing(to_address, from_address, 500, "1234567890")

# Вывод информации о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - "
f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, - {mailing.to_address.apartment}. "
f"Стоимость рублей.")