class Car:
    def __init__(self, model: str, year: int, color: str, for_sale: bool):
        self.model: str = model
        self.year: int = year
        self.color: str = color
        self.for_sale: bool = for_sale

    def drive(self):
        print(f"The {self.year} {self.color} {self.model} is driving")

    def stop(self):
        print(f"The {self.year} {self.color} {self.model} is stopped")
