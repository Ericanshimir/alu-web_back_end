import Car from './10-car';

const EVCarSymbol = Symbol('EVCar');

export default class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super(brand, motor, color);
    this._range = range;
    this[EVCarSymbol] = Car;  // Symbol to hold the Car constructor
  }

  cloneCar() {
    // Return an instance of Car instead of EVCar
    return new this[EVCarSymbol]();
  }
}