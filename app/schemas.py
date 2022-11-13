"""
    Shema for the API
"""

from datetime import date
from typing import  List, Optional, Union
from pydantic import BaseModel

#
#  ITEM
#
class ItemBase(BaseModel):
    """
        Item base model
    """
    name: str
    description: Union[str, None] = None

class ItemCreate(ItemBase):
    """
        Item creation
    """

class Item(ItemBase):
    """
        Item model
    """
    id: int
    trainer_id: int

    class Config:
        """
            Pydantic config
        """
        orm_mode = True

#
#  POKEMON
#
class PokemonBase(BaseModel):
    """
        Pokemon base model
    """
    api_id: int
    custom_name: Optional[str] = None

class PokemonCreate(PokemonBase):
    """
        Pokemon creation model
    """

class Pokemon(PokemonBase):
    """
        Pokemon model
    """
    id: int
    name: str
    trainer_id: int

    class Config:
        """
            Pydantic config
        """
        orm_mode = True
#
#  TRAINER
#
class TrainerBase(BaseModel):
    """
        Base schema for Trainer
    """
    name: str
    birthdate: date

class TrainerCreate(TrainerBase):
    """
        Create a new trainer
    """

class Trainer(TrainerBase):
    """
        Trainer class
    """
    id: int
    inventory: List[Item] = []
    pokemons: List[Pokemon] = []

    class Config:
        """
            ORM mode
        """
        orm_mode = True
