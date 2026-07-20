from utils.data_generator import DataGenerator

BILLING_INFO = {
            "name": DataGenerator.full_name(),
            "country": DataGenerator.country(),
            "city": DataGenerator.city(),
            "card_number": DataGenerator.card_number(),
            "month": DataGenerator.month(),
            "year": DataGenerator.year(),
            "expected_message": "Thank you for your purchase!"
}