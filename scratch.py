from dataclasses import dataclass


@dataclass
class Person:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self):
        return self.price * self.quantity


p1 = Person("John", 50)
p2 = Person("John", 50)
p3 = Person("John", 50, 3)

print(p1)
print(p1.total_cost())
print(p1 == p2)
print(p1 == p3)
