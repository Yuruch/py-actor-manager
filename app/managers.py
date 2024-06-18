import sqlite3

from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self._connection = sqlite3.connect("cinema.sqlite")
        self.table = "actors"

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table} (first_name, last_name) "
            f"VALUES (?, ?) ",
            (first_name, last_name)
        )
        self._connection.commit()

    def all(self) -> list[Actor]:
        cursor = self._connection.execute(
            f"SELECT * FROM {self.table}"
        )
        return [
            Actor(*row) for row in cursor
        ]

    def update(
            self,
            id_to_update: str,
            first_name: str,
            last_name: str
    ) -> None:
        self._connection.execute(
            f"UPDATE {self.table} "
            f"SET first_name = ?, last_name = ? "
            f"WHERE id = ?",
            (first_name, last_name, id_to_update)
        )
        self._connection.commit()

    def delete(self, id_to_delete: str) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table} "
            f"WHERE id = ?",
            (id_to_delete,)
        )
        self._connection.commit()