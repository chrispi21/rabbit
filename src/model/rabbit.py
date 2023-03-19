
from src.model.base_animal import BaseAnimal
from dataclasses import dataclass

@dataclass(frozen=True)
class Rabbit(BaseAnimal):

    _desease_vitality_change: int = -5
    _healing_vitality_change: int = 2
    _desease_mood_change: int = -1
    _healing_mood_change: int = 2

    _being_bored_mood_change: int = -1
    _playing_mood_change: int = 3


rabbit = Rabbit("Anetka")
    

