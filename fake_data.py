"""
This file is for generating some
random fake data, and i will use the value to
store the fake data into the database
"""

from faker import Faker

fake = Faker()


def get_a_full_name() -> str:
    output = fake.name()
    return output


def one_word() -> str:
    output = fake.word()
    return output


def age_int() -> int:
    output = fake.random_number(
        digits=2,
        fix_len=True,
    )
    return output
