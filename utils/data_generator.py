from faker import Faker
from datetime import datetime
import random

fake = Faker()

class DataGenerator:

    @staticmethod
    def full_name():
        return fake.name()

    @staticmethod
    def phone_number(prefix="+628", length=10):
        return prefix + "".join(random.choices("0123456789", k=length))
    
    @staticmethod
    def email():
        return fake.email()

    @staticmethod
    def card_number():
        return fake.credit_card_number(card_type="visa")
    
    @staticmethod
    def country():
        return fake.country()
    
    @staticmethod
    def city():
        return fake.city()
    
    @staticmethod
    def month():
        return str(datetime.now().month)
    
    @staticmethod
    def year():
        return str(datetime.now().year)