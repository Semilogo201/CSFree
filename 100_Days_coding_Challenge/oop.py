class Car:

    #attribute, properties.
    #class attribute(every object can inherit it)
    state = "flying_car"
    color = "silver"
    tyre = "six-tyres"
    mode_of_movement = "water"

# constructor method(creating an object outside of a class)
    def__init__(self) -> None:#called a magic metd abd it wont return anything
        pass
    #instance attribute.
    Car.color = "blue"
    mercedis = Car()
    print(mercedis.state)
    print(mercedis.color)
    print(mercedis.tyre)
    print(mercedis.mode_of_movement)