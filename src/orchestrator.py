# Import exceptions
from src.exceptions.no_unit_found import NoUnitFoundError
from src.exceptions.incompatible_units import IncompatibleUnitsError

# Import converters
from src.converters.area_converter import AreaConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.temperature_converter import TemperatureConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

# Import Input class
from src.input.input import Input

class Orchestrator:

    def __find_unit(self, unit: str) -> dict[str, str]:
        out_unit: dict[str, str] = {
            "unit": '',
            "type": ''
        }
        for found_unit in [
                AreaConverter().which_unit(unit),
                DistanceConverter().which_unit(unit),
                TemperatureConverter().which_unit(unit),
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
        input_data: Input = Input(command)

        # Early return in case the help page was requested
        if input_data.get_help_page() != "":
            return input_data.get_help_page()
        # If the input was submitted for conversion, continue
        else:
            # Find out if the submitted unit is valid and, if so, to which data type it belongs
            input_unit_and_type: dict[str, str] = self.__find_unit(input_data.get_raw_input_unit())
            output_unit_and_type: dict[str, str] = self.__find_unit(input_data.get_raw_output_unit())
            if input_unit_and_type["type"] != output_unit_and_type["type"]:
                raise IncompatibleUnitsError(f"{input_unit_and_type["unit"]} ({input_data.get_raw_input_unit()})", f"{output_unit_and_type["unit"]} ({input_data.get_raw_output_unit()})")

            # Assign input data to seperate variables for increased readability
            input_value: float = input_data.get_input_value()
            input_unit: str = input_unit_and_type["unit"]
            output_unit: str = output_unit_and_type["unit"]
            unit_type: str = input_unit_and_type["type"]

            # Apply the correct conversion method
            output: str = ''
            for ConverterClass in [
                    AreaConverter,
                    DistanceConverter,
                    TemperatureConverter,
                    TimeConverter,
                    VolumeConverter,
                    WeightConverter
                ]:
                if ConverterClass().get_type() == unit_type:
                    output_value: float = ConverterClass().convert(input_value, input_unit, output_unit)
                    output_symbol: str = ConverterClass().get_units()[output_unit][0]
                    if output_value != 1 and unit_type != "temperature":
                        output_unit: str = output_unit + 's'
                    if input_data.get_unitless_output():
                        output: str = str(self.__round(output_value, input_data.get_decimals()))
                    else:
                        output: str = f"{str(self.__round(output_value, input_data.get_decimals()))} {output_unit.replace("_", " ")} ({output_symbol})"
            if output != '':
                return output
            else:
                return f"Unable to convert input: {command}"
