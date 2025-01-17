class OrderDetails:
    @classmethod
    def details_1(cls):
        return cls(
            'Людмила',
            'Гребенщикова',
            'ул. Пушкина, д. Колотушкина',
            'Парк культуры',
            '+385445647382',
            20,
            'сутки',
            'black',
            'Hello'
        )

    @classmethod
    def details_2(cls):
        return cls(
            'Федор',
            'Гребенщикова',
            'ул. Пушкина, д. Колотушкина',
            'Парк культуры',
            '+385445647384',
            21,
            'трое суток',
            'grey',
            'Hello'
        )

    def __init__(self, name, last_name, address, station, phone_number, day, period, color, comment):
        self.name = name
        self.last_name = last_name
        self.address = address
        self.station = station
        self.phone_number = phone_number
        self.day = day
        self.period = period
        self.color = color
        self.comment = comment


class Locators:
