class BaseConverter:

    conversion_multipliers: dict[str, float] = {"base": 1, "half": 2}

    units: dict[str, list[str]] = {"base": ["b", "bs", "base"], "half": ["h", "hf", "half"]}

    type: str = "Base class"

    # Printing methods
    def __str__(self) -> str:  # pragma: no cover
        return str(self.type + "\n" + str(self.conversion_multipliers) + "\n" + str(self.units))

    def get_multipliers(self) -> dict[str, float]:  # pragma: no cover
        return self.conversion_multipliers

    def get_units(self) -> dict[str, list[str]]:  # pragma: no cover
        return self.units

    def get_type(self) -> str:  # pragma: no cover
        return self.type

    # Functional methods
    def convert(self, number: float, input_unit: str, output_unit: str) -> float:
        multiplier: float = self.get_multipliers()[output_unit] / self.get_multipliers()[input_unit]
        return number * multiplier

    def which_unit(self, symbol: str) -> dict[str, str]:
        found_unit: str = ""
        for unit, symbol_list in self.get_units().items():
            if symbol in symbol_list:
                found_unit: str = unit
        return {"unit": found_unit, "type": self.get_type()}
