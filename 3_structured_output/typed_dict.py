from typing import TypedDict

class Person (TypedDict):
    name: str
    age: int

obj: Person = {
    'age':1,
    'name': 1
}
print(obj)