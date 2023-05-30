class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("Название ресторана: ",self.restaurant_name,"\nТип кухни:  ", self.cuisine_type)
    def open_restaurant(self):
        print("Ресторан открыт")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, time):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["шоколадное", "фисташковое"]
        self.location = location
        self.time = time
    def print_flavors(self):
        print("Вкусы мороженого:")
        for flavor in self.flavors:
            print(flavor)
    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)
        print("\nБыло добавлено в список вкусов мороженого - ",new_flavor)
    def remove_flavor(self, removed_flavor):
        self.flavors.remove(removed_flavor)
        print("Было удалено из списка вкусов мороженого - ",removed_flavor)
    def has_flavor(self, flavor):
        if flavor in self.flavors:
            print("\nРесторан -",self.restaurant_name, "имеет в ассортименте вкус:", flavor)
        else:
            print("Ресторан -",self.restaurant_name, "не имеет в ассортименте вкус:", flavor)

class IceCreamOnStick(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, location, time, stick_type):
        super().__init__(restaurant_name, cuisine_type, location, time)
        self.stick_type = stick_type

    def display_stick_type(self):
        print("\nРесторан использует", self.stick_type, "палочки для мороженого на палочке")

    def change_stick_type(self, new_type):
        self.stick_type = new_type
        print("Ресторан использует новые", new_type, "палочки для мороженого на палочке")


class SoftServeIceCream(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, location, hours, toppings):
        super().__init__(restaurant_name, cuisine_type, location, hours)
        self.toppings = toppings

    def display_toppings(self):
        print("\nТопинги: ")
        for topping in self.toppings:
            print(topping)

    def add_topping(self, new_topping):
        self.toppings.append(new_topping)
        print("\nБыл добавлен в список топингов - ",new_topping)

    def remove_topping(self, removed_topping):
        self.toppings.remove(removed_topping)
        print("Был удалён из списка топингов - ",removed_topping)


my_ice_cream_stand = IceCreamStand("Мороженое", "Кафе-мороженное", "Папанина 13", "11:00 - 23:00")
my_ice_cream_stand.print_flavors()
my_ice_cream_stand.add_flavor("ореховое")
my_ice_cream_stand.has_flavor("клубничное")


my_ice_cream_on_stick = IceCreamOnStick("Мороженое", "Кафе-мороженное", "Папанина 13", "11:00 - 23:00", "деревянные")
my_ice_cream_on_stick.display_stick_type()
my_ice_cream_on_stick.change_stick_type("пластик")

my_soft_serve = SoftServeIceCream("Мороженое", "Кафе-мороженное", "Папанина 13", "11:00 - 23:00",
                                  ["клубничный сироп", "шоколадный сироп", "карамельный сироп","глазурь"])


my_soft_serve.display_toppings()
my_soft_serve.add_topping("манговый сироп")
my_soft_serve.remove_topping("глазурь")