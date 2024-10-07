from typing import Optional, Dict

from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationPath:

    def __init__(self, 
                 path_id: int, 
                 species: str, 
                 start_location: Habitat, 
                 destination: Habitat, 
                 current_date: str,
                 current_location: str,
                 migration_path: 'MigrationPath',
                 duration: Optional[int] = None)->None:
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration
        self.current_date = current_date
        self.current_location = current_location
        self.migration_path=migration_path 

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    def get_migration_paths_by_destination(destination: Habitat) -> list['MigrationPath']:
        pass

    def get_migration_paths_by_species(species: str) -> list['MigrationPath']:
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list['MigrationPath']:
        pass

    def get_migrations_by_current_location(current_location: str) -> list['Migration']:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list['Migration']:
        pass

    def get_migrations_by_start_date(start_date: str) -> list['Migration']:
        pass

    def get_migrations_by_status(status: str) -> list['Migration']:
        pass

    def get_migration_path_details(path_id) -> dict:
        pass

    def update_migration_path_details(path_id: int, **kwargs) -> None:
        pass