from src.model.rabbit import Rabbit


class GamePlay:
    def __init__(self, animal_type: str="rabbit", animal_name: str="Kimi") -> None:
        if animal_type != "rabbit":
            raise ValueError("rabbit is supportted only") # TODO: create a factory for animals
        
        self.animal = Rabbit(animal_name)

    def run(self) -> None:
        while True:
            pass # TODO: read the arcade docs