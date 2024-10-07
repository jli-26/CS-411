from typing import Optional, List

from wildlife_tracker.habitat_management.habitat import Habitat


class HabitatManager:
    def __init__(self) -> None:
        habitats: Dict[int, Habitat] = {}

    def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass

    def remove_habitat(habitat_id: int) -> None:
        pass

    def get_habitat_by_id(habitat_id: int) -> Habitat:
        pass

    def assign_animals_to_habitat(self, animals: List[Animal]) -> None:
        pass
