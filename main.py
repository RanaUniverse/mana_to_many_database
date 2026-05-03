"""
main.py
Here i will write the code for makig the data
"""

from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
    Session,
)


import fake_data
from database_code.db_make import engine, create_db_and_tables


class HeroTeamLink(SQLModel, table=True):
    __tablename__ = "hero_team_link"  # type: ignore

    hero_id: int | None = Field(
        default=None,
        foreign_key="hero_data.id_",
        primary_key=True,
    )
    team_id: int | None = Field(
        default=None,
        foreign_key="team_data.id_",
        primary_key=True,
    )


class TeamModel(SQLModel, table=True):
    __tablename__ = "team_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["HeroModel"] = Relationship(
        back_populates="teams",
        link_model=HeroTeamLink,
    )


class HeroModel(SQLModel, table=True):
    __tablename__ = "hero_data"  # type: ignore

    id_: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None

    teams: list["TeamModel"] = Relationship(
        back_populates="heroes",
        link_model=HeroTeamLink,
    )


# def create_hero_and_team():
#     with Session(engine) as session:
#         team_obj = TeamModel(
#             name=fake_data.get_a_full_name(),
#             headquarters=fake_data.one_word(),
#         )
#         hero_obj_1 = HeroModel(
#             name=fake_data.get_a_full_name(),
#             secret_name=fake_data.one_word(),
#         )
#         hero_obj_2 = HeroModel(
#             name=fake_data.get_a_full_name(),
#             secret_name=fake_data.one_word(),
#         )
#         team_obj.heroes.append(hero_obj_1)
#         team_obj.heroes.append(hero_obj_2)
#         session.add(team_obj)
#         session.commit()
#         session.refresh(team_obj)
#         print("Hero details are", team_obj.heroes)


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
    create_db_and_tables()
    create_hero()


if __name__ == "__main__":
    main()
