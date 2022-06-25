class Clothes:
    def __init__(self, name, country, color, size, price):
        self.name = name
        self.country = country
        self.color = color
        self.size = size
        self.price = price

    def __str__(self):
        return '%-15s %-15s %-10s %-8d %-8d' % (self.name, self.country, self.color, self.size, self.price)


def main_func():
    items = [Clothes("Джинси", "Італія", "Синій", 45, 800),
             Clothes("Футболка", "Іспанія", "Червоний", 50, 500),
             Clothes("Худі", "Бразилія", "Білий", 55, 890),
             Clothes("Футболка", "Італія", "Чорний", 47, 850),
             Clothes("Куртка", "Польща", "Червоний", 40, 2000),
             Clothes("Куртка", "Чорний", "Україна", 43, 2500)]
    printed(items)

    print("\nВідсотрований список речей за розміром")
    items.sort(key=lambda x: x.size)
    printed(items)

    print("\nВідсотрований список речей за ціною")
    items.sort(key=lambda x: x.price, reverse=True)
    printed(items)


def printed(items):
    print('%-15s %-15s %-10s %-8s %-8s' % ("Назва", "Виробництво", "Колір", "Розмір", "Ціна"))
    for i in range(0, len(items)):
        print(items[i])


main_func()

