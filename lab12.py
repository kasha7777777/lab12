import tkinter as tk
def z1():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана - {self.restaurant_name}, Кухня: {self.cuisine_type}")

    class RamenStand(Restaraunt):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ramen_flavors(self):
            print("Виды раменов:")
            print(*self.flavors, sep = "\n")

    type_ramen = RamenStand("A K I R A", "Японская", ["сио", "сею", "мисо"])
    type_ramen.ramen_flavors()

def z2():
    class Restaraunt:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Ресторан: {self.restaurant_name} | Кухня: {self.cuisine_type}")

    class RamenStand(Restaraunt):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = place
            self.time = time

        def describe_ramen_cafe(self):
            print(f"Ресторан: {self.restaurant_name} | Кухня: {self.cuisine_type} | Место: Осака, Япония | Время работы: 08:00 - 22:00")

        def ramen_flavors(self):
            print("Виды раменов:")
            print(*self.flavors, sep = "\n")

        def add(self):
            self.flavors.append(input("Добавить рамен: "))

        def delete(self):
            self.flavors.remove(input("Удалить рамен: "))

        def poisk(self):
            if input("Напишите новый рамен: ") in self.flavors:
                print("Есть в наличии")
            else:
                print("Нет в наличии")

    class ramen_fat(RamenStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, leight):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.leight = leight

        def fat(self):
            print("Жирность: ", self.leight)

    class ramen_size(RamenStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, place, time, height):
            super().__init__(restaurant_name, cuisine_type, flavors, place, time)
            self.height = height

        def size(self):
            print("Обьем порции: ", self.height)

    type_ramen = RamenStand("A K I R A", "Японская", ["сио", "сею", "мисо"], "Осака, Япония", "08:00 - 22:00")
    type_ramen.describe_ramen_cafe()
    type_ramen.ramen_flavors()
    type_ramen.poisk()

    p = ramen_fat("A K I R A", "Японская", ["сио", "сею", "мисо"], "Оска, Япония", "08:00 - 22:00", "750 ккал")
    p.fat()

    s = ramen_size("A K I R A", "Японская", ["сио", "сею", "мисо"], "Осака, Япония", "08:00 - 22:00", "Большой")
    s.size()

def z3():
    class RamenStand:
        def __init__(self):
            self.flavors = ["сио", "сею", "мисо"]
            self.prices = [50, 60, 70]

        def get_flavors(self):
            return self.flavors

        def get_prices(self):
            return self.prices

    class RamenStandGUI:
        def __init__(self, master):
            self.master = master
            master.title("RamenStand")

            self.ramen_stand =RamenStand()

            self.flavors_label = tk.Label(master, text="Рамен", font="Arial 12 bold")

            self.flavors_listbox = tk.Listbox(master, font="Helvetica 12", height=len(self.ramen_stand.get_flavors()))

            for flavor in self.ramen_stand.get_flavors():
                self.flavors_listbox.insert(tk.END, flavor)

            self.prices_label = tk.Label(master, text="Цена", font="Arial 12 bold")

            self.prices_listbox = tk.Listbox(master, font="Helvetica 12", height=len(self.ramen_stand.get_prices()))

            for price in self.ramen_stand.get_prices():
                self.prices_listbox.insert(tk.END, price)

            self.flavors_label.grid(row=0, column=0)
            self.flavors_listbox.grid(row=1, column=0)
            self.prices_label.grid(row=0, column=1)
            self.prices_listbox.grid(row=1, column=1)

    root = tk.Tk()
    ramen = RamenStandGUI(root)
    root.mainloop()

z3()