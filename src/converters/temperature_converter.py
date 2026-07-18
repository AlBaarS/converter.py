# Import exceptions
from src.exceptions.invalid_temperature import InvalidTemperatureError

class TemperatureConverter:

    units: dict[str, list[str]] = {
        "Celsius": ["°C","C","Celsius","celsius","centigrade"],
        "Fahrenheit": ["°F","F","Fahrenheit","fahrenheit"],
        "Kelvin": ["K","°K","Kelvin","kelvin"]
    }

    type: str = "temperature"

    # Getter methods
    def __str__(self) -> str:   # pragma: no cover
        return str(self.type + "\n" + str(self.units))
    
    def get_units(self) -> dict[str, list[str]]:   # pragma: no cover
        return self.units
    
    def get_type(self) -> str:                     # pragma: no cover
        return self.type

    # Functional methods
    def convert(self, number: float, input_unit: str, output_unit: str) -> float:
        match input_unit:
            case "Celsius":
                match output_unit:
                    case "Celsius":
                        return number
                    case "Fahrenheit":
                        return self.__convert_Celsius_to_Fahrenheit(number)
                    case "Kelvin":
                        return number + 273.15
                    case _:
                        raise InvalidTemperatureError(output_unit)
            case "Fahrenheit":
                match output_unit:
                    case "Celsius":
                        return self.__convert_Fahrenheit_to_Celsius(number)
                    case "Fahrenheit":
                        return number
                    case "Kelvin":
                        return self.__convert_Fahrenheit_to_Celsius(number) + 273.15
                    case _:
                        raise InvalidTemperatureError(output_unit)
            case "Kelvin":
                match output_unit:
                    case "Celsius":
                        return number - 273.15
                    case "Fahrenheit":
                        return self.__convert_Celsius_to_Fahrenheit(number - 273.15)
                    case "Kelvin":
                        return number
                    case _:
                        raise InvalidTemperatureError(output_unit)
            case _:
                raise InvalidTemperatureError(input_unit)
    
    def __convert_Celsius_to_Fahrenheit(self, number: float) -> float:
        return number * (9 / 5) + 32
    
    def __convert_Fahrenheit_to_Celsius(self, number: float) -> float:
        return (number - 32) * (5 / 9)
    
    def which_unit(self, symbol: str) -> dict[str, str]:
        found_unit: str = ""
        for unit, symbol_list in self.get_units().items():
            if symbol in symbol_list:
                found_unit: str = unit
        return {
            "unit": found_unit,
            "type": self.get_type()
        }
