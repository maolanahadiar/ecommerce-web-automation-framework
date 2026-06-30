from utils.data_generator import DataGenerator as Data

CHECKOUT_DATA = {
            "name": Data.full_name(),
            "country": Data.country(),
            "city": Data.city(),
            "card_number": Data.card_number(),
            "month": Data.month(),
            "year": Data.year(),
            "expected": "Thank you for your purchase!"
        }