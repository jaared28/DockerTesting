from dataclasses import dataclass


@dataclass
class User:
    name: str
    id: int
    email: str
