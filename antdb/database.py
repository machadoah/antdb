from typing import Dict, List, Type

from pydantic import BaseModel

from antdb import Table


class DataBase:
    def __init__(self, name: str):
        self.name = name
        self.tables: Dict[str, Table] = {}

    def create_table(self, name: str, model: Type[BaseModel]) -> Table:
        if name in self.tables:
            raise ValueError(f"Table '{name}' already exists")
        table = Table(name, model)
        self.tables[name] = table
        return table

    def drop_table(self, name: str) -> None:
        if name not in self.tables:
            raise ValueError(f"Table '{name}' does not exist")
        del self.tables[name]

    def get_table(self, name: str) -> Table:
        if name not in self.tables:
            raise ValueError(f"Table '{name}' does not exist")
        return self.tables[name]

    def list_tables(self) -> List[str]:
        return list(self.tables.keys())
