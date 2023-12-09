to_address = Address("12345", "New York", "Main Street", "123", "Apt 1")
from_address = Address("54321", "Los Angeles", "Oak Avenue", "456", "Apt 2")

mailing = Mailing(to_address, from_address, 20.50, "ABC123")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")