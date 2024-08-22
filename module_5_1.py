class House:
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        '''
        Нужно приехать на данный этаж\n
        params:
            new_floor - int
        '''
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)


h0 = House('ЖК Эльбрус', 30)
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h0.go_to(-2)
h1.go_to(5)
h2.go_to(10)
