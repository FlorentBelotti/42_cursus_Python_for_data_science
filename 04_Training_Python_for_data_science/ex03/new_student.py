from dataclasses import dataclass, field
import random
import string


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __init__(self, name: str, surname: str, active: bool = True, **kwargs):
        if 'login' in kwargs or 'id' in kwargs:
            raise TypeError(
                f"TypeError: Student.__init__() got an unexpected keyword"
                f"argument '{ 'login' if 'login' in kwargs else 'id' }'"
            )
        if not name or not surname:
            raise ValueError("Both 'name' and 'surname' are required")
        if kwargs:
            raise TypeError(
                f"TypeError: Student.__init__() got an unexpected keyword "
                f"argument '{ list(kwargs.keys())[0] }'"
            )
        self.name = name
        self.surname = surname
        self.active = active
        self.__post_init__()

    def __post_init__(self):
        self.login = self.name[0].upper() + self.surname.lower()
        self.id = generate_id()
