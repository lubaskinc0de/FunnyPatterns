from abc import ABC, abstractmethod


class AbstractPizza(ABC):

    @abstractmethod
    def eat(self):
        raise NotImplementedError()


class PizzaBridge:
    _pizza_impl: AbstractPizza

    def eat(self):
        return self._pizza_impl.eat()

    def set_impementation(self, implementation: AbstractPizza):
        self._pizza_impl = implementation


class PeperoniPizza(AbstractPizza):
    def eat(self):
        print('You eat a peperoni!')


class CheesePizza(AbstractPizza):
    gramms_of_cheese: int

    def __init__(self, gramms_of_cheese):
        self.gramms_of_cheese = gramms_of_cheese

    def eat(self):
        print(f'You eat a chesse pizza with gramms of cheese = {self.gramms_of_cheese}')


if __name__ == '__main__':
    bridge = PizzaBridge()

    bridge.set_impementation(PeperoniPizza())
    bridge.eat()

    bridge.set_impementation(CheesePizza(10))
    bridge.eat()
