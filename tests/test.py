#!/bin/python3

# Import converters
from src.converters.area_converter import AreaConverter
from src.converters.base_converter import BaseConverter
from src.converters.distance_converter import DistanceConverter
from src.converters.time_converter import TimeConverter
from src.converters.volume_converter import VolumeConverter
from src.converters.weight_converter import WeightConverter

# Import orchestrator class
from src.orchestrator import Orchestrator

# Import input class
from src.input.input import Input

# Import exceptions
from src.exceptions.invalid_number_of_input_items import InvalidNumberOfInputArgumentsError
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError
from src.exceptions.incompatible_units import IncompatibleUnitsError
from src.exceptions.invalid_rounding_input import InvalidRoundingInputError
from src.exceptions.american_detected import AmericanDetectedError

# Import python modules
import unittest

class TestConverterObjects(unittest.TestCase):

    def test_doubling(self) -> None:
        input_number: float = 21
        output_expect: float = 42
        output_test: float = BaseConverter().convert(input_number, "base", "half")
        self.assertEqual(output_expect, output_test)

    def test_meter_to_centimeter(self) -> None:
        input_number: float = 0.42
        output_expect: float = 42
        output_test: float = DistanceConverter().convert(input_number, "meter", "centimeter")
        self.assertEqual(output_expect, output_test)

    def test_feet_to_meter(self) -> None:
        input_number: float = 137.79527559
        output_expect: float = 42
        output_test: float = DistanceConverter().convert(input_number, "foot", "meter")
        self.assertAlmostEqual(output_expect, output_test)

    def test_hour_to_day(self) -> None:
        input_number: float = 48
        output_expect: float = 2
        output_test: float = TimeConverter().convert(input_number, "hour", "day")
        self.assertAlmostEqual(output_expect, output_test)

    def test_if_symbol_can_be_found(self) -> None:
        input_symbol: str = "hf"
        output_expect: str = "half"
        output_test: dict[str, str] = BaseConverter().which_unit(input_symbol)
        self.assertEqual(output_expect, output_test["unit"])

    def test_if_symbol_that_is_not_present_returns_an_empty_string(self) -> None:
        input_symbol: str = "foo"
        output_expect: str = ""
        output_test: dict[str, str]  = BaseConverter().which_unit(input_symbol)
        self.assertEqual(output_expect, output_test["unit"])

    def test_if_there_are_duplicate_unit_definitions(self) -> None:
        all_units: list[str] = []
        duplicates: list[str] = []
        for category in [AreaConverter().get_units(), DistanceConverter().get_units(), TimeConverter().get_units(), VolumeConverter().get_units(), WeightConverter().get_units()]:
            for unit_definitions in category.values():
                for unit in unit_definitions:
                    if unit in all_units:
                        duplicates.append(unit)
                    else:
                        all_units.append(unit)
        self.assertEqual(duplicates, [])

