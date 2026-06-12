# Import modules
from re import Match, match, search, split, sub

# Import exceptions
from src.exceptions.invalid_number_of_input_items import InvalidNumberOfInputArgumentsError
from src.exceptions.no_number_found import NoNumberFoundError
from src.exceptions.no_unit_found import NoUnitFoundError
from src.exceptions.invalid_rounding_input import InvalidRoundingInputError
from src.exceptions.american_detected import AmericanDetectedError

class Input():
    input_value: float
    raw_input_unit: str
    raw_output_unit: str
    decimals: int = -1
    numeric_output: bool = False

    # Builder methods
    def __init__(self, command: str) -> None:
        self.input_value = self.__get_input_value(command)
        self.raw_input_unit = self.__get_raw_unit(command, "input")
        self.raw_output_unit = self.__get_raw_unit(command, "output")
        self.decimals = self.__get_decimals(command)
        self.numeric_output = self.__determine_output_type(command)
            
    def __str__(self) -> str:
        return(
            "input_value: " + str(self.input_value) + "\n" +
            "raw_input_unit: " + self.raw_input_unit + "\n" +
            "raw_output_unit: " + self.raw_output_unit + "\n" +
            "decimals: " + str(self.decimals) + "\n" +
            "numeric_output: " + str(self.numeric_output)
        )
    
    # Input filtering methods
    def __get_input_value(self, command: str) -> float:
        number_match: str = r"\d+\.\d+|\d+"
        input_value_match: Match[str] | None = match(number_match, command)
        if input_value_match != None:
            return float(input_value_match.group().strip())
        else:
            raise NoNumberFoundError(command)

    def __get_raw_unit(self, command: str, in_or_out: str) -> str:
        string_match: str = r"[a-zA-Z]+[\s_][a-zA-Z]+|[a-zA-Z]+"
        command_split: list[str] = split(" to ", sub(r" round \d{1,3}| unitless","",command))

        if len(command_split) == 2:
            if in_or_out == "input":
                unit_match: Match[str] | None = search(string_match, command_split[0])
            else:
                unit_match: Match[str] | None = search(string_match, command_split[1])
        else:
            raise InvalidNumberOfInputArgumentsError(command_split)
        
        if unit_match != None:
            raw_unit: str = unit_match.group().strip()
        else:
            raise NoUnitFoundError(command_split)
        
        if len(raw_unit) > 2 and raw_unit.endswith('s'):
            raw_unit: str = raw_unit[:-1]

        for usa in ["football field", "hamburger", "ford mustang"]:
            if raw_unit == usa:
                raise AmericanDetectedError(raw_unit)
            
        return raw_unit

    def __get_decimals(self, command: str) -> int:
        if "round" in command:
            command_split: list[str] = split(" ", command)

            if command_split[3] == "round":
                round_value: str = command_split[4]     # When the input value and unit are combined and no int output is specified before the round parameter
            elif command_split[4] == "round":
                round_value: str = command_split[5]     # When the input value and unit are not combined or int output is specified before the round parameter
            elif command_split[5] == "round":
                round_value: str = command_split[6]     # When the input value and unit are not combined and int output is specified before the round parameter
            else:
                raise InvalidNumberOfInputArgumentsError(command_split)
            
            try:
                return int(round_value.strip())
            except ValueError:
                raise InvalidRoundingInputError(round_value.strip())
            
        else:
            return -1

    def __determine_output_type(self, command: str) -> bool:
        return "unitless" in command
