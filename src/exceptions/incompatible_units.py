class IncompatibleUnitsError(Exception):
    """Exception raised when two units were found of different types

    Attributes:
        message -- explanation of the error
    """

    error_code: int = 1

    def __init__(self, unittype_1: str, unittype_2: str) -> None:
        self.message: str = f"Trying to convert {unittype_1} to {unittype_2} failed: Incompatible unit types."

    def __str__(self) -> str:
        return f"{self.message} (Error Code: {self.error_code})"
