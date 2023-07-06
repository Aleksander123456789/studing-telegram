class Ingridient():
    def __init__(self, calories: float, mass: float ):
        print('Вызывается метод инит  у ингридиентовS')
        self._calories = calories
        self._mass = mass

    def prepare(self):
        #Подготавливать еду к приготовлению
        return self._calories
    
    def get_calories(self):
        #Возвращает калории
        return self._calories
    
    def get_mass(self):
        #Возвращает массу
        return self._mass

class Bread(Ingridient):
    def prepare(self):
        self._calories += 10
        self._mass *= 0.8
        return super().prepare()

class Tomato(Ingridient):
    def __init__(self, calories: float, mass: float, color: str):
        print('Вызывается метод инит у томата')
        self._color = color
        super().__init__(calories, mass)
    
    def prepare(self):
        self._mass -+ 10
    
class Soup(Ingridient):
    def __init__(self, calories: float, mass: float,)
    print('Вызывается метод инит у супа')
    self._salinity = salinity
    super(.__init__(calories, mass))

def cook(ings: list[Ingridient])
    for ing in ings:
        print(type(ing))
        print(ing.prepare())
        print(ing.get_mass())

def main():
    bread = Bread(100, 54)
    soup = Soup(200, 100, 0.5)
    tomato = Tomato(30, 100, 'RED')

    cook ([bread, soup, tomato])

if __name__ = '__main__':
    main()


    
