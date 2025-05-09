"""
Database module.
"""
import sqlite3
from typing import Dict, Any, List, Iterator, ContextManager
from contextlib import contextmanager


class Database:
    def __init__(self, database_name: str):
        self.database_name = database_name
        self.connection = None
        self.cursor = None

    @contextmanager
    def connection_scope(self) -> Iterator[sqlite3.Cursor]:
        self.connect()
        try:
            yield self.cursor
            self.connection.commit()
        except sqlite3.Error as e:
            self.connection.rollback()
            raise e

    def connect(self) -> None:
        if not self.connection:
            self.connection = sqlite3.connect(self.database_name)
            self.cursor = self.connection.cursor()

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def create(self, table: str, data: dict[str, any]) -> int | None:
        with self.connection_scope() as cursor:
            columns = ", ".join(data.keys())
            placeholders = ", ".join("?" * len(data.keys()))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cursor.execute(query, list(data.values()))
            return cursor.lastrowid

    """
    SELECT exercise.id, exercise.name, category.name AS category_name
    FROM tasks
    INNER JOIN categories ON tasks.category_id = categories.id
    WHERE categories.name = ? OR tasks.name = ?
    """
    join = {"exercise": ["id", "name"], "category": ["name"]}
    query = ""
    for table in join:
        for field in join[table]:
            print()

    def read(self, table: str, join: dict[str, any] = None, conditions: dict[str, any] = None) -> list[dict[str, any]]:
        with self.connection_scope() as cursor:
            if join:
                query = f"SELECT {f', '.join(f'{table}.{value}' for value in join[table])}, "
            query = f"SELECT * FROM {table}"
            params = []
            if conditions:
                where_clause = " AND ".join(f"{k} = ?" for k in conditions)
                query += f" WHERE {where_clause}"
                params = list(conditions.values())
            try:
                cursor.execute(query, params)
                columns = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                return [dict(zip(columns, row)) for row in rows]
            except sqlite3.Error as e:
                print(f"Failed to read from table '{table}'. Error: {e}")
                return []

    def update(self, table: str, data: dict[str, any], conditions: dict[str, any]) -> int:
        with self.connection_scope() as cursor:
            set_clause = ", ".join([f"{k} = ?" for k in data.keys()])
            where_clause = " AND ".join(f"{k} = ?" for k in conditions.keys())
            query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            params = list(data.values()) + list(conditions.values())
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.rowcount

    def delete(self, table: str, conditions: dict[str, any]) -> int:
        with self.connection_scope() as cursor:
            where_clause = " AND ".join(
                [f"{k} = ?" for k in conditions.keys()]
                )
            query = f"DELETE FROM {table} WHERE {where_clause}"
            cursor.execute(query, list(conditions.values()))
            self.connection.commit()
            return cursor.rowcount
