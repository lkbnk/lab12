class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Название ресторана: ",self.restaurant_name,"\nТип кухни: ", self.cuisine_type, "\n")


class IceCreamStand(restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["шоколадное", "фисташковое"]
    def print_flavors(self):
        print("Вкусы мороженого:")
        for flavor in self.flavors:
            print(flavor)

stand = IceCreamStand("Мороженое", "Кафе-мороженное")
stand.describe_restaurant()
stand.print_flavors()