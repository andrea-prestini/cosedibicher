from dataclasses import dataclass, field


@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)

    name: str
    age: int
    iq: int = 100
    can_vote: bool = field(init=False)

    def __post_init__(self):
        self.can_vote = 18 <= self.age <= 70
        # sort by age
        self.sort_index = self.age


members = [
    Person(name="andrea", age=52),
    Person(name="pio", age=72),
    Person(name="roberto", age=40),
    Person(name="sofia", age=6),
]

sorted_members = sorted(members)
for member in sorted_members:
    print(f'{member.name}(age={member.age})')
