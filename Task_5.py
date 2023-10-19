# animal1-herbivore; animal2-predator

class Animal:
    def eat(self) -> str:
        return 'The animal ate!'
    herbivore = Animal()
    print(herbivore.eat())
    'The animal ate!'
    class Animal:
        def __str__(self) -> str:
            return 'This animal!'
        def eat(self):
            return 'The animal ate!'
        herbivore = Animal()
        print(herbivore)
        'This animal!'
        predator = Animal()
        print(predator)
        'This animal!'
        class Herbivore(Animal):
            def sound(self) -> str:
                return 'Makes a sound 1'
        class Predator(Animal):
            def sound(self) ->:
                return 'Makes a sound 2'


