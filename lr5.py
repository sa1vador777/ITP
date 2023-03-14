import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def diameter(self):
        return 2 * self.radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def __str__(self):
        return f"Сфера с радиусом: {self.radius}"
    
"Вызов экземпляра класса"

def call() -> str:
    s = Sphere(int(input("Введите радиус сферы: ")))
    print(s)
    print(f"Радиус: {s.radius}")
    print(f"Volume: {s.volume()}")
    print(f"Diameter: {s.diameter()}")
    print(f"Surface area: {s.surface_area()}")

if __name__ == "__main__":
    call()
