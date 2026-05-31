# Import modules
from re import Match, match, search, split
from sys import exit

# Import exceptions
from src.exceptions.invalid_number_of_input_items import InvalidNumberOfInputArgumentsError
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError
from src.exceptions.incompatible_units import IncompatibleUnitsError
from src.exceptions.invalid_rounding_input import InvalidRoundingInputError
from src.exceptions.american_detected import AmericanDetectedError

# Import converters
from src.converters.area_converter import AreaConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

# Importing Input class
from src.input.input import Input

class Orchestrator:

    def __input_handler(self, command: str) -> Input:

        number_match: str = r"\d+\.\d+|\d+"
        string_match: str = r"[a-zA-Z]+[\s_][a-zA-Z]+|[a-zA-Z]+"

        input_split: list[str] = split("to|round", command)
        if len(input_split) > 3 or (len(input_split) > 2 and 'round' not in command):
            raise InvalidNumberOfInputArgumentsError(input_split)

        input_value_match: Match[str] | None = match(number_match, input_split[0]) # match ensures it starts with a number
        input_unit_match: Match[str] | None = search(string_match, input_split[0]) # search searches through the whole input string
        output_unit_match: Match[str] | None = search(string_match, input_split[1])

        # Check if the string format is correct
        if input_value_match != None:
            input_value: float = float(input_value_match.group().strip())
        else:
            raise NoNumberFoundError(input_split)
        if input_unit_match != None:
            input_unit: str = input_unit_match.group().strip()
        else:
            raise NoUnitFoundError(input_split)
        if output_unit_match != None:
            output_unit: str = output_unit_match.group().strip()
        else:
            raise NoUnitFoundError(input_split)
        
        if len(input_unit) > 2 and input_unit.endswith('s'):
            input_unit: str = input_unit[:-1]
        if len(output_unit) > 2 and output_unit.endswith('s'):
            output_unit: str = output_unit[:-1]

        if len(input_split) == 3:
            try:
                decimals: int = int(input_split[2].strip())
            except ValueError:
                raise InvalidRoundingInputError(input_split[2].strip())
        else:
            decimals: int = -1

        for usa in ["football field", "hamburger", "ford mustang"]:
            if input_unit == usa:
                raise AmericanDetectedError(input_unit)
            elif output_unit == usa:
                raise AmericanDetectedError(output_unit)
        
        return Input(input_value, input_unit, output_unit, decimals)
    
    def __which_unit(self, unit: str) -> dict[str, str]:
        out_unit: dict[str, str] = {
            "unit": '',
            "type": ''
        }
        for found_unit in [
                AreaConverter().which_unit(unit),
                DistanceConverter().which_unit(unit),
                TimeConverter().which_unit(unit),
                VolumeConverter().which_unit(unit),
                WeightConverter().which_unit(unit)
            ]:
            if found_unit["unit"] != '':
                out_unit: dict[str, str] = found_unit
        if out_unit["unit"] != '':
            return out_unit
        else:
            raise NoUnitFoundError([unit])
        
    def __round(self, value: float, decimals: int) -> float | int:
        if decimals > -1:
            rounded_value: float = round(value, decimals)
        else:
            rounded_value: float = value
        if rounded_value == int(rounded_value):
            return int(rounded_value)
        else:
            return rounded_value

    def orchestrate_conversion(self, command: str) -> str:
        # Process input
        # input_split: tuple[float, str, str] = self.__input_handler(command)
        # input_value: float = input_split[0]
        # input_unit_and_type: tuple[str, str] = self.__which_unit(input_split[1])
        # output_unit_and_type: tuple[str, str] = self.__which_unit(input_split[2])
        input_data: Input = self.__input_handler(command)
        input_unit_and_type: dict[str, str] = self.__which_unit(input_data.raw_input_unit)
        output_unit_and_type: dict[str, str] = self.__which_unit(input_data.raw_output_unit)

        # Reserve variables for input
        input_value: float = input_data.input_value
        input_unit: str = ""
        output_unit: str = ""
        unit_type: str = ""

        # Sort the input data
        if input_unit_and_type["type"] != output_unit_and_type["type"]:
            raise IncompatibleUnitsError(f"{input_unit_and_type["unit"]} ({input_data.raw_input_unit})", f"{output_unit_and_type["unit"]} ({input_data.raw_output_unit})")
        else:
            input_unit: str = input_unit_and_type["unit"]
            output_unit: str = output_unit_and_type["unit"]
            unit_type: str = input_unit_and_type["type"]

        # Apply the correct conversion method
        output: str = ''
        for ConverterClass in [AreaConverter, DistanceConverter, TimeConverter, VolumeConverter, WeightConverter]:
            if ConverterClass().type == unit_type:
                output_value: float = ConverterClass().convert(input_value, input_unit, output_unit)
                output_symbol: str = ConverterClass.units[output_unit][0]
                if output_value != 1:
                    output_unit: str = output_unit + 's'
                output: str =  f"{str(self.__round(output_value, input_data.decimals))} {output_unit.replace("_", " ")} ({output_symbol})"
        if output != '':
            return output
        else:
            return f"Unable to convert input: {command}"
