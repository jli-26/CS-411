from typing import Optional

from wildlife_tracker.migration_tracker.migration import Migration
from wildlife_tracker.migration_tracker.migration_path import MigrationPath


class MigrationManager:

     def __init__(self) -> None:
        migrations: Dict[int, Migration] = {}
        paths: Dict[int, MigrationPath] = {} 


    def get_migration_by_id(migration_id: int) -> Migration:
        pass

    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass
    
    def update_migration_details(migration_id: int, **kwargs: Any) -> None:
        pass

    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass