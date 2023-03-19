
from typing import TypeVar
from src.model.base_animal import TBaseAnimal
from enum import Enum, auto

TGameState = TypeVar("TGameState", bound="GameState")

class Action(Enum):
    NOOP = auto()
    SICKNESS = auto()
    HEALING = auto()
    PLAYING = auto()
    BEING_BORED = auto()

class GameOverException(RuntimeError): # TODO move to exceptions
    pass

class GameState:

    def __init__(self, animal: TBaseAnimal) -> None:
        self.animal = animal

    def play(self, action: Action) -> TGameState:
        if not self.animal.is_alive():
            raise GameOverException

        match action:
            case Action.NOOP:
                return self
            case Action.SICKNESS:
                return GameState(self.animal.has_desease())
            case Action.HEALING:
                return GameState(self.animal.being_healed())
            case Action.PLAYING:
                return GameState(self.animal.plays())
            case Action.BEING_BORED:
                return GameState(self.animal.being_bored())

    