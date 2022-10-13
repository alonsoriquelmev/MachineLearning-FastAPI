from pydantic import BaseModel


class PkRequest(BaseModel):
    hitpoints: int
    attack: int
    defense: int
    specattack: int
    specdefense: int
    speed: int