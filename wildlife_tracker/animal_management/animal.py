from typing import Any, List, Optional  

class Animal:
    def __init__(self,
                 animal_id: int, 
                 species: str,
                 age: Optional[int] = None, 
                 habitats: Optional[List[int]] = None,
                 health_status: Optional[str] = None) -> None:
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status
        self.habitats = habitats or []

    def get_animal_by_id(animal_id: int) -> Optional['Animal']:
        pass

    def get_animal_details(self) -> dict[str, Any]:
        pass
    
    def update_animal_details(self, **kwargs: Any) -> None:
        pass

    def register_animal(self, animal: 'Animal') -> None:
        pass

    def remove_animal(self, animal_id: int) -> None:
        pass
