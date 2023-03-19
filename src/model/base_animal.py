from dataclasses import dataclass
from enum import Enum, auto
from typing import TypeVar

TBaseAnimal = TypeVar("TBaseAnimal", bound="BaseAnimal")

class Mood(Enum):
    HAPPY = auto()
    SO_SO = auto()
    SAD = auto()
    COMMITTED_SUICEDE = auto()

class Vitality(Enum):
    HIGH = auto()
    SO_SO = auto()
    WEAK = auto()
    DEAD = auto()


@dataclass(frozen=True)
class BaseAnimal:
    name: str
    mood_score: int = 50
    vitality_score: int = 50

    _desease_vitality_change: int = -1
    _healing_vitality_change: int = 1
    _desease_mood_change: int = -1
    _healing_mood_change: int = 1

    _being_bored_mood_change: int = -1
    _playing_mood_change: int = 1

    def __post_init__(self) -> None:
        self._validate()

    def _validate(self) -> None:
        if self.mood_score < 0 or self.mood_score > 100:
            ValueError("Mood must be between 0 and 100")
        
        if self.vitality_score < 0 or self.vitality_score > 100:
            ValueError("Vitality must be between 0 and 100")

    def _evolve(self, mood_change: int=0, vitality_change: int=0) -> TBaseAnimal:
        return self.__class__(self.name, self.mood_score + mood_change, self.vitality_score + vitality_change)

    def has_desease(self) -> TBaseAnimal:
        return self._evolve(
            mood_change=self._desease_mood_change,
            vitality_change=self._desease_vitality_change,
        )
    
    def being_healed(self) -> TBaseAnimal:
        return self._evolve(
            mood_change=self._healing_mood_change,
            vitality_change=self._healing_vitality_change,
        )

    def being_bored(self) -> TBaseAnimal:
        return self._evolve(
            mood_change=self._being_bored_mood_change
        )
    
    def plays(self) -> TBaseAnimal:
        return self._evolve(
            mood_change=self._playing_mood_change
        )

    def get_vitality(self):
        match score := self.vitality_score:
            case _ if score >= 80:
                return Vitality.HIGH
            case _ if score >= 40:
                return Vitality.SO_SO
            case _ if score > 0:
                return Vitality.WEAK
            case _ if score == 0:
                return Vitality.DEAD

    def get_mood(self):
        match score := self.mood_score:
            case _ if score >= 80:
                return Mood.HAPPY
            case _ if score >= 40:
                return Mood.SO_SO
            case _ if score > 0:
                return Mood.SAD
            case _ if score == 0:
                return Mood.COMMITTED_SUICEDE

    def is_alive(self):
        return (
                self.get_mood != Mood.COMMITTED_SUICEDE
            and self.get_vitality != Vitality.DEAD
        )
    