class TestInputClass(unittest.TestCase):

    def test_input_initialization(self) -> None:
        input_command: str = "2 metre to centimetre"
        output_input_value_expect: float = 2
        output_raw_input_unit_expect: str = "metre"
        output_raw_output_unit_expect: str = "centimetre"
        output_decimals_expect: int = -1
        output_unitless_output_expect: bool = False
        output_test: Input = Input(input_command)
        self.assertEqual(output_test.get_input_value(), output_input_value_expect)
        self.assertEqual(output_test.get_raw_input_unit(), output_raw_input_unit_expect)
        self.assertEqual(output_test.get_raw_output_unit(), output_raw_output_unit_expect)
        self.assertEqual(output_test.get_decimals(), output_decimals_expect)
        self.assertEqual(output_test.get_unitless_output(), output_unitless_output_expect)

    def test_if_round_integer_is_correctly_detected(self) -> None:
        input_command: str = "303 seconds to minutes round 2"
        output_decimals_expect: int = 2
        output_test: Input = Input(input_command)
        self.assertEqual(output_test.get_decimals(), output_decimals_expect)

    def test_if_string_following_round_results_in_a_InvalidRoundingInputError(self) -> None:
        input_command: str = "303 seconds to minutes round down"
        self.assertRaises(InvalidRoundingInputError, Input, input_command)

    def test_if_float_following_round_results_in_a_InvalidRoundingInputError(self) -> None:
        input_command: str = "303 seconds to minutes round 1.3"
        self.assertRaises(InvalidRoundingInputError, Input, input_command)

    def test_if_unitless_detection_works(self) -> None:
        input_command: str = "450 grams to kilograms unitless"
        output_unitless_output_expect: bool = True
        output_test: Input = Input(input_command)
        self.assertEqual(output_test.get_unitless_output(), output_unitless_output_expect)

    def test_if_multiple_to_results_in_InvaludNumberOfInputArgumentsError(self) -> None:
        input_command: str = "20m to be or not to be that is the question"
        self.assertRaises(InvalidNumberOfInputArgumentsError, Input, input_command)

    def test_if_a_string_at_the_start_results_in_a_NoNumberFoundError(self) -> None:
        input_command: str = "please convert 40 square meters to square feet"
        self.assertRaises(NoNumberFoundError, Input, input_command)

    def test_if_an_American_unit_results_in_an_AmericanDetectedError(self) -> None:
        input_command: str = "23 football fields to square feet"
        self.assertRaises(AmericanDetectedError, Input, input_command)

    def test_if_the_first_number_is_selected_when_multiple_are_submitted(self) -> None:
        input_command: str = "400 5.3 69 square meters to square decameters"
        output_input_value_expect: float = 400
        output_test: Input = Input(input_command)
        self.assertEqual(output_test.get_input_value(), output_input_value_expect)

    def test_if_multiple_strings_as_unit_are_handled_correctly(self) -> None:
        input_command: str = "400 square meters bilbo baggins to square decameters"
        output_raw_input_unit_expect: str = "square meter"
        output_raw_output_unit_expect: str = "square decameter"
        output_test: Input = Input(input_command)
        self.assertEqual(output_test.get_raw_input_unit(), output_raw_input_unit_expect)
        self.assertEqual(output_test.get_raw_output_unit(), output_raw_output_unit_expect)

class TestOrchestratorClass(unittest.TestCase):
    
    def test_if_conversion_works(self) -> None:
        input_command: str = "2 metre to centimetre"
        output_expect: str = "200 centimeters (cm)"
        output_test: str = Orchestrator().orchestrate_conversion(input_command)
        self.assertEqual(output_expect, output_test)
    
    def test_if_the_resulting_unit_is_singular_if_the_answer_is_precisely_1(self) -> None:
        input_command: str = "100 cm to m"
        output_expect: str = "1 meter (m)"
        output_test: str = Orchestrator().orchestrate_conversion(input_command)
        self.assertEqual(output_expect, output_test)

    def test_if_the_output_is_rounded_correctly(self) -> None:
        input_command: str = "1 metre to yard round 3"
        output_expect: str = "1.094 yards (yd)"
        output_test: str = Orchestrator().orchestrate_conversion(input_command)
        self.assertEqual(output_expect, output_test)

    def test_if_units_ending_in_s_are_correctly_detected(self) -> None:
        input_command: str = "2 cups to quarts round 1"
        output_expect: str = "0.5 quarts (qt)"
        output_test: str = Orchestrator().orchestrate_conversion(input_command)
        self.assertEqual(output_expect, output_test)

    def test_if_giberrish_input_unit_results_in_a_NoUnitFoundError(self) -> None:
        input_command: str = "23ef2t43fe to square feet"
        self.assertRaises(NoUnitFoundError, Orchestrator().orchestrate_conversion, input_command)

    def test_if_giberrish_output_unit_results_in_a_NoUnitFoundError(self) -> None:
        input_command: str = "20 minutes to 1dnfu219nt2wf3940t"
        self.assertRaises(NoUnitFoundError, Orchestrator().orchestrate_conversion, input_command)

    def test_if_correctly_formatted_non_existent_unit_results_in_a_NoUnitFoundError(self) -> None:
        input_command: str = "23 biscuits to kg"
        self.assertRaises(NoUnitFoundError, Orchestrator().orchestrate_conversion, input_command)

    def test_if_non_matching_unit_types_result_in_a_IncompatibleUnitsError(self) -> None:
        input_command: str = "30 seconds to lightyears"
        self.assertRaises(IncompatibleUnitsError, Orchestrator().orchestrate_conversion, input_command)

    def test_if_unitless_output_works(self) -> None:
        input_command: str = "2000g to kg unitless"
        output_expect: str = "2"
        output_test: str = Orchestrator().orchestrate_conversion(input_command)
        self.assertEqual(output_expect, output_test)

if __name__ == '__main__':
    unittest.main()
