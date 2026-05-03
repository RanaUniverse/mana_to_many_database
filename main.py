"""
main.py
Here i will write the code for makig the data
"""

from sqlmodel import (
    Session,
)


import fake_data

from database_code.models import TeamModel, HeroModel
from database_code.db_make import engine, create_db_and_tables


def create_hero():
    with Session(engine) as session:
        team1 = TeamModel(
            name=fake_data.get_a_full_name(),
            headquarters=fake_data.one_word(),
        )
        team2 = TeamModel(
            name=fake_data.get_a_full_name(),
            headquarters=fake_data.one_word(),
        )
        hero1 = HeroModel(
            name=fake_data.get_a_full_name(),
            secret_name=fake_data.one_word(),
            age=fake_data.age_int(),
            teams=[team1, team2],
        )
        hero2 = HeroModel(
            name=fake_data.get_a_full_name(),
            secret_name=fake_data.one_word(),
            age=fake_data.age_int(),
            teams=[team2],
        )
        hero3 = HeroModel(
            name=fake_data.get_a_full_name(),
            secret_name=fake_data.one_word(),
            age=fake_data.age_int(),
            teams=[team2],
        )

        session.add(hero1)
        session.add(hero2)
        session.add(hero3)
        session.commit()
        session.refresh(hero1)
        session.refresh(hero2)
        session.refresh(hero3)

        print("Hero 1", hero1)
        print("Hero 2", hero2)
        print("Hero 3", hero3)


def main():
    # create_db_and_tables()
    create_hero()


if __name__ == "__main__":
    main()
