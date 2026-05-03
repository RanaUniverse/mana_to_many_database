"""
database_code/models.py
Here i will write the code related to the models
class here in this place
"""

from sqlmodel import (
    SQLModel,
    Field,
    Relationship,
)


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
